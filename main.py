from tratamento import Cidades

print("Bem Vindo!")
print("Selecione a cidade desejada:")
print("[1] Santo André")
print("[2] São Bernardo do Campo")
print("[3] São Caetano do Sul")
print("Ou aperte qualquer botão para buscar todas")
valor = input("Opção:")

if valor == "1":
    Cidades.santoandre()
elif valor == "2":
    Cidades.saobernardo()
elif valor == "3":
    Cidades.saocaetano()
else:
    Cidades.santoandre()
    Cidades.saobernardo()
    Cidades.saocaetano()
