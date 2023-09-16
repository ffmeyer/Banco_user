import unittest
from src.service.service_user import ServiceUser


class TestServiceUser(unittest.TestCase):

    def test_user_invalid(self):
        service = ServiceUser()
        resposta = service.add_user(None, None)
        user_invalid = 'Usuario invalido'
        self.assertEqual(resposta, user_invalid)

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
