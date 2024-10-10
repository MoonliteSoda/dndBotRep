import telebot

TOKEN = "7578329604:AAEjfLM4OW5MVqPu8k58tN7VfDrWqkeAsJQ"

lobby_reg = ['LB4410']


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])#декоратор если text
def start_message(message):
    bot.send_message(message.chat.id,'Вас приветствует DnD бот!\nЧтобы открыть меню напишите /menu')
    bot.register_next_step_handler(message,dialog1)

def dialog1(message):
    if message.text.lower() == '/menu':
        bot.send_message(message.chat.id,'/создать_лобби(/join)\n/присоединиться_к_лобби')
        bot.register_next_step_handler(message, get_join)

@bot.message_handler(commands=['join'])
def get_join(message):
    bot.send_message(message.chat.id,"Введите номер лобби")
    bot.register_next_step_handler(message, CRL)

def CRL(message):
    if message.text in lobby_reg:
        bot.send_message(message.chat.id,"Вы подключены!")
    else:
        bot.send_message(message.chat.id, "Нет такого лобби.")


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()#константа для обновления данных