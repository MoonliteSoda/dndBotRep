from random import randrange

import telebot

TOKEN = ""

lobby_reg = {'LBDEF':[],'LB4410':[]} #Количесво лобби lbdef = lobbydefolt
nickname_base = {}


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start']) #декоратор если start
def start_message(message):
    bot.send_message(message.chat.id,'Вас приветствует DnD бот!\nЧтобы открыть меню, напишите /menu \nЧтобы создать свой профиль, напишите /ID')
    bot.register_next_step_handler(message,dialog1)


def dialog1(message):
    if message.text.lower() == '/menu':
        bot.send_message(message.chat.id,'/создать_лобби(/create)\n/присоединиться_к_лобби(/join)')
        bot.register_next_step_handler(message, get_perem, get_ID)

@bot.message_handler(commands=['ID'])
def get_ID(message):
    bot.send_message(message.chat.id, "Введите имя")
    bor.register_next_step_handler(message, get_create_name)

def get_create_name(message):
    user_id = message.chat.id
    user_nick_name = message.text
    nickname_base[user_id] = user_nick_name
    bot.send_message(message.chat.id, f"Имя создано: {user_nick_name}")


def get_perem(message): #переписать этот позор
    if message.text == '/join':
        bot.register_next_step_handler(message,get_join)
    elif message.text == '/create':
        bot.register_next_step_handler(message,get_creater)



@bot.message_handler(commands=['join']) #декоратор функции
def get_join(message): #создание лобби
    bot.send_message(message.chat.id,"Введите номер лобби")
    bot.register_next_step_handler(message, get_add)


def get_add(message): #подключение в лобби
    if message.text in lobby_reg:
        lobby_name = message.text
        user_name = message.chat.id
        if lobby_name in lobby_reg.keys():
            if user_name not in lobby_reg[lobby_name]:
                lobby_reg[lobby_name].append(user_name)
                bot.send_message(message.chat.id,f"Вы подключены к лобби: {lobby_name} ")
            elif user_name in lobby_reg[lobby_name]:
                bot.send_message(message.chat.id, "Вы УЖЕ подключенны к этому лобби!")
    else:
        bot.send_message(message.chat.id, "Нет такого лобби.")


@bot.message_handler(commands=['create'])
def get_creater(message):
    cretor_name = message.chat.id
    nomer_lob_gen = 'LBDEF'
    while nomer_lob_gen in lobby_reg.keys():
        nomer_lob_gen = 'LB' + str(randrange(4000,5000))
        if nomer_lob_gen not in lobby_reg.keys():
            break
    lobby_reg[nomer_lob_gen] = [cretor_name]
    bot.send_message(message.chat.id, f"Создано лобби под именем: {nomer_lob_gen}")



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
                                      "/techInfo")

@bot.message_handler(commands=['techInfo'])
def info(message):
    bot.send_message(message.chat.id,f"{lobby_reg}", f"{nickname_base}")


@bot.message_handler(commands=['mess'])
def get_message(message):
    bot.send_message(message.chat.id, "Напишите номер лобби")
    bot.register_next_step_handler(message,get_message1)


def get_message1(message):
    if message.text in lobby_reg.keys():
        if lobby_reg[message.text][0] == message.chat.id:
            bot.send_message(message.chat.id,"Введите текст сообщения")
            #bot.register_next_step_handler(message, get_message2)
        else:
            bot.send_message(message.chat.id,"У вас недостаточно прав")
    else:
        bot.send_message(message.chat.id,"Такого лобби не существует")

"""def get_message2(message):
    mes_gm = message.text
    for lc_id in lobby_reg[lob]"""
    
        


@bot.message_handler(content_types=['text'])# по факту обязан работать во всех остальных случаях
def print_help(message):
    bot.send_message(message.chat.id, "Напишите /help для вывода списка команд")




if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()#константа для обновления данных





