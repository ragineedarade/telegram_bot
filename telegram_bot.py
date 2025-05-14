 import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Main menu
main_keyboard = ReplyKeyboardMarkup(
    [
        ["📰 Latest News", "📞 Contact"],
        ["👥 Be a Member", "📦 Become Distributor"],
        ["ℹ️ Help"]
    ],
    resize_keyboard=True
)

# Help submenu
help_keyboard = ReplyKeyboardMarkup(
    [
        ["🏠 Address Issue", "💸 Taking More Charges"],
        ["📰 Paper Quality Issue", "📆 Weekly Guide Not Available"],
        ["✅ Submit Your Query"]
    ],
    resize_keyboard=True
)

# /start command


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"👋 Hello {user.first_name}, welcome to *Raginee Darade Newspaper Bot*! 🗞️\n\n"
        "Please choose an option below:",
        reply_markup=main_keyboard
    )

# General chat handler


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Main menu responses
    if text == "📰 Latest News":
        await update.message.reply_text("🗞️ Today’s headline: 'Tech revolution in Madhya Pradesh!' More updates coming soon.")
    elif text == "📞 Contact":
        await update.message.reply_text("📞 Contact us at: +91-9584531181\n📧 Email: contactz@newspaper.com")
    elif text == "👥 Be a Member":
        await update.message.reply_text("🤝 To become a member, visit: https://newspaper.com/membership")
    elif text == "📦 Become Distributor":
        await update.message.reply_text("🚚 To become a distributor, call us at +91-9584531181\n📧 Email: contact@newspaper.com")

    # Help submenu trigger
    elif text == "ℹ️ Help":
        await update.message.reply_text(
            "🛠 Please select your issue from the options below:",
            reply_markup=help_keyboard
        )

    # Help submenu responses
    elif text == "🏠 Address Issue":
        await update.message.reply_text("📍 Please provide the correct delivery address.")
    elif text == "💸 Taking More Charges":
        await update.message.reply_text("💰 Sorry for the inconvenience. We’ll investigate the extra charges.")
    elif text == "📰 Paper Quality Issue":
        await update.message.reply_text("📄 We regret the quality issue. Please send a photo if possible.")
    elif text == "📆 Weekly Guide Not Available":
        await update.message.reply_text("🗓️ Weekly Guide will be sent within 24 hours. Sorry for the delay.")
    elif text == "✅ Submit Your Query":
        await update.message.reply_text("📝 Thank you! Your query has been recorded and our support team will reach out soon.")

    else:
        await update.message.reply_text("❓ I didn’t understand that. Please use the menu buttons.")

# Run the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(
        # Replace with your actual token
        "8153737351:AAEeJhlgnkbJGkxIlOvCLJMU0jCeFpfPfj4").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Newspaper Bot is running...")
    app.run_polling()
