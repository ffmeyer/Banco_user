import unittest

from parameterized import parameterized
from unittest.mock import patch

from src.service.service_user import ServiceUser

# os testes pametrizados só executam em uma classe deles, entao separei dos demais
class TestParametherized_tests(unittest.TestCase):
    @parameterized.expand([
        (None, None, 'Usuario invalido'),
        (None, 'qa', 'Usuario invalido'),
        ('zezinho', None, 'Usuario invalido'),
        (1, 'qa', 'Usuario invalido'),
        ('zezinho', -1, 'Usuario invalido'),
        (-1.1, 'qa', 'Usuario invalido'),
        ('zezinho', 1.1, 'Usuario invalido'),
        ({}, 'qa', 'Usuario invalido'),
        ('zezinho', {}, 'Usuario invalido'),
        (True, 'qa', 'Usuario invalido'),
        ('zezinho', False, 'Usuario invalido')
    ])
    def test_invalid_input_parametherized(self, name, job, expected_result):
        service = ServiceUser()
        resposta = service.add_user(name, job)
        # user_invalid = 'Usuario invalido'
        self.assertEqual(resposta, expected_result)


class TestServiceUser(unittest.TestCase):
    def test_add_user(self):
        service = ServiceUser()
        resposta = service.add_user('Fabricio', 'Eng')
        user_add = 'Usuario adicionado'
        self.assertEqual(resposta, user_add)

    def test_user_already_exists(self):
        service = ServiceUser()
        service.add_user('Fabricio', 'Eng')
        response = service.add_user('Fabricio', 'Eng')
        user_already_exists = 'Usuario ja existe'
        self.assertEqual(response, user_already_exists)

    def test_not_found_user_to_remove(self):
        service = ServiceUser()
        service.add_user('zezinho', 'qa')
        response = service.remove_user('huginho', 'qa')
        user_not_found_remove = 'Usuario não existe'
        self.assertEqual(response, user_not_found_remove)

    def test_remover_user(self):
        service = ServiceUser()
        service.add_user('luizinho', 'qa')
        service.add_user('zezinho', 'qa')
        response = service.remove_user('luizinho', 'qa')
        user_deleted = 'Usuario removido'
        self.assertEqual(response, user_deleted)

    def test_update_user(self):
        service = ServiceUser()
        service.add_user('huguinho', 'qa')
        resposta = service.update_user('huguinho', 'dev')
        user_updated = 'Usuario atualizado'
        self.assertEqual(resposta, user_updated)
        user = service.find_user('huguinho')
        self.assertEqual(user.name, 'huguinho')
        self.assertEqual(user.job, 'dev')

    def test_update_user_not_found(self):
        service = ServiceUser()
        service.add_user('huguinho', 'qa')
        resposta = service.update_user('patinhas', 'dev')
        user_not_found = 'Usuario não encontrado'
        self.assertEqual(resposta, user_not_found)

    def test_get_user_by_name(self):
        service = ServiceUser()
        service.add_user('huguinho', 'qa')
        service.add_user('zezinho', 'qa')
        service.add_user('luizinho', 'qa')
        user = service.get_user_by_name('zezinho')
        self.assertEqual(user.name, 'huguinho')
        self.assertEqual(user.job, 'qa')

    def test_list_user(self):
        service = ServiceUser()
        service.add_user('huguinho', 'qa')
        service.add_user('zezinho', 'qa')
        service.add_user('luizinho', 'qa')
        service.remove_user('zezinho', 'qa')
        response = service.list_all_users()
        qtd_itens_list = 2
        assert len(response) == qtd_itens_list

