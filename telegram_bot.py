from pytgbot import Bot
import random
from info import *


def get_response(map, message):
    message = message.lower()
    if message in map.keys():
        answer_list = map[message]
        return random.choice(answer_list)
    else:
        return f"I don't know the answer to your question:\n {message}"

def main():
    API_KEY = "6848088859:AAH2cBlXuvkkI16fAvaoAIFL-Q-bwsy7RG0"
    bot = Bot(API_KEY)
    my_info = bot.get_me()
    print(f"Information about the bot: {my_info}")
    last_update_id = 0

    while True:
        for update in bot.get_updates(limit=50, offset = last_update_id+1):
            last_update_id = update.update_id
            if update.message and update.message.from_peer:  # we have a text message from  fellow chat.
                sender = update.message.from_peer.id  # set the sender id
                message = update.message.text
                response = get_response(MAP, message)
                bot.send_msg(sender, response)

if __name__ == "__main__":
    main()
