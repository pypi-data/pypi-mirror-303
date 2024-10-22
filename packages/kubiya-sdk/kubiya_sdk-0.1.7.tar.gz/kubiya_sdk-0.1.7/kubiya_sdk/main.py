import os
import click
import json
import sys
import uvicorn

from kubiya_sdk.kubiya_cli.bundle import bundle as bundle_func
from kubiya_sdk.project_init import CLIProjectInitializer

from .core import load_workflows_and_tools, run_workflow_with_progress, run_tool
from .serialization import KubiyaJSONEncoder
from kubiya_sdk.utils.discovery import discover_workflows_and_tools
from kubiya_sdk.utils.logger import sdk_logger, configure_logger, WorkflowLogger, span
import sentry_sdk


def json_echo(data):
    click.echo(json.dumps(data, cls=KubiyaJSONEncoder, indent=2))


@span("get_workflows_and_tools")
def get_workflows_and_tools(source):
    """Load workflows and tools from the given source."""
    try:
        return discover_workflows_and_tools(source)
    except Exception as e:
        return {"error": str(e)}


@click.group()
@click.option("--json", is_flag=True, help="Output in JSON format only")
@click.option(
    "--log-level",
    default="INFO",
    type=click.Choice(["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]),
    help="Set the logging level",
)
@click.pass_context
def cli(ctx, json, log_level):
    """Kubiya SDK Command Line Interface."""
    ctx.ensure_object(dict)
    ctx.obj["JSON_OUTPUT"] = json
    configure_logger(level=log_level, json_mode=json)


@cli.command()
@click.option(
    "--host", default="0.0.0.0", show_default=True, help="Host to bind the server to"
)
@click.option(
    "--port", default=8000, show_default=True, help="Port to bind the server to"
)
@click.option(
    "--reload", is_flag=True, default=False, help="Enable auto-reload on code changes"
)
@click.pass_context
@span("server")
def server(ctx, host, port, reload):
    """Start the Kubiya SDK server."""
    from .server import create_app

    try:
        with sentry_sdk.start_transaction(op="server", name="Start Kubiya SDK Server"):
            app = create_app()
            if ctx.obj["JSON_OUTPUT"]:
                json_echo(
                    {
                        "message": f"Starting the Kubiya SDK server on {host}:{port}",
                        "host": host,
                        "port": port,
                    }
                )
            else:
                sdk_logger.log(
                    f"Starting the Kubiya SDK server on {host}:{port}...",
                    component="Server",
                )
            uvicorn.run(app, host=host, port=port, reload=reload)
    except Exception as e:
        error_message = f"Error starting the server: {str(e)}"
        if ctx.obj["JSON_OUTPUT"]:
            json_echo({"error": error_message})
        else:
            sdk_logger.log(error_message, component="Server", level="ERROR")
        sentry_sdk.capture_exception(e)
        sys.exit(1)


@cli.command()
@click.option(
    "--source",
    required=True,
    type=click.Path(exists=True),
    help="Source to discover workflows and tools from",
)
@click.pass_context
@span("discover")
def discover(ctx, source: str):
    """Discover workflows and tools from the given source."""
    with sentry_sdk.start_transaction(
        op="discover", name="Discover Workflows and Tools"
    ):
        results = get_workflows_and_tools(source)
        if ctx.obj["JSON_OUTPUT"]:
            json_echo(results)
        else:
            sdk_logger.log("Discovering workflows and tools...", component="Discovery")
            click.echo(json.dumps(results, cls=KubiyaJSONEncoder, indent=2))


@cli.command()
@click.option(
    "--source",
    required=True,
    type=click.Path(exists=True),
    help="Path to the project directory or source",
)
@click.option("--name", required=True, help="Name of the workflow or tool to run")
@click.option(
    "--input",
    type=click.Path(exists=True),
    help="Path to JSON file containing input data",
)
@click.pass_context
@span("run")
def run(ctx, source: str, name: str, input: str):
    """Run a workflow or tool."""
    with sentry_sdk.start_transaction(op="run", name=f"Run {name}"):
        results = get_workflows_and_tools(source)
        workflow = next((w for w in results["workflows"] if w["name"] == name), None)
        tool = next((t for t in results["tools"] if t.name == name), None)

        inputs = {}
        if input:
            try:
                with click.open_file(input, "r") as f:
                    inputs = json.load(f)
            except Exception as e:
                error_message = f"Error reading input file: {str(e)}"
                if ctx.obj["JSON_OUTPUT"]:
                    json_echo({"error": error_message})
                else:
                    sdk_logger.log(error_message, component="Run", level="ERROR")
                sentry_sdk.capture_exception(e)
                sys.exit(1)

        try:
            if workflow:
                with sentry_sdk.start_span(
                    op="run_workflow", description=f"Run workflow '{name}'"
                ):
                    if ctx.obj["JSON_OUTPUT"]:
                        json_echo(
                            {"message": f"Running workflow '{name}'", "workflow": name}
                        )
                    else:
                        sdk_logger.log(f"Running workflow '{name}'...", component="Run")
                    result = run_workflow_with_progress(workflow["instance"], inputs)
                    json_echo(list(result))
            elif tool:
                with sentry_sdk.start_span(
                    op="run_tool", description=f"Run tool '{name}'"
                ):
                    if ctx.obj["JSON_OUTPUT"]:
                        json_echo({"message": f"Running tool '{name}'", "tool": name})
                    else:
                        sdk_logger.log(f"Running tool '{name}'...", component="Run")
                    result = run_tool(tool, inputs)
                    json_echo(result)
            else:
                error_message = f"Workflow or tool '{name}' not found in the source"
                if ctx.obj["JSON_OUTPUT"]:
                    json_echo({"error": error_message})
                else:
                    sdk_logger.log(error_message, component="Run", level="ERROR")
                sys.exit(1)
        except Exception as e:
            error_message = f"Error running '{name}': {str(e)}"
            if ctx.obj["JSON_OUTPUT"]:
                json_echo({"error": error_message})
            else:
                sdk_logger.log(error_message, component="Run", level="ERROR")
            sentry_sdk.capture_exception(e)
            sys.exit(1)


@cli.command()
@click.option(
    "--source",
    required=True,
    type=click.Path(exists=True),
    help="Path to the project directory or source",
)
@click.option("--name", required=True, help="Name of the workflow or tool to describe")
@click.pass_context
@span("describe")
def describe(ctx, source: str, name: str):
    """Describe a workflow or tool."""
    with sentry_sdk.start_transaction(op="describe", name=f"Describe {name}"):
        results = get_workflows_and_tools(source)
        workflow = next((w for w in results["workflows"] if w["name"] == name), None)
        tool = next((t for t in results["tools"] if t.name == name), None)

        try:
            if workflow:
                with sentry_sdk.start_span(
                    op="describe_workflow", description=f"Describe workflow '{name}'"
                ):
                    if not ctx.obj["JSON_OUTPUT"]:
                        click.echo(f"📋 Describing workflow '{name}'...")
                    description = {
                        "type": "workflow",
                        "name": workflow["name"],
                        "description": workflow["instance"].description,
                        "steps": [
                            {
                                "name": step_name,
                                "description": step.description,
                                "icon": step.icon,
                                "label": step.label,
                                "next_steps": step.next_steps,
                                "conditions": step.conditions,
                            }
                            for step_name, step in workflow["instance"].steps.items()
                        ],
                        "entry_point": workflow["instance"].entry_point,
                    }
            elif tool:
                with sentry_sdk.start_span(
                    op="describe_tool", description=f"Describe tool '{name}'"
                ):
                    if not ctx.obj["JSON_OUTPUT"]:
                        click.echo(f"🔧 Describing tool '{name}'...")
                    description = {
                        "type": "tool",
                        "name": tool.name,
                        "description": tool.description,
                        "args": [arg.dict() for arg in tool.args],
                        "env": tool.env,
                    }
            else:
                error_message = f"Workflow or tool '{name}' not found in the source"
                if ctx.obj["JSON_OUTPUT"]:
                    json_echo({"error": error_message})
                else:
                    sdk_logger.log(error_message, component="Describe", level="ERROR")
                sys.exit(1)

            json_echo(description)
        except Exception as e:
            error_message = f"Error describing '{name}': {str(e)}"
            if ctx.obj["JSON_OUTPUT"]:
                json_echo({"error": error_message})
            else:
                sdk_logger.log(error_message, component="Describe", level="ERROR")
            sentry_sdk.capture_exception(e)
            sys.exit(1)


@cli.command()
@click.option(
    "--source",
    required=True,
    type=click.Path(exists=True),
    help="Path to the project directory or source",
)
@click.option("--workflow", required=True, help="Name of the workflow to visualize")
@click.pass_context
@span("visualize")
def visualize(ctx, source: str, workflow: str):
    """Visualize a workflow."""
    with sentry_sdk.start_transaction(op="visualize", name=f"Visualize {workflow}"):
        results = get_workflows_and_tools(source)
        workflow_obj = next(
            (w for w in results["workflows"] if w["name"] == workflow), None
        )

        try:
            if not workflow_obj:
                error_message = f"Workflow '{workflow}' not found in the source"
                if ctx.obj["JSON_OUTPUT"]:
                    json_echo({"error": error_message})
                else:
                    sdk_logger.log(error_message, component="Visualize", level="ERROR")
                sys.exit(1)

            with sentry_sdk.start_span(
                op="generate_mermaid",
                description=f"Generate Mermaid diagram for '{workflow}'",
            ):
                if not ctx.obj["JSON_OUTPUT"]:
                    click.echo(f"🎨 Visualizing workflow '{workflow}'...")
                mermaid_diagram = workflow_obj["instance"].to_mermaid()
                if ctx.obj["JSON_OUTPUT"]:
                    json_echo({"mermaid": mermaid_diagram})
                else:
                    click.echo(mermaid_diagram)
        except Exception as e:
            error_message = f"Error visualizing workflow '{workflow}': {str(e)}"
            if ctx.obj["JSON_OUTPUT"]:
                json_echo({"error": error_message})
            else:
                sdk_logger.log(error_message, component="Visualize", level="ERROR")
            sentry_sdk.capture_exception(e)
            sys.exit(1)


@cli.command()
def init():
    """Initialize a new Kubiya project."""
    CLIProjectInitializer().initialize()


@cli.command()
@click.option(
    "-i", "--ignore-dir", "ignore_dirs", multiple=True, help="Directories to ignore"
)
def bundle(ignore_dirs: tuple[str]):
    try:
        """Bundle Kubiya tools in the project"""
        current_dir = os.getcwd()
        bundle_func(
            current_dir,
            ignore_dirs=ignore_dirs,
        )
    except Exception as e:
        sdk_logger.log(
            f"Error bundling tools: {str(e)}", component="Bundle", level="ERROR"
        )


if __name__ == "__main__":
    cli()
