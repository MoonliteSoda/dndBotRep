from random import randrange

import telebot

TOKEN = ""

lobby_reg = {'LB0000':[['test_user1'],['test_user2']]}
buffer = []


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])#декоратор если start
def start_message(message):
    bot.send_message(message.chat.id,'Вас приветствует DnD бот!\nЧтобы открыть меню напишите /menu')
    bot.register_next_step_handler(message,dialog1)


def dialog1(message):
    if message.text.lower() == '/menu':
        bot.send_message(message.chat.id,'/создать_лобби(/create)\n/присоединиться_к_лобби(/join)')
        bot.register_next_step_handler(message, get_perem)


def get_perem(message):#переписать этот позор
    if message.text == '/join':
        bot.register_next_step_handler(message,get_join)
    elif message.text == '/create':
        bot.register_next_step_handler(message,get_creater)


@bot.message_handler(commands=['join'])
def get_join(message):
    bot.send_message(message.chat.id,"Введите номер лобби")
    bot.register_next_step_handler(message, get_add)


def get_add(message):
    if message.text in lobby_reg:
        lobby_name = message.text
        user_name = message.chat.id
        if lobby_name in lobby_reg.keys():
            lobby_reg[lobby_name].append([user_name])
            bot.send_message(message.chat.id,"Вы подключены!")
            """добавить только одно возможное лобби в нейминг"""
    else:
        bot.send_message(message.chat.id, "Нет такого лобби.")


@bot.message_handler(commands=['create'])
def get_creater(message):
    cretor_name = message.chat.id
    while True:
        nomer_lob_gen = 'LB' + str(randrange(4000,5000))
        if nomer_lob_gen not in lobby_reg.keys():
            break
    lobby_reg[nomer_lob_gen] = [[cretor_name]]
    bot.send_message(message.chat.id, f"Создано лобби под номером {nomer_lob_gen}")



@bot.message_handler(commands=['exit'])
def get_exit(message):
    name = message.chat.id
    for i, j in lobby_reg.items():
        if name in j:
            j.remove(name)
    bot.send_message(message.chat.id, f"Вы вышли из всех лобби")


@bot.message_handler(commands=['help'])  # если /help
def print_comands(message):
    bot.send_message(message.chat.id, "/join - присоединиться к лобби\n"
                                      "/create - создать лобби\n"
                                      "/exit - выйти из лобби\n"
                                      "/mess - написать сообщение(для ГМ)\n"
                                      "/param - задать параметры ID\n"
                                      "/techData")


""""@bot.message_handler(commands=['param'])
def get_parametru(message):
    user_name = message.chat.id3."""






@bot.message_handler(commands=['techData'])
def info(message):
    bot.send_message(message.chat.id,f"{lobby_reg}")


@bot.message_handler(commands=['mess'])
def get_message(message):
    bot.send_message(message.chat.id, "Напишите номер лобби")
    bot.register_next_step_handler(message,get_message1)


def get_message1(message):
    lobby_name_1 = message.text
    buffer.append([lobby_name_1,message.chat.id])
    if message.text in lobby_reg.keys():
        a = lobby_reg[lobby_name_1][0]
        if a == [message.chat.id]:
            bot.send_message(message.chat.id,"Введите текст сообщения")
            bot.register_next_step_handler(message, get_message2)
        else:
            bot.send_message(message.chat.id,"У вас недостаточно прав")
    else:
        bot.send_message(message.chat.id,"Такого лобби не существует")


def get_message2(message):
    mes_gm = message.text
    for i in range(len(buffer)):
        if buffer[i][1] == message.chat.id:#проверка гм-айди
            break
    for elem in lobby_reg[buffer[i][0]]:
        bot.send_message(*elem,f"{mes_gm}")
    bot.send_message(message.chat.id,f"Ваше сообщение отправлено")
    buffer.clear()


@bot.message_handler(content_types=['text'])# по факту обязан работать во всех остальных случаях
def print_help(message):
    bot.send_message(message.chat.id, "Напишите /help для вывода списка команд")


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()#константа для обновления данных
