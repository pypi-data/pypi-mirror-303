from pydantic import BaseModel
from typing import Dict, Any, List


class ConvaAIResponse(BaseModel):
    request_id: str
    input_query: str
    message: str
    reason: str = ""
    response_language: str
    is_final: bool
    domain_name: str | None = None
    app_name: str | None = None
    category: str | None = None
    llm_key: str | None = None
    message_type: str | None = None
    parameters: Dict[str, Any] = {}
    related_queries: List[str] = []
    conversation_history: str = ""
    is_error: bool = False
    is_unsupported: bool = False
    tool_name: str = ""
    is_parameter_complete: bool = False
