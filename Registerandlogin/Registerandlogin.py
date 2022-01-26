from random import *
from module1 import *

log_user=[]
pas_user=[]


menu=''
user=''
new_user=''
login=''
pas=''
new_pas=''
str0=".,:;!_*-+()/#¤%&"
str1 = '0123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()


while menu not in ["Да","Нет","да","нет"]:
    log_user=faillist_read('Login.txt',log_user)
    pas_user=faillist_read('password.txt',pas_user)
    menu=input("Войти в аккаунт?: ")
    print()
    if menu=="Да" or menu=="да":
        autorize(pas_user,log_user)
    if menu=="Нет" or "нет":
        login=input("Создайте логин(не больше 10 символов): ")
        if len(login)>10:
            print("Логин длинный! Попробуйте ещё раз!")
        elif isUserUnic(log_user,login)==False:
            print("Пользователь существует. Придумайте новый логин")
        else:
            print("Ваш логин -", login)
            print()
        while new_pas not in ["да","Да","нет","Нет"]:
            new_pas=input("Вы хотите сгенерировать пароль или придумать сами?(Да/Нет): ")
        if new_pas in ['да','Да']:
            str4 = str0+str1+str2+str3
            ls = list(str4)
            random.shuffle(ls)
            new_pas = ''.join([random.choice(ls) for x in range(10)])
            print("Ваш пароль -", new_pas)
            autorize()
        else:
            new_pas=input("Придумайте пароль(не менее 9 символов): ")
            if len(new_pas)<9:
                print("Пароль короткий! Попробуйте еще раз!")
            else:
                print("Ваш пароль -", new_pas)
                print()
                new_pas=''
                while new_pas not in ['Нет','нет','да','Да']:
                    new_pas=input("Ваш аккаунт создан! Хотите войти в него?(Да/Нет): ")
                if new_pas in ['Да','да']:
                    autorize(pas_user,log_user)
                else:
                    break