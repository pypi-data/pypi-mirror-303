from dataclasses                                                import dataclass
from typing                                                     import Optional
from cbr_shared.schemas.data_models.llm_chat.GPT_Prompt_Simple  import GPT_Prompt_Simple

@dataclass
class GPT_Prompt_With_System(GPT_Prompt_Simple):
    system_prompts: Optional[list[str]] = None