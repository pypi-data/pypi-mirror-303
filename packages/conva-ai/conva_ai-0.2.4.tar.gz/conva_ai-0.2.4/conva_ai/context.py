from pydantic import BaseModel
from typing import Any, Dict


class ConversationContext(BaseModel):
    assistant_context: Dict[str, Any] = {}
    conversation_history: str = ""
    capability_context: Dict[str, Any] = {}
