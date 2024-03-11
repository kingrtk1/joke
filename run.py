import random
import requests
from telegram.ext import Updater, CommandHandler

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text(
        "টাইম পাস বটে আপনাকে স্বাগতম! নিম্নলিখিত কাজগুলি করতে পারেন:\n"
        "/joke - একটি যেকোনো মজার কৌতুক পান\n"
        "/trivia - একটি যেকোনো তথ্য পান\n"
        "/fact - একটি আদ্ভুত তথ্য পান"
    )

# Define a function to handle the /joke command
def joke(update, context):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    joke = f"{data['setup']}\n\n{data['punchline']}"
    update.message.reply_text(joke)

# Define a function to handle the /trivia command
def trivia(update, context):
    response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
    data = response.json()
    question = data['results'][0]['question']
    options = data['results'][0]['incorrect_answers']
    correct_answer = data['results'][0]['correct_answer']
    options.append(correct_answer)
    random.shuffle(options)
    options_text = '\n'.join(options)
    trivia_question = f"{question}\n\n{options_text}"
    update.message.reply_text(trivia_question)

# Define a function to handle the /fact command
def fact(update, context):
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    data = response.json()
    fact_text = data['text']
    update.message.reply_text(fact_text)

# Define a main function to start the bot
def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    updater = Updater('6809169766:AAGk6rd_cuqZukNrHvGJIVSA1pvWi0w48tA', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("joke", joke))
    dp.add_handler(CommandHandler("trivia", trivia))
    dp.add_handler(CommandHandler("fact", fact))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

# Call the main function to start the bot
if __name__ == '__main__':
    main()
