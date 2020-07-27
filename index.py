from wxpy import *

bot = Bot(console_qr=True)
all_friends = bot.friends()
# test_bot_group = bot.groups().search('TEST')[0]
# apikey for Tuling chat bot
tuling = Tuling(api_key='d153338263de483ab54c1916c36a8b6d') 


@bot.register(all_friends)

# def reply_all(msg):
    # tuling.do_reply(msg)

def reply_test_group(msg):
    # print('test')
    tuling.do_reply(msg)

embed()
