from litellm import Router

from lego.litellm.settings import (
    CustomLLMChatSettings,
    LiteLLMProxyModel,
    LiteLLMSettings,
)
from lego.settings import AmazonAccess


def build_bedrock_model(
    model: str, model_alias: str = "bedrock_model"
) -> LiteLLMProxyModel:
    """Build a snapshot of a Bedrock model."""
    return LiteLLMProxyModel(
        provider=AmazonAccess(),
        model_settings=CustomLLMChatSettings(model=model),
        proxy_settings=LiteLLMSettings(model_alias=model_alias),
    )


def build_litellm_router(models: list[LiteLLMProxyModel], **kwargs) -> Router:
    """Build a Bedrock model from a Pydantic model."""
    return Router(model_list=[model.serialize() for model in models], **kwargs)


if __name__ == "__main__":
    router = build_litellm_router(
        [build_bedrock_model("anthropic.claude-3-haiku-20240307-v1:0")]
    )

    print(
        router.completion(
            model="bedrock_model",
            messages=[{"role": "user", "content": "Hello, world!"}],
        )
    )
