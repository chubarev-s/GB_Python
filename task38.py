# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных

file_path = "spravochnik.txt"
file_replace = "replacesprav.txt"
#метод(функция) вывода всего справочника
def show_all_records():
    with (open(file_path, 'r', encoding="utf-8")) as _data:
        for line in _data:
            phonebook_data = line.replace(";", " ")
            print(phonebook_data, end="")

#метод(функция) поиска контакта
def search_record(Fam):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if Fam.lower() in line.split(";")[0].lower():
                print(line, end = "")
               

#метод(функция) добавление контакта
def add_contact(new_contact_fio, new_contact_number):

    with open("spravochnik.txt", "a", encoding = "utf-8") as f:
        f.write("\n")
        f.write(new_contact_fio.replace(" ",";"))
        f.write(';')
        f.write(new_contact_number)

#метод(функция) удаление контакта
def del_fio(phone):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if phone.lower() in line.split(";")[3].lower():
                line_del = line
                print(f"Запись {line_del} - будет удалена")
            else:
                with open(file_replace, "a", encoding="utf-8") as _data: 
                    _data.write(line)
    with open(file_path, "w", encoding="utf-8") as f: 
        f.writelines("")
    with open(file_replace, "r", encoding="utf-8") as f:
        for line in f:
            with open(file_path, "a", encoding="utf-8") as _data: 
                    _data.write(line)
    with open(file_replace, "w", encoding="utf-8") as f: 
        f.writelines("")

#метод(функция) замены данных контакта:
def replace_fio(phone):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if phone.lower() in line.split(";")[3].lower():
                line_del = line
                print(f"Вы хотите изменить запись: {line_del}")
                fio = input("Введите ФИО через пробел: ")
                number = input("Введите номер: ")
                with open(file_replace, "a", encoding="utf-8") as _data:
                    #_data.write("\n")
                    _data.write(fio.replace(" ",";"))
                    _data.write(';')
                    _data.write(number)
            else:
                with open(file_replace, "a", encoding="utf-8") as _data: 
                    _data.write(line)
    with open(file_path, "w", encoding="utf-8") as f: 
        f.writelines("")
    with open(file_replace, "r", encoding="utf-8") as f:
        for line in f:
            with open(file_path, "a", encoding="utf-8") as _data: 
                    _data.write(line)
    with open(file_replace, "w", encoding="utf-8") as f: 
        f.writelines("")
        
def main():
    print("Выберите действие: 1 - Показать справочник, "
          "2 - Найти контакт, "
          "3 - Добавить контакт, "
          "4 - Изменить контакт, "
          "5 - Удалить контакт")
    
    select = int(input())
    if select == 1:
        show_all_records()
    elif select == 2:
        name = input("Введите фамилию: ")
        search_record(name)
    elif select == 3:
        fio = input("Введите ФИО через пробел: ")
        number = input("Введите номер: ")
        add_contact(fio, number)
    elif select == 4:
        name = input("Введите фамилию: ")
        print("По Ваему запросу найдены следующие люди: ")
        search_record(name)
        print("")
        num = input("Введите номер телефона абонента для изменения контакта: ")
        replace_fio(num)
    elif select == 5:
        name = input("Введите фамилию: ")
        print("По Ваему запросу найдены следующие люди: ")
        search_record(name)
        print("")
        num = input("Введите номер телефона абонента для удаления: ")
        del_fio(num)

main()


