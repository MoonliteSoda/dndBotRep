

lobby_reg = {'LBDEF':['user11','user12','user22'],'LB4410':['user21','user22']}
name = 'user22'
"""for i,j in lobby_reg.items():
    if name in j:
        j.remove(name)"""
GM = 'user11'
lob = "LBDEF"
if lob in lobby_reg.keys():
    if lobby_reg[lob][0] == GM:
        print('Вы можете отправить сообщение')

    else:
        print("У вас недостаточно прав")
