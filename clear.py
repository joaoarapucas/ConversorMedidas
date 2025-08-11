import os
# função não muito importante,
# implementei pra testar a interação com o terminal pq estava curioso !!!
def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else: 
        _ = os.system("clear")
