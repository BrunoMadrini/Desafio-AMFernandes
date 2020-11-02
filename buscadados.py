import requests

class buscardados():
    @classmethod
    def buscar(cls):
        url = 'https://api.estagio.amfernandes.com.br/imoveis'
        resposta = requests.get(url)
        r = resposta.content
        r = r.decode('utf-8')
        #print(r)
        return r