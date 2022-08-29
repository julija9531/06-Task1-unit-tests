documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


#TODO 01. Проверка наличия документа в словаре по номеру документа
def check_document_existance(user_doc_number):
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded

#TODO 02. p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
def get_doc_owner_name():
    user_doc_number = input('Введите номер документа - ')
    print()
    if check_document_existance(user_doc_number):
        for current_document in documents:
            if current_document['number'] == user_doc_number:
                return current_document['name']

#TODO 03. ap - (all people) - команда, которая выводит список всех владельцев документов
def get_all_doc_owners_names():
    users_list = []
    for current_document in documents:
        try:
            doc_owner_name = current_document['name']
            users_list.append(doc_owner_name)
        except KeyError:
            pass
    return set(users_list)

#TODO 04. as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень
def add_new_shelf(shelf_number=''):
    if not shelf_number:
        shelf_number = input('Введите номер полки - ')
    if shelf_number not in directories.keys():
        directories[shelf_number] = []
        return shelf_number, True
    return shelf_number, False

#TODO 05. Добавление документа на полку directories
def append_doc_to_shelf(doc_number, shelf_number):
    add_new_shelf(shelf_number)
    directories[shelf_number].append(doc_number)
    return directories

#TODO 06. Удаление документа из полки directories
def remove_doc_from_shelf(doc_number):
    for directory_number, directory_docs_list in directories.items():
        if doc_number in directory_docs_list:
            directory_docs_list.remove(doc_number)
            break

#TODO 07. Вывод информации о документе из documents
def show_document_info(document):
    doc_type = document['type']
    doc_number = document['number']
    doc_owner_name = document['name']
    return ('{} "{}" "{}"'.format(doc_type, doc_number, doc_owner_name))

#TODO 08. l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
def show_all_docs_info():
    docs_info = 'Список всех документов:'
    for current_document in documents:
        docs_info += '\n' + show_document_info(current_document)
    return docs_info

#TODO 09. s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится
def get_doc_shelf(user_doc_number):
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for directory_number, directory_docs_list in directories.items():
            if user_doc_number in directory_docs_list:
                return directory_number, doc_exist
    else: return user_doc_number, doc_exist

#TODO 10. m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую
def move_doc_to_shelf(num_doc, num_shelf):
    remove_doc_from_shelf(num_doc)
    append_doc_to_shelf(num_doc, num_shelf)
    return 'Документ номер "{}" был перемещен на полку номер "{}"'.format(num_doc, num_shelf)

#TODO 11. a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер,
# тип, имя владельца и номер полки, на котором он будет храниться
def add_new_doc(doc_num, doc_type, doc_o_name, doc_shalf_num):
    new_doc = {
        "type": doc_type,
        "number": doc_num,
        "name": doc_o_name
    }
    documents.append(new_doc)
    append_doc_to_shelf(doc_num, doc_shalf_num)
    print(directories)
    return doc_shalf_num

#TODO 12. d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок
def delete_doc(user_doc_number):
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                documents.remove(current_document)
                remove_doc_from_shelf(doc_number)
                return doc_number, True
    else: return user_doc_number, False



#TODO 00. Запуск цикла
def secretary_program_start():
    """
    ap - (all people) - команда, которая выводит список всех владельцев документов
    p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
    имя владельца и номер полки, на котором он будет храниться;
    d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
    q - (quit) - команда, которая завершает выполнение программы.
    """
    print(
        'Вас приветствует программа помошник!\n',
        '(Введите help, для просмотра списка поддерживаемых команд)\n'
    )
    while True:
        user_command = input('Введите команду - ').lower()
        if user_command == 'p':
            owner_name = get_doc_owner_name()
            print('Владелец документа - {}'.format(owner_name))
        elif user_command == 'ap':
            uniq_users = get_all_doc_owners_names()
            print('Список владельцев документов - {}'.format(uniq_users))
        elif user_command == 'l':
            docs_info = show_all_docs_info()
            print(docs_info)
        elif user_command == 's':
            user_doc_number = input('Введите номер документа - ')
            directory_number, doc_exist = get_doc_shelf(user_doc_number)
            if doc_exist:
                print('Документ находится на полке номер {}'.format(directory_number))
            else: print('Документ номер {} отсутствует в базе'.format(directory_number))
        elif user_command == 'a':
            print('Добавление нового документа:')
            new_doc_number = input('Введите номер документа - ')
            new_doc_type = input('Введите тип документа - ')
            new_doc_owner_name = input('Введите имя владельца документа- ')
            new_doc_shelf_number = input('Введите номер полки для хранения - ')
            new_doc_shelf_number = add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number)
            print('\nНа полку "{}" добавлен новый документ:'.format(new_doc_shelf_number))
        elif user_command == 'd':
            user_doc_number = input('Введите номер документа - ')
            doc_number, deleted = delete_doc(user_doc_number)
            if deleted:
                print('Документ с номером "{}" был успешно удален'.format(doc_number))
            else: print('Документ номер {} отсутствует в базе'.format(doc_number))
        elif user_command == 'm':
            user_doc_number = input('Введите номер документа - ')
            user_shelf_number = input('Введите номер полки для перемещения - ')
            print(move_doc_to_shelf(user_doc_number, user_shelf_number))
        elif user_command == 'as':
            shelf_number, added = add_new_shelf()
            if added:
                print('Добавлена полка "{}"'.format(shelf_number))
            else: print('Полка "{}" уже существует'.format(shelf_number))
        elif user_command == 'help':
            print(secretary_program_start.__doc__)
        elif user_command == 'q':
            break
        else:
            print('Введенная команда не поддерживается.\nВведите help, для просмотра списка поддерживаемых команд)\n')


if __name__ == '__main__':
    secretary_program_start()
