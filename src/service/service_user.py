from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                user_bd = self.find_user(name)
                if user_bd is None:
                    user = User(name=name, job=job)
                    self.store.bd.append(user)
                    return "Usuario adicionado"
                else:
                    return 'Usuario ja existe'
            else:
                return "Usuario invalido"
        else:
            return "Usuario invalido"

    def remove_user(self, name, job):
        if name != None and job != None:
            if isinstance(name, str) and isinstance(job, str):
                user_bd = self.find_user(name)
                if user_bd != None:
                    self.store.bd.remove(user_bd)
                    return "Usuario removido"
                else:
                    return 'Usuario não existe'
            else:
                return "Usuario invalidd"
        else:
            return "Usuario invalidd"

    def find_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    def update_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                user_bd = self.find_user(name)
                if user_bd != None:
                    for index, item_user in enumerate(self.store.bd):
                        updated_user = User(item_user.name, job)
                        self.store.bd[index] = updated_user
                        return 'Usuario atualizado'

                else:
                    return 'Usuario não encontrado'

    def get_user_by_name(self, name):
        if name is not None:
            if isinstance(name, str):
                user_bd = self.find_user(name)
                for index, item_user in enumerate(self.store.bd):
                    return self.store.bd[index]
                else:
                    return 'Usuario não encontrado'

    def list_all_users(self):
        return self.store.bd
