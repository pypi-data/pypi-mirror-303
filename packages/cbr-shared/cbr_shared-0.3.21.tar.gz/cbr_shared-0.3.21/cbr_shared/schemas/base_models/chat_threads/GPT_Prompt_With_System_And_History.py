from typing                                                import Optional

from cbr_shared.schemas.base_models.chat_threads.GPT_History            import GPT_History
from cbr_shared.schemas.base_models.chat_threads.GPT_Prompt_With_System import GPT_Prompt_With_System


class GPT_Prompt_With_System_And_History(GPT_Prompt_With_System):
    histories      : Optional[list[GPT_History]] = None