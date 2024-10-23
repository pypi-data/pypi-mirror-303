from osbot_utils.base_classes.Type_Safe import Type_Safe

# todo: finish implementation and wire up to tests and main UI
class CBR__Cache__LLM_Prompts(Type_Safe):
    cached_prompts : dict

    def add_cached_prompt(self, prompt: str, answer: str):
        self.cached_prompts[prompt] = answer

    def get_cached_prompt(self, prompt: str) -> dict:
        return self.cached_prompts.get(prompt)
