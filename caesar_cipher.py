import client
import json
import hashlib
from caesarcipher import CaesarCipher

# Resposta da requisição da API
answer = client.data

# Metodo que cria o arquivo json
def escrever_json(lista):
    with open('answer.json', 'w') as f:
        json.dump(lista, f)

# Metodo que carrega os dados do arquivo json
def carregar_json(arquivo):
    with open('answer.json', 'r') as f:
        return json.load(f)

# Processo de decifrar mensagem
des = CaesarCipher(client.data["cifrado"] , offset=10)
decifrado = des.decoded

# Processo para criar resumo
h = hashlib.sha1()
h.update(decifrado.encode('utf-8'))
resumo = h.hexdigest()

# Atualizando as key vazias do json da requisição
editado = {
    'decifrado': decifrado,
    'resumo_criptografico': resumo
}
answer.update(editado)

# Criando ou atualizando o json
escrever_json(answer)
carregar_json(answer)


