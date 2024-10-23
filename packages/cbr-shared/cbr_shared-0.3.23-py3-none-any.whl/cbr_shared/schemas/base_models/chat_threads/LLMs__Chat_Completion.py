from typing import Optional

from cbr_shared.schemas.base_models.chat_threads.GPT_Prompt_With_System_And_History import \
    GPT_Prompt_With_System_And_History


class LLMs__Chat_Completion(GPT_Prompt_With_System_And_History):
    llm_platform: Optional[str] = None
    llm_provider: Optional[str] = None
    llm_model   : Optional[str] = None
    llm_answer  : Optional[str] = None