from dataclasses import dataclass
from typing                                                         import Optional
from cbr_shared.schemas.data_models.llm_chat.GPT_History            import GPT_History
from cbr_shared.schemas.data_models.llm_chat.GPT_Prompt_With_System import GPT_Prompt_With_System

@dataclass
class GPT_Prompt_With_System_And_History(GPT_Prompt_With_System):
    histories      : Optional[list[GPT_History]] = None