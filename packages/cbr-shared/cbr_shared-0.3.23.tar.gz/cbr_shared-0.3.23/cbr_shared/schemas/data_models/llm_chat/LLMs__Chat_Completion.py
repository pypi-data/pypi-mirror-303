from dataclasses                                                                import dataclass
from typing                                                                     import Optional
from fastapi.params                                                             import Body
from cbr_shared.schemas.data_models.llm_chat.GPT_Prompt_With_System_And_History import GPT_Prompt_With_System_And_History




SWAGGER_EXAMPLE__LLMs__Chat_Completion  = Body(..., example=dict(user_prompt    ='Good morning, what is 44-2?' ,
                                                                        llm_provider    = "1. Meta"                   ,
                                                                        llm_model       = "llama-3.1-70b-versatile"   ))

@dataclass
class LLMs__Chat_Completion(GPT_Prompt_With_System_And_History):
    llm_platform: Optional[str] = None
    llm_provider: Optional[str] = None
    llm_model   : Optional[str] = None
    llm_answer  : Optional[str] = None