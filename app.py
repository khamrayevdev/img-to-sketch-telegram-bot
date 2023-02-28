from telegram.ext import CommandHandler, MessageHandler, Filters, filters, ConversationHandler, Updater
from img2sketch import imgtosketch

API_TOKEN = 'Bot token'

def start(update, context):
    update.message.reply_text('Rasm yuboring...')
    return 1

def sketch(update, context):
    chat_id = update.message.chat_id
    rasm_id = update.message.photo[-1]
    photo = context.bot.get_file(rasm_id)
    imgtosketch(photo['file_path'])
    context.bot.send_document(chat_id, open('rasm.jpg', 'rb'))
    return 1

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conv_hand = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [
                MessageHandler(Filters.photo, sketch)
            ]
        },
        fallbacks=[CommandHandler('start', start)]
    )
    dispatcher.add_handler(conv_hand)

    updater.start_polling()
    updater.idle()

main()