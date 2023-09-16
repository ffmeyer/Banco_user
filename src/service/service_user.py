from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name != None or job != None:
            user = User(name, job)
            for item_user in self.store.bd:
                if item_user.name == user.name:
                    return "Nome já existe"
            self.store.bd.append(user)
            return "Usuario adicionado"
        else:
            return "Usuario Inválido"

    def remove_user(self, user):
        for item_user in self.store.bd:
            if item_user.name == user:
                item_removido = item_user
        if item_removido != None:
            self.store.bd.remove(item_removido)
            return "removendo usuario"
        else:
            return "usuario não existe"

    def lista_user(self):
        print("print lista user")
        for item_user in self.store.bd:
            print(item_user.name)
