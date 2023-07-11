from pyrogram import Client, filters
import setting
bot = Client(setting.name,
        api_id=setting.api_id,
        api_hash= setting.api_hash,
        bot_token = setting.bot_token
)

@bot.on_message(filters.command('start')& filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, "hi this is ferst command!")

@bot.on_message(filters.command('help'))
def command1(bot, message):
    message.reply_text("سلام لاشی، فعلا باهام هیچ گوهی نمیتونید بخورید :))")

# @bot.on_message(filters.text & filters.private)
# def echo(Client, message):
#     message.reply_text("فعلا کاری بلد نیستم بکنم، منم بازی فقط :))")


# welcombot
GROUP = 'gang_so_gang'
WELCOME_MESSAGE = 'خوش اومدی دیوث، چرا اومدی اینجا حالا؟'

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcome(client, message):
    message.reply_text(WELCOME_MESSAGE)


#send photo
@bot.on_message(filters.command('photo'))
def photo(bot, message):
    bot.send_photo(message.chat.id, "https://digimovie.red/wp-content/uploads/2022/11/o8J1HvqO6QF1hMTY0eQq7itnUn4.jpg")

@bot.on_message(filters.audio & filters.private)
def audio(bot, message):
    message.reply(f'the id audio: {message.audio.file_id}')

@bot.on_message(filters.command('audio'))
def send_audio(bot, message):
    bot.send_audio(message.chat.id, "CQACAgIAAxkBAAMoZKu5xESW447Z_J80ao9gBDFwRaIAAuklAAL27ahI2MnZXFsem9IeBA")

# delete message
@bot.on_message(filters.text)
def delete_text(bot, message):
    word_list = ["wtf", "fuck"]
    if message.text in word_list:
        bot.delete_messages(message.chat.id, message.id,  "اینجا از این حرفا نمیتونی بزنیاا ...")
        # bot.send_message(message.chat.id, "اینجا از این حرفا نمیتونی بزنیاا ...")
    else:
        message.reply("نمیفهمم چی میگی ...")



print('I AM ALIVE')
bot.run()