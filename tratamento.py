import json
from buscadados import buscardados

abc = buscardados.buscar()
abc = json.loads(abc)

class Cidades:
    @classmethod
    def santoandre(cls):
        for i in abc:
            if i['cidade'] == 'Santo André':
                print("______________________________________________________________________________________________")
                print("### SANTO ANDRÉ ###")
                print("Endereço: " + i['rua'] + ", " + i['num'], "| " + "Bairro: " + i['bairro'], "| " + "Nome do Condomínio: " + i['nome'])
                try:
                    edf = i['planta']
                    valor = str(edf['preco'])
                    metragem = str(edf['metragem'])
                    dorms = str(edf['dorms'])
                    vagas = str(edf['vagas'])
                    print("Metragem (m²): " + metragem, "| Preço (R$): " + valor, "| Dormitórios: " + dorms, "| Vagas: " + vagas)
                except:
                    print("Informação não disponível")
                print("Foto da fachada: " + i['fachada'])
            else:
                pass

    @classmethod
    def saobernardo(cls):
        for i in abc:
            if i['cidade'] == 'São Bernardo do Campo':
                print("______________________________________________________________________________________________")
                print("### SÃO BERNARDO DO CAMPO ###")
                print("Endereço: " + i['rua'] + ", " + i['num'], "| " + "Bairro: " + i['bairro'], "| " + "Nome do Condomínio: " + i['nome'])
                try:
                    edf = i['planta']
                    valor = str(edf['preco'])
                    metragem = str(edf['metragem'])
                    dorms = str(edf['dorms'])
                    vagas = str(edf['vagas'])
                    print("Metragem (m²): " + metragem, "| Preço (R$): " + valor, "| Dormitórios: " + dorms, "| Vagas: " + vagas)
                except:
                    print("Informação não disponível")
                print("Foto fachada: " + i['fachada'])
            else:
                pass

    @classmethod
    def saocaetano(cls):
        for i in abc:
            if i['cidade'] == 'São Caetano do Sul':
                print("______________________________________________________________________________________________")
                print("### SÃO CAETANO DO SUL ###")
                print("Endereço: " + i['rua'] + ", " + i['num'], "| " + "Bairro: " + i['bairro'], "| " + "Nome do Condomínio: " + i['nome'])
                try:
                    edf = i['planta']
                    valor = str(edf['preco'])
                    metragem = str(edf['metragem'])
                    dorms = str(edf['dorms'])
                    vagas = str(edf['vagas'])
                    print("Metragem (m²): " + metragem, "| Preço (R$): " + valor, "| Dormitórios: " + dorms, "| Vagas: " + vagas)
                except:
                    print("Informação não disponível")
                print("Foto fachada: " + i['fachada'])
            else:
                pass