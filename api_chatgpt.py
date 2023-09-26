import openai
import os
import dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def ler_arquivo(arquivo):
    with open(arquivo, "r", encoding="utf-8") as file:
        return file.read()

def traduzir(texto, idioma_origem, idioma_destino):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Traduza o seguinte texto do idioma {idioma_origem} para o idioma {idioma_destino}: {texto}",
            temperature=0.7,
            max_tokens=2048,
            n=1,
            stop=None
        )
        return response['choices'][0]['text']
    except Exception as e:
        print('Erro na conexão com a API: ', e)

arquivo = 'artigo.txt'
texto = ler_arquivo(arquivo)
print(traduzir(texto, "português", "francês"))
