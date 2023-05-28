def imp (data_list):
    with open ("Data_tl.txt", "a", encoding="utf-8") as file:
        for el in data_list:
            file.write(el+" ")

def exp (arg):
    with open ("Data_tl.txt", "r", encoding="utf-8") as file:
        file_text = file.read().split("\n\n")          
        for i in file_text:
            string_text = i.split(" ") 
            for k in string_text:
                if arg == k:
                    print (*string_text)
        
def all_import ():
    with open ("Data_tl.txt", "r", encoding="utf-8") as file:
        file_text = file.read()
        print (file_text)

def interface ():
    bot = input ("Введите 1 - для импорта данных, 2 - для поиска данных, 3 - для вывода базы данных: ")
    if bot == "1":
        surname = input ("Введите фамилию: ")
        name = input ("Введите имя: ")
        patronymic = input ("Введите отчество: ")
        data = input ("Введите год рождения: ")
        number = input ("Введите номер телефона: ")
        data_list = ["\n\n"] + [surname, name, patronymic, data, number]
        imp (data_list)
    elif bot=="2":
        find = input ("Введите контактную информацию (Фамилию, имя, отчество, год рождения или номер телефона): ")
        exp (find)
    elif bot=="3":
        all_import ()
    else :
        print ("неккоректный ввод")
interface ()