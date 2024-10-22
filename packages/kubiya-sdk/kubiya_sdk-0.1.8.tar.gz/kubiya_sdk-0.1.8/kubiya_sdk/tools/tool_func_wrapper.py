from functools import wraps
import inspect
import re
from typing import Callable

from kubiya_sdk.tools.models import Arg, FileSpec, Tool
from kubiya_sdk.tools.registry import tool_registry


def _get_content(args: list[Arg]) -> str:
    arg_names = [arg.name for arg in args]
    arg_str = " ".join([f'"{{{{ .{arg} }}}}"' for arg in arg_names])
    return f"""
curl -LsSf https://astral.sh/uv/install.sh | sh > /dev/null 2>&1
. $HOME/.cargo/env

uv venv > /dev/null 2>&1
. .venv/bin/activate > /dev/null 2>&1

uv pip install -r /tmp/requirements.txt > /dev/null 2>&1

python /tmp/main.py {arg_str}
"""


def _get_main(func_name: str, func_source: str) -> str:
    function_regex = rf"^(@function_tool.*)(def {func_name}\(.*$)"
    match = re.match(function_regex, func_source, re.DOTALL)
    if match is None:
        raise ValueError("Function regex found no match")

    only_func_source = match.group(2)
    return f"""
from typing_extensions import Annotated

import typer

app = typer.Typer(rich_markup_mode=None, add_completion=False)

{only_func_source}

app.command()({func_name})

if __name__ == "__main__":
    app()
"""


def _get_arg_def(param: inspect.Parameter) -> str:
    if param.annotation == bool:
        return f"Input param for arg: {param.name}, type: string, Options: true, false"
    elif param.annotation == int:
        return f"Input param for arg: {param.name}, type: int"
    else:
        return f"Input param for arg: {param.name}, type: string"


def function_tool(
    description: str,
    env: list[str] = [],
    name: str | None = None,
    # image: str = "python:3.12-slim-bullseye",
    image: str = "python:3.12",
    secrets: list[str] = [],
    requirements: list[str] = [],
):
    def f(func: Callable):
        func_name = func.__name__
        source_code = inspect.getsource(func)
        sig = inspect.signature(func)
        args = [
            Arg(
                name=param.name,
                # type="str", this does not work for now...
                default=(
                    param.default if param.default != inspect.Parameter.empty else None
                ),
                required=True if param.default == inspect.Parameter.empty else False,
                description=_get_arg_def(param),
            )
            for param in sig.parameters.values()
        ]
        content = _get_content(args)
        main_code = _get_main(func_name, source_code)

        requirements.append("typer==0.12.5")
        requirements_content = "\n".join(requirements)

        tool = Tool(
            name=name or func_name,
            type="docker",
            image=image,
            description=description,
            args=args,
            env=env,
            secrets=secrets,
            content=content,
            with_files=[
                FileSpec(
                    destination="/tmp/main.py",
                    content=main_code,
                ),
                FileSpec(
                    destination="/tmp/requirements.txt",
                    content=requirements_content,
                ),
            ],
        )

        tool_registry.register("func_name", tool)

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return f
