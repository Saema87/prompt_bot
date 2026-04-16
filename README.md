# 🤖 Prompt Optimizer Telegram Bot

Turn rough ideas into professional prompts for ChatGPT, Claude, Gemini, Midjourney, Flux, and more — right inside Telegram.

**100% free stack:**
- 🆓 **Groq API** (`llama-3.1-8b-instant`) — 14,400 req/day, no credit card
- 🆓 **Vercel serverless** — 100k invocations/day, never sleeps, free SSL
- 🆓 **Telegram Bot API** — always free
- 🆓 **Zero dependencies** — only Python stdlib, instant cold starts

## ✨ Features

- 4 optimization modes: **General**, **Image**, **Coding**, **Writing**
- Mode selection via simple prefix: `/image`, `/code`, `/write`, `/general`
- Copy-to-clipboard-ready formatted output
- Typing indicators
- Graceful error handling
- Channel promotion built in (`@ai_prompts1`)

---

## 🚀 Deployment (15 minutes, all free)

### Step 1 — Create the Telegram bot

1. Open Telegram, search for **@BotFather**.
2. Send `/newbot` and follow the prompts.
3. Copy the **bot token** (looks like `123456789:ABCdef...`).
4. Optional: send `/setdescription`, `/setabouttext`, `/setuserpic` to customize.

### Step 2 — Get a free Groq API key

1. Go to https://console.groq.com/keys
2. Sign up with Google/GitHub (no credit card).
3. Click **Create API Key**, copy it (starts with `gsk_`).

### Step 3 — Push this project to GitHub

```bash
cd prompt-optimizer-bot
git init
git add .
git commit -m "Initial commit"
# Create a new repo on github.com, then:
git remote add origin https://github.com/YOUR_USERNAME/prompt-optimizer-bot.git
git push -u origin main
```

### Step 4 — Deploy to Vercel

1. Go to https://vercel.com → sign in with GitHub (free).
2. Click **Add New → Project** → import your repo.
3. In the import screen, click **Environment Variables** and add:
   - `BOT_TOKEN` = your Telegram bot token
   - `GROQ_API_KEY` = your Groq key
4. Click **Deploy**. Wait ~30 seconds.
5. Copy your deployment URL (e.g., `https://prompt-optimizer-bot.vercel.app`).

### Step 5 — Connect the webhook

On your local machine:

```bash
# Put your bot token in a .env file first
cp .env.example .env
# Edit .env and paste your BOT_TOKEN

# Point Telegram at your Vercel URL
python set_webhook.py https://your-project.vercel.app
```

You should see `{"ok": true, "result": true, "description": "Webhook was set"}`.

### Step 6 — Test it

Open Telegram, find your bot, send:

```
/start
```

Then try:

```
/image astronaut reading Rumi poetry at night
```

🎉 Done.

---

## 💡 Usage examples

| Input | Mode |
|---|---|
| `write email asking for raise` | General (default) |
| `/image cyberpunk samurai in rain` | Image |
| `/code python script that summarizes pdfs` | Coding |
| `/write linkedin post about ai education` | Writing |

---

## 📁 Project structure

```
prompt-optimizer-bot/
├── api/
│   └── webhook.py       # Main bot logic (single file)
├── vercel.json          # Vercel config
├── requirements.txt     # Empty — zero dependencies
├── set_webhook.py       # Helper to set Telegram webhook
├── .env.example         # Environment variables template
└── README.md
```

---

## 🔧 Customization

**Change the AI model** — edit `GROQ_MODEL` env var on Vercel:
- `llama-3.1-8b-instant` (default, super fast)
- `llama-3.3-70b-versatile` (smarter, slightly slower)
- `openai/gpt-oss-20b` (another free Groq option)

**Add new modes** — edit `SYSTEM_PROMPTS` in `api/webhook.py`, add to `detect_mode()`.

**Change the branding** — edit `WELCOME`, `MODE_HELP`, `EXAMPLES` strings.

---

## 📈 Scaling to SaaS / Premium (later)

When you're ready to monetize, the upgrade path is clean:

| v1 (Free) | v2 (Premium) |
|---|---|
| Stateless, no DB | Add **Upstash Redis** free tier for usage tracking |
| No user accounts | Add **Supabase** free tier for auth + history |
| One model | Gate GPT-OSS / Llama-70B behind a paid tier |
| No rate limits | Rate-limit free users (e.g., 20/day) |
| No persistence | Save prompt history; let users export |

**Payment integration options that work from Pakistan:**
- **Telegram Stars** — native in-bot payments (Telegram takes 30%, no setup)
- **Lemon Squeezy** — accepts international cards, pays Payoneer
- **Gumroad** — sell premium prompt packs as a funnel to the bot

---

## 🐛 Troubleshooting

**Bot doesn't respond:**
```bash
python set_webhook.py status
```
Check `last_error_message`. If the URL is wrong, re-run `set_webhook.py` with the correct URL.

**"Webhook request timed out":**
Groq calls should finish in 1–3 seconds. If timing out, try the faster 8b model.

**"Bad Request: can't parse entities":**
Rare markdown escape issue. The bot auto-retries without markdown, so user still gets a reply.

**Vercel deployment fails:**
Make sure `vercel.json` is at the project root, and `api/webhook.py` exists.

---

## 📊 Free tier limits (for reference)

| Service | Free tier | Enough for |
|---|---|---|
| Groq | 14,400 req/day | ~500 daily active users |
| Vercel | 100k invocations/day | Plenty |
| Telegram | Unlimited | Unlimited |

You can run a meaningfully active bot on free tier indefinitely.

---

Built with ❤️ for **@ai_prompts1** · **@AI_Newz_Hub** · **@AI_courses0**
