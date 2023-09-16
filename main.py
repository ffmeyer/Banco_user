from src.service.service_user import ServiceUser

service = ServiceUser()
resposta = service.add_user("jonathan", "advogado")
print(resposta)

resposta2 = service.add_user("zacarias", "advogado")
print(resposta2)

validar = service.add_user("zacarias", "advogado")
print(validar)

service.remove_user("jonathan")
service.lista_user()