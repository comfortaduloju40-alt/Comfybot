import os
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ✅ CORRECT: Read from environment variable
TOKEN = os.getenv("BOT_TOKEN")

# ✅ Add validation
if not TOKEN:
    print("❌ ERROR: BOT_TOKEN environment variable is not set!")
    print("💡 Set it in Render Dashboard → Environment tab")
    exit(1)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ... rest of your button handlers ...

async def main():
    print(f"✅ Bot starting with token: {TOKEN[:10]}...")  # Show first 10 chars
    
    # For now, keep polling for simplicity
    # (We'll switch to webhooks after it works)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
