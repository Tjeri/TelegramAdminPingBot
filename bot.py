from os import getenv

from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv('BOT_TOKEN')
OVERWATCH_CHANNEL = int(getenv('OVERWATCH_CHANNEL'))
ADMIN_CHANNEL = int(getenv('ADMIN_CHANNEL'))
NOTIFY_MESSAGE = getenv('NOTIFY_MESSAGE')

from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters


async def check_ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.chat.id == OVERWATCH_CHANNEL and '@admin' in update.message.text:
        await context.bot.send_message(chat_id=ADMIN_CHANNEL, text=NOTIFY_MESSAGE)
        await update.message.set_reaction(reaction='👍')


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & filters.ChatType.GROUPS, check_ping))
    application.run_polling(allowed_updates=Update.MESSAGE)


if __name__ == '__main__':
    main()
