import unittest
from unittest.mock import patch
from parameterized import parameterized

from main import documents, directories, check_document_existance, get_doc_owner_name, get_all_doc_owners_names, \
    remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, show_document_info, show_all_docs_info, \
    get_doc_shelf, move_doc_to_shelf, add_new_doc, delete_doc

FIXTURE_check_document_existance = [
        ("2207 876234", True),
        ("2207 876234adga", False),
        ("10006", True)
    ]
FIXTURE_get_doc_shelf = [
        ("2207 876234", '1', True),
        ("2207 876234adga", "2207 876234adga", False),
        ("10006", '2', True)
    ]
FIXTURE_move_doc_to_shelf = [
        ('2207 876234', '3', 'Документ номер "2207 876234" был перемещен на полку номер "3"'),
        ('2207 876234', '1', 'Документ номер "2207 876234" был перемещен на полку номер "1"'),
        ('10006', '1', 'Документ номер "10006" был перемещен на полку номер "1"'),
        ('10006', '2', 'Документ номер "10006" был перемещен на полку номер "2"')
    ]
FIXTURE_add_new_doc = [
        ('4231235', 'insurance', 'Pupkin', '3',
             [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
              {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
              {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
              {'type': 'insurance', 'number': '4231235', 'name': 'Pupkin'}],
             {'1': ['11-2', '5455 028765', '2207 876234'], '2': ['10006'], '3': ['4231235'], '5': []}
         ),
        ('sfgbkad', 'pasport', 'Hokarasefga', '2',
             [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
              {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
              {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
              {'type': 'insurance', 'number': '4231235', 'name': 'Pupkin'},
              {'type': 'pasport', 'number': 'sfgbkad', 'name': 'Hokarasefga'}],
             {'1': ['11-2', '5455 028765', '2207 876234'], '2': ['10006', 'sfgbkad'], '3': ['4231235'], '5': []}
         )
    ]
FIXTURE_delete_doc = [
        ('4231235', True,
             [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
              {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
              {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
              {'type': 'pasport', 'number': 'sfgbkad', 'name': 'Hokarasefga'}],
             {'1': ['11-2', '5455 028765', '2207 876234'], '2': ['10006', 'sfgbkad'], '3': [], '5': []}
         ),
        ('sfgbkad', True,
             [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
              {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
              {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}],
             {'1': ['11-2', '5455 028765', '2207 876234'], '2': ['10006'], '3': [], '5': []}
         ),
        ('3412351 t wjkrgnwe', False,
             [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
              {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
              {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}],
             {'1': ['11-2', '5455 028765', '2207 876234'], '2': ['10006'], '3': [], '5': []}
         )
    ]


class TestFunctions(unittest.TestCase):

    #TODO 01. Тест функции <Проверка наличия документа в словаре по номеру документа>:
    @parameterized.expand(FIXTURE_check_document_existance)
    def test_01_check_document_existance(self, num, result):
        self.assertEqual(check_document_existance(num), result)

    #TODO 02. Тест функции <p – (people)>:
    """Рабочий вариант для 1 набора параметров"""
    @patch('builtins.input', return_value="2207 876234")
    def test_02_get_doc_owner_name(self, mock_input):
        result = get_doc_owner_name()
        self.assertEqual(result, "Василий Гупкин")

    #TODO 03. Тест функции <ap - (all people)>:
    def test_03_get_all_doc_owners_names(self):
        result = list(get_all_doc_owners_names())
        result.sort()
        self.assertEqual(result, ['Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'])

    #TODO 04. Тест функции <as – (add shelf)>:
    @patch('builtins.input', return_value='5')
    def test_04_1_add_new_shelf(self, mock_input):
        directories2 = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': [],
            '5': []
        }
        res_1_1, res_1_2 = add_new_shelf()
        self.assertEqual(res_1_1, '5')
        self.assertEqual(res_1_2, True)
        self.assertEqual(directories, directories2)

    """Попытка добавить существующую полку"""
    @patch('builtins.input', return_value='5')
    def test_04_2_add_new_shelf(self, mock_input):
        directories2 = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': [],
            '5': []
        }
        res_1_1, res_1_2 = add_new_shelf()
        self.assertEqual(res_1_1, '5')
        self.assertEqual(res_1_2, False)
        self.assertEqual(directories, directories2)

    #TODO 05. Тест функции <Добавление документа на полку directories>:
    @patch('builtins.input', return_value='5')
    def test_05_add_new_shelf(self, mock_input):
        directories2 = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': [],
            '5': ['5dga 5 5g']
        }
        self.assertEqual(append_doc_to_shelf('5dga 5 5g', '5'), directories2)

    #TODO 06.Тест функции <Удаление документа из directories>:
    def test_06_remove_doc_from_shelf(self):
        directories2 = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': [],
            '5': []
        }
        remove_doc_from_shelf('5dga 5 5g')
        self.assertEqual(directories, directories2)

    #TODO 07.Тест функции <Вывод информации о документе из documents>:
    def test_07_show_document_info(self):
        doc = {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
        self.assertEqual(show_document_info(doc), 'invoice "11-2" "Геннадий Покемонов"')

    #TODO 08.Тест функции <l – (list)>:
    def test_08_show_all_docs_info(self):
        doc_info = '''Список всех документов:
passport "2207 876234" "Василий Гупкин"
invoice "11-2" "Геннадий Покемонов"
insurance "10006" "Аристарх Павлов"'''
        self.assertEqual(show_all_docs_info(), doc_info)

    #TODO 09.Тест функции <s – (shelf)>:
    @parameterized.expand(FIXTURE_get_doc_shelf)
    def test_09_get_doc_shelf_1(self, doc_num, res1, res2):
        res1_2, res2_2 = get_doc_shelf(doc_num)
        self.assertEqual(res1_2, res1)
        self.assertEqual(res2_2, res2)

    #TODO 10.Тест функции <m – (move)>:
    @parameterized.expand(FIXTURE_move_doc_to_shelf)
    def test_10_move_doc_to_shelf(self, num_doc, num_shelf, result):
        self.assertEqual(move_doc_to_shelf(num_doc, num_shelf), result)

    # TODO 11.Тест функции <a – (add)>:
    @parameterized.expand(FIXTURE_add_new_doc)
    def test_11_add_new_doc(self, doc_num, doc_type, doc_o_name, doc_shalf_num, result1, result2):
        self.assertEqual(add_new_doc(doc_num, doc_type, doc_o_name, doc_shalf_num), doc_shalf_num)
        self.assertEqual(documents, result1)
        self.assertEqual(directories, result2)

    # TODO 12.Тест функции <d – (delete)>:
    @parameterized.expand(FIXTURE_delete_doc)
    def test_12_delete_doc(self, doc_num, deleted, result1, result2):
        return1, return2 = delete_doc(doc_num)
        self.assertEqual(return1, doc_num)
        self.assertEqual(return2, deleted)
        self.assertEqual(documents, result1)
        self.assertEqual(directories, result2)