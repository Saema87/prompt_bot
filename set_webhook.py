"""
Run this ONCE after deploying to Vercel to point your bot at the webhook.

Usage:
    python set_webhook.py https://your-project.vercel.app

To check current webhook status:
    python set_webhook.py status

To delete webhook (e.g., for local testing):
    python set_webhook.py delete
"""
import os
import sys
import json
import urllib.request

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

if not BOT_TOKEN:
    # Try reading from .env
    try:
        with open(".env") as f:
            for line in f:
                if line.startswith("BOT_TOKEN="):
                    BOT_TOKEN = line.split("=", 1)[1].strip()
                    break
    except FileNotFoundError:
        pass

if not BOT_TOKEN:
    print("❌ BOT_TOKEN not found. Set it as env var or in .env")
    sys.exit(1)

API = f"https://api.telegram.org/bot{BOT_TOKEN}"


def call(method: str, params=None):
    url = f"{API}/{method}"
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read().decode())


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "status":
        result = call("getWebhookInfo")
        print(json.dumps(result, indent=2))
        return

    if arg == "delete":
        result = call("deleteWebhook")
        print(json.dumps(result, indent=2))
        return

    base_url = arg.rstrip("/")
    webhook_url = f"{base_url}/api/webhook"
    print(f"Setting webhook to: {webhook_url}")
    result = call("setWebhook", {"url": webhook_url})
    print(json.dumps(result, indent=2))

    if result.get("ok"):
        print("\n✅ Webhook set! Send your bot a message on Telegram to test.")
    else:
        print("\n❌ Failed. Check your BOT_TOKEN and URL.")


if __name__ == "__main__":
    main()
