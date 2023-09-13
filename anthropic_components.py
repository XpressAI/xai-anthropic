import os

from xai_components.base import InArg, OutArg, InCompArg, Component, BaseComponent, secret, xai_component
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT


@xai_component
class AnthropicAuthorize(Component):
    """Sets the API key for the Anthropic client.

    ##### inPorts:
    - api_key: API key for the Anthropic API.
    - from_env: Boolean value indicating whether the API key is to be fetched from environment variables. 
    """
    api_key: InArg[secret]
    from_env: InArg[bool]

    def execute(self, ctx) -> None:
        if self.from_env.value:
            ctx['anthropic'] = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        else:
            ctx['anthropic'] = Anthropic(api_key=self.api_key.value)


@xai_component
class AnthropicGenerate(Component):
    """Generates text using a specified model from Anthropic.

    ##### inPorts:
    - model_name: Name of the model to be used for text generation.
    - prompt: The initial text to generate from.
    - max_tokens: The maximum length of the generated text.
    - temperature: Controls randomness of the output text.

    ##### outPorts:
    - completion: The generated text.
    """

    model_name: InCompArg[str]
    prompt: InCompArg[str]
    max_tokens: InArg[int]
    temperature: InArg[float]
    completion: OutArg[str]

    def execute(self, ctx) -> None:
        prompt = self.prompt.value

        if not prompt.startswith(HUMAN_PROMPT):
            prompt = f"{HUMAN_PROMPT} {prompt}"
        if not prompt.endswith(AI_PROMPT):
            prompt = f"{prompt}{AI_PROMPT}"

        result = ctx['anthropic'].completions.create(
            model=self.model_name.value,
            prompt=prompt,
            max_tokens_to_sample=self.max_tokens.value if self.max_tokens.value is not None else 100,
            temperature=self.temperature.value if self.temperature.value is not None else 1
        )

        self.completion.value = result.completion