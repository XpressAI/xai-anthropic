import os
from xai_components.base import InArg, OutArg, InCompArg, Component, BaseComponent, secret, xai_component
from anthropic import Anthropic


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
    - system: Optional system message to set the context or behavior.

    ##### outPorts:
    - completion: The generated text.
    """

    model_name: InCompArg[str]
    prompt: InCompArg[str]
    max_tokens: InArg[int]
    temperature: InArg[float]
    system: InArg[str]
    completion: OutArg[str]

    def execute(self, ctx) -> None:
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": self.prompt.value
                    }
                ]
            }
        ]

        params = {
            "model": self.model_name.value,
            "messages": messages,
            "max_tokens": self.max_tokens.value if self.max_tokens.value is not None else 1000,
            "temperature": self.temperature.value if self.temperature.value is not None else 1
        }

        if self.system.value:
            params["system"] = self.system.value

        result = ctx['anthropic'].messages.create(**params)
        
        # Extract the text content from the response
        self.completion.value = result.content[0].text