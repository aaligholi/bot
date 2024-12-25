from telegram.ext import Application, CommandHandler
from flask import Flask

# توکن ربات تلگرام خود را اینجا وارد کنید
TOKEN = "7973226865:AAHWfGn9sj4gOwBYHf6kmWhAUrfLq036j54"

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# تعریف دستور /start
def start(update, context):
    update.message.reply_text("سلام! به ربات من خوش آمدید.")

application.add_handler(CommandHandler("start", start))

@app.route("/")
def index():
    return "ربات در حال اجرا است."

if __name__ == "__main__":
    import threading
    threading.Thread(target=application.run_polling).start()
    app.run(port=5000)
