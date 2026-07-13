import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [InlineKeyboardButton("💰 Pricing", callback_data="pricing")],

        [InlineKeyboardButton("📞 Contact", callback_data="contact")],

        [InlineKeyboardButton("❓ FAQ", callback_data="faq")],

    ]

    text = """
🎬 Welcome to RUCKX Editing

Professional Video Editing Services

✨ Services:
• Reels & Shorts
• YouTube Videos
• Gaming Videos
• Cinematic Edits
• Thumbnail Design

👇 Select an option below.
"""

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
