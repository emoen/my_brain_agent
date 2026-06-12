"""
GitHub Models API client using your Copilot Business license.
Requires: .venv/bin/pip install openai httpx

Setup:
    Set TOKEN = "your_pat_token" in this file
  (github.com → Settings → Developer settings → Personal access tokens → Fine-grained → models:read)

Run:
        source .venv/bin/activate && python copilot_agent_test.py
        source .venv/bin/activate && python copilot_agent_test.py --diagnose
"""

import os
from openai import OpenAI
import argparse
import httpx

TOKEN = os.environ["GITHUB_TOKEN"]

DEFAULT_CHAT_MODELS = [
    "gpt-4o",
    "gpt-4o-mini",
    "Meta-Llama-3.1-405B-Instruct",
    "Meta-Llama-3.1-8B-Instruct",
]


def fetch_available_models(token: str) -> list[str]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    response = httpx.get(
        "https://models.inference.ai.azure.com/models",
        headers=headers,
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    names = sorted(
        {
            (item.get("name") or item.get("id") or "")
            for item in payload
            if (item.get("name") or item.get("id"))
        },
        key=str.lower,
    )
    return names


def filter_chat_models(models: list[str]) -> list[str]:
    chat_models = []
    for model in models:
        lower = model.lower()
        if "embed" in lower or "embedding" in lower:
            continue
        chat_models.append(model)
    return chat_models


def select_model(chat_models: list[str]) -> str:
    print("\nAvailable chat models for your token:")
    for index, model in enumerate(chat_models, start=1):
        print(f"  {index}. {model}")
    choice = input(f"\nSelect model [1-{len(chat_models)}, default=1]: ").strip() or "1"
    try:
        selected_index = int(choice)
    except ValueError:
        selected_index = 1
    if selected_index < 1 or selected_index > len(chat_models):
        selected_index = 1
    return chat_models[selected_index - 1]


def diagnose_models(client: OpenAI, chat_models: list[str]) -> None:
    print("\nRunning model access diagnostics...\n")
    test_messages = [{"role": "user", "content": "Respond with one word: ok"}]

    for model in chat_models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=test_messages,
                max_tokens=8,
                stream=False,
            )
            output = (response.choices[0].message.content or "").strip()
            print(f"[OK ] {model:35s} | sample='{output}'")
        except Exception as error:
            error_text = str(error)
            if "Unsupported parameter: 'max_tokens'" in error_text:
                try:
                    response = client.chat.completions.create(
                        model=model,
                        messages=test_messages,
                        max_completion_tokens=8,
                        stream=False,
                    )
                    output = (response.choices[0].message.content or "").strip()
                    print(f"[OK ] {model:35s} | sample='{output}'")
                    continue
                except Exception as retry_error:
                    error_text = str(retry_error)

            print(f"[ERR] {model:35s} | {error_text}")
            if "401" in error_text or "Bad credentials" in error_text or "unauthorized" in error_text.lower():
                print("\nAuthentication failed (401). Fix token and retry.")
                print("Checklist:")
                print("  1) Use a GitHub PAT (not Copilot token/session token)")
                print("  2) Token has models:read permission")
                print("  3) Token is not expired/revoked")
                print("  4) Remove extra spaces, quotes, or 'Bearer ' prefix")
                print("  5) If org policies restrict Models, ask org admin")
                break

def run_agent(diagnose: bool = False):
    token = TOKEN.strip().strip('"').strip("'")
    if token.lower().startswith("bearer "):
        token = token[7:].strip()

    if token == "PASTE_YOUR_GITHUB_PAT_HERE":
        raise EnvironmentError(
            "Token placeholder still set. Paste real PAT into TOKEN.\n"
            "Create PAT at: github.com → Settings → Developer settings → "
            "Personal access tokens → Fine-grained → models:read"
        )

    if not token:
        raise EnvironmentError(
            "Token not set.\n"
            "Create one at: github.com → Settings → Developer settings → "
            "Personal access tokens → Fine-grained → models:read\n"
            "Then paste it into TOKEN at the top of this file"
        )

    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=token,
    )

    try:
        available_models = fetch_available_models(token)
        chat_models = filter_chat_models(available_models)
    except Exception as model_error:
        print(f"Warning: live model discovery failed: {model_error}")
        print("Falling back to built-in model list.")
        chat_models = DEFAULT_CHAT_MODELS

    if not chat_models:
        raise RuntimeError("No chat models available for this token.")

    print("\nLive model catalog for this token:")
    for model in available_models if 'available_models' in locals() else chat_models:
        print(f"  - {model}")

    if diagnose:
        diagnose_models(client, chat_models)
        return

    model = select_model(chat_models)
    print(f"\nUsing model: {model}")
    print("Type your message (or 'quit' to exit):\n")

    messages = []

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
            )

            print("Assistant: ", end="", flush=True)
            assistant_reply = ""
            for chunk in response:
                delta = chunk.choices[0].delta.content or ""
                print(delta, end="", flush=True)
                assistant_reply += delta
            print()

            # Keep conversation history for multi-turn
            messages.append({"role": "assistant", "content": assistant_reply})

        except Exception as e:
            print(f"\nError: {e}")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHub Models chat client")
    parser.add_argument(
        "--diagnose",
        action="store_true",
        help="Probe configured models and print access results",
    )
    args = parser.parse_args()
    run_agent(diagnose=args.diagnose)