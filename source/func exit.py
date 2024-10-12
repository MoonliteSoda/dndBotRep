

"""lobby_reg = {'LBDEF':['user11','user12','user22'],'LB4410':['user21','user22']}
name = 'user22'
for i,j in lobby_reg.items():
    if name in j:
        j.remove(name)
GM = 'user11'
lob = "LBDEF"
if lob in lobby_reg.keys():
    if lobby_reg[lob][0] == GM:
        print('Вы можете отправить сообщение')

    else:
        print("У вас недостаточно прав")"""

#lobby_reg = {'LBDEF':[["user11"],['user12'],['user13']],'LB4410':[]}

lobby_reg = {'LBDEF':[['111111'],['111']],'LB4410':[['2222222'],['222'],['12345']]}
n = [['LB4410','111111'],['LB4420','2222222']]
id = n[1][1]
'''for i in range(len(n)):
    if n[i][1] == id:  # проверка гм-айди
        break
    for elem in lobby_reg[n[i][0]]:'''

print(*lobby_reg['LBDEF'][0])




