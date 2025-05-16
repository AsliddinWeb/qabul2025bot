from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from messages import messages_handler, contact_handler

from buttons import BUTTON_HOME
from config import BOT_TOKEN
from states import BotState


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Change State
    context.user_data['state'] = BotState.START

    first_name = update.effective_user.first_name
    greeting_text = (
        f"👋 Salom, <b>{first_name}</b>!\n\n"
        "🎓 Bu — <b>Xalqaro Innovatsion Universitet</b>ning rasmiy <b>qabul bot</b>i.\n"
        "📝 Ariza topshirish va ma’lumot olish uchun menyudan foydalaning ⬇️"
    )
    await update.message.reply_text(text=greeting_text, reply_markup=BUTTON_HOME, parse_mode="HTML")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    print("🚀 Bot ishga tushdi!")

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(MessageHandler(filters.TEXT, messages_handler))
    app.add_handler(MessageHandler(filters.CONTACT, contact_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
