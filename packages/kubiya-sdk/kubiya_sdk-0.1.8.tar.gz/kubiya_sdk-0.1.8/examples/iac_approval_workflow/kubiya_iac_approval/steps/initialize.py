import uuid
from typing import Dict, Any

async def initialize_request(state: Dict[str, Any]) -> Dict[str, Any]:
    state['request_id'] = str(uuid.uuid4())
    return state
