import json
from pprint import pprint

def pb_menu(d):              #у параметр передаємо наш зчитаний файл json, присвоєний змінній contacts_dict у вигляді dict
    print("\n*** Hello, welcome to phonebook! ***")
    while True:
        print("""\nHere is what you can do:
        1. Add a new contact.
        2. Search the contact.
        3. Exit phonebook. 
        """)

        try:
            menu_select = int(input("Please press number from 1 to 3 to navigate within your phonebook:  "))
            if menu_select == 1:
                add(d)
            elif menu_select == 2:
                search(d)
            elif menu_select == 3:    # після збереження розриваємо цикл while і програма закривається
                save_file(d)
                break
            else:                    #якщо було введено букву, або будь-яку цифру окрім 1-3. Викликаємо Exception і повертаємося в головне меню для вибору правильної цифри
                raise Exception
        except:
            print("\n* ERROR. Incorrect value, try again. * \n")



def add(d):
    while True:
        try:
            number = input("\nEnter phone number in format '+хххххххххххх': \n")
            if number in d:      # якщо введений номер вже існує в тел.книзі --> виводимо його на екран і пропонуємо його змінити/видалити
                print("\nNumber already exist in phonebook. See below. \n")
                pprint(d[number])
                print("""\nPlease select what do you want to do with this contact?
                1. Change contact details.
                2. Delete contact.
                3. Exit to main menu.
                """)
                while True:
                    try:
                        selection = int(input("Type number from to 3 from above options: "))
                        if selection == 1:
                            change(d, number)
                        elif selection == 2:
                            delete(d, number)
                        elif selection == 3:
                            return
                        else:                          #перевірка на правильність вводу
                            raise Exception
                        break
                    except:
                        print("\nChoose only numbers from given options")


            elif len(number) == 13 and number[0] == "+" and number[1:].isdigit():   #номер має відповідати правильному формату "+хххххххххххх"
                d[number] = {}                             #до кожного ключа (=номер телефону) в головному словнику - створюємо новий словник з деталями контакту
                d[number]["name"] = input("Type name: ")   #створюємо ключі і присвоюємо їм значення здобуті від користувача
                d[number]["last_name"] = input("Type last name: ")
                d[number]["full_name"] = d[number]["name"] + " " + d[number]["last_name"]  #full name складається з імені та прізвища
                d[number]["phone_number"] = number         #тел.номер у маленькому словнику і так дорівнює введеному раніше номеру (який до того ж є ключем)
                d[number]["city"] = input("Type city: ")

            else:                    #перевірка на правильність вводу
                raise Exception
            break
        except:
            print("*ERROR. Please enter valid number, which contains only digits in format '+хххххххххххх'. *")

def search(d):
    while True:
        try:
            print("""\nPlease select the search option:
            1. By first name.
            2. By last name.
            3. By full name.
            4. By number.
            5. By city.
            """)
            search_option = int(input("Please select the search option:"))
            if search_option == 1:
                search_by_option(d, "name")
            elif search_option == 2:
                search_by_option(d, "last_name")
            elif search_option == 3:
                search_by_option(d, "full_name")
            elif search_option == 4:
                search_by_option(d, "number")
            elif search_option == 5:
                search_by_option(d, "city")
            else:
                raise Exception        #перевірка на правильність вводу
            break
        except:
            print("\n* ERROR. Please select only number from above. *")


def change(d, number):
    while True:
        print("""\nWhat do you want to change in the contact? 
        1. First name.
        2. Last name.
        3. Number.
        4. City
        5. Exit to main menu""")
        try:
            change_option = int(input("\nChoose option from 1 to 5:  "))
            if change_option == 1:
                new_name = input("Type new name: ")
                d[number]["name"] = new_name                     #переприсвоюємо нові значення по ключу
                d[number]["full_name"] = new_name + " " + d[number]["last_name"]
            elif change_option == 2:
                new_last_name = input("Type new last name: ")
                d[number]["last_name"] = new_last_name
                d[number]["full_name"] = d[number]["name"] + " " + new_last_name
            elif change_option == 3:
                while True:
                    try:
                        new_number = input("\nType new number: ")
                        if new_number in d:
                            raise KeyError
                        elif len(new_number) != 13 or new_number[0] != "+" or not new_number[1:].isdigit():
                            raise TypeError
                        break       #якщо номер ще не існує і введений у правильному форматі - розриваємо цикл і йдемо нижче перезаписувати контакт
                    except KeyError:
                        print("\n* Number already exist in phonebook. *")
                    except TypeError:
                        print("\n* ERROR. Number format is incorrect. Try again. *")
                d[number]["phone_number"] = new_number   #спочатку присвоюємо новий номер по ключу в маленькому словнику
                d[new_number] = d[number]   #створюємо у великому словнику новий ключ (=новий номер) і присвоюємо йому усі values(тобто маленький словник) зі старого ключа
                d.pop(number)               #вилучаємо старий ключ з його values
            elif change_option == 4:
                new_city = input("Type new city: ")
                d[number]["city"] = new_city
            elif change_option == 5:     #розриваємо цикл і повертаємося у головне меню
                break
            else:
                raise Exception
        except:
            print("\n* ERROR. Wrong option, choose correct one from above only. *")

def delete(d, number):
    while True:
        print("""\nAre you sure you want to delete this contact?
         1. Type "y" if you want to delete.
         2. Type "n" if you want to return back to main menu """)
        try:
            delete_check = input("\nYour answer here: ")
            if delete_check == "y":
                d.pop(number)
            elif delete_check == "n":
                pass
            else:                  # перевірка якщо було введено щось окрім 'y' чи 'n'. Якщо ні - йдемо в except --> у блок while True/try для нової спроби вводу
                raise Exception
            break
        except:
            print("\n* ERROR. Try again. Use only 'y' or 'n'. *")


def save_file(d):
    with open("contacts.json", "w") as file:
        json.dump(d, file)             #перезаписуємо json зі змінами

def open_file():
    with open("contacts.json", "r") as file:       #зчитуємо файл і повертаємо його для подальшої роботи. переприсвоюємо його у змінну contacts_dict у функції main()
        return json.load(file)

def search_by_option(d, option):
    occurances = []         #створимо пустий список і зберемо всі можливі результати пошуку (якщо, наприклад, контактів за іменем "Анна" більше ніж 1)
    search_value = input("\nType search value here: ")
    for key in d:            # key == номер телефону з d
        if search_value == d[key][option]:              #якщо введене значення знайдено в словнику
            out_tuple = (d[key]["full_name"], key)      #зберемо в tuple повне ім'я контакту та його номер
            occurances.append(out_tuple)                #додамо tuple до нашого пустого списку
    if len(occurances) == 0:
        print("\n* No contact found *")
        return
    number = ''
    if len(occurances) == 1:
        print(occurances)                #виведемо на екран контакт (повне ім'я контакту та його номер)
        number = occurances[0][1]        #присвоємо номер телефону з tuple в нову змінну number (для подальшої роботи у циклі while: для зміни/видалення знайденого контакту, адже знайдений номер є також ключем головного словника d)
    elif len(occurances) > 1:
        print("\nThere are few contacts matching your inquiry.\n")
        while True:
            pprint(occurances)     #виведемо на екран усі знайдені контакти за введеним значенням пошуку
            try:
                exact_number = input("\nType exact number you want to review: ")
                for item in occurances:
                    if exact_number in item:     #якщо введений номер є одним із знайдених раніше варіантів
                        number = exact_number    #присвоємо номер телефону з tuple в нову змінну number (для подальшої роботи у циклі while)
                        break
                else:
                    raise Exception   #якщо було введено номер не з екрану, або взагалі що інше
                break
            except:
                print("\n* ERROR. Try again, number not correct. *")
    while True:
        try:                                                     # працюємо зі знайденим контактом
            print("""\nSelect what you want to do with the number:"
                  1. Show full contact with details.
                  2. Change contact.
                  3. Delete contact.
                  4. Exit to main menu.""")
            contact_op = int(input("\nType here number from 1 to 4: "))
            if contact_op == 1:
                pprint(d[number])     #виводимо на екран деталі контакту по ключу (наш маленький словник)
            elif contact_op == 2:
                change(d, number)     #викликаємо функцію і передаємо в неї головний словник та ключ (присвоєний раніше змінній number, тобто наш контакт який ми знайшли раніше)
            elif contact_op == 3:
                delete(d, number)
            elif contact_op == 4:
                break
            else:
                raise Exception       #перевірка на правильність вводу
        except:
            print("\n* ERROR. Type correct option number. *")



def main():
    contacts_dict = open_file()
    pb_menu(contacts_dict)   #передаємо аргументом наш головний словник з відкритого json файлу


if __name__ == "__main__":
    main()