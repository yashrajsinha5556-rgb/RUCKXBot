import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
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


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "pricing":
        await query.edit_message_text(
            """💰 Pricing

🎬 Basic Edit - ₹299
🔥 Premium Edit - ₹699
🚀 Advanced Edit - ₹1499

📩 Contact for custom pricing.
"""
        )

    elif query.data == "contact":
        await query.edit_message_text(
            """📞 Contact

Telegram: @RUCKXS
Email: info9edits@gmail.com
"""
        )

    elif query.data == "faq":
        await query.edit_message_text(
            """❓ FAQ

Q: Delivery Time?
A: 24-48 Hours

Q: Revision?
A: Yes

Q: Payment?
A: UPI / Bank Transfer
"""
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
