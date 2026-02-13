from anthropic import AnthropicFoundry
import os

endpoint = os.getenv("ANTHROPIC_BASE_URL", "https://gianm-mlkugit4-swedencentral.services.ai.azure.com/anthropic/")
deployment_name = os.getenv("ANTHROPIC_DEPLOYMENT", "claude-opus-4-6-swedish")
api_key = "4qNFpnBawn12BwejvHDltgSPfoUc7R4YQDRXPBr9bUq2ShAYgkvdJQQJ99CBACfhMk5XJ3w3AAAAACOGvumV"

if not api_key:
    raise RuntimeError("Missing ANTHROPIC_API_KEY environment variable. Set it before running this script to avoid embedding secrets in source files.")

client = AnthropicFoundry(
    api_key=api_key,
    base_url=endpoint
)

message = client.messages.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ],
    max_tokens=1024,
)

print(message.content)