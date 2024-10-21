from typing import Any


class BaseClient:
    def __init__(
        self, assistant_id: str, assistant_version: str, api_key: str, host: str = "https://infer-v2.conva.ai"
    ):
        self.assistant_id: str = assistant_id
        self.api_key: str = api_key
        self.assistant_version: str = assistant_version
        self.host: str = host
        self.keep_conversation_history: bool = True
        self.domain: str = ""
        self.assistant_context: dict = {}

    def set_assistant_context(self, assistant_context: dict[str, Any]):
        self.assistant_context = assistant_context
