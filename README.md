# Conexão com a API do Chat GPT
# Pré requisitos
Python 3

## Como usar
1. Acesse o site da [OpenIA](https://openai.com/), crie uma conta e obtenha sua chave
2. Clone o projeto ou crie o seu com os métodos para chamada da API
3. Crie um ambiente virtual e entre nele com: `virtualenv .venv` e `source .venv/bin/activate`
4. Instale a biblioteca da OpenAI com o comando: `pip install openai python-dotenv`
5. Crie um arquivo com o nome .env e adicione sua chave da seguinte forma:
`OPENAI_API_KEY=sk-JlJHhfuutjjMmnbfjkkNbjkIIppYYhnrjkjJUUnnJUYHnf`
6. Altere o prompt conforme a necessidade, neste caso o objetivo é traduzir textos, mas as possibilidades são muitas
7. Crie um arquivo com o nome artigo.txt ou outro conforme sua necessidade (lembre-se de alterar o nome no código)
8. Execute com o comando: `python api_chatgpt.py`
