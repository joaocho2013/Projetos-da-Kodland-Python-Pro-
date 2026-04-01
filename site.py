from flask import Flask
import random
import string

app = Flask(__name__)

ftsl = [
    "De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.",
    "A maioria das pessoas que sofre de dependência tecnológica sente um forte estresse quando fica fora da área de cobertura de rede ou não pode usar seus dispositivos",
    "A dependência tecnológica pode levar a problemas de saúde mental, como ansiedade e depressão, além de afetar negativamente as relações sociais e o desempenho acadêmico ou profissional.",
    "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna",
    "Segundo um estudo de 2019, mais de 60% das pessoas respondem a mensagens de trabalho em seus smartphones dentro de 15 minutos após sair do trabalho",
    "Uma forma de combater a dependência tecnológica é buscar atividades que tragam prazer e melhorem o humor",
    "Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, fazendo com que passemos o máximo de tempo possível consumindo conteúdo",
    "Elon Musk também defende a regulamentação das redes sociais e a proteção dos dados pessoais dos usuários. Ele afirma que as redes sociais coletam uma enorme quantidade de informações sobre nós, que podem ser usadas para manipular nossos pensamentos e comportamentos",
    "As redes sociais têm pontos positivos e negativos, e devemos estar atentos a ambos ao utilizar essas plataformas"
]

@app.route("/")
def hello_world():
    return """
    <h1>Página inicial</h1>
    <a href='/random_fact'>Veja um fato aleatório!</a><br>
    <a href='/secret'>Página secreta </a><br>
    <a href='/senha'>Gerar senha </a>
    """

@app.route("/random_fact")
def random_fact():
    fato = random.choice(ftsl)
    return f"<h1>Fato aleatório:</h1><p>{fato}</p>"

@app.route("/secret")
def secret():
    resultado = random.choice(["Cara", "Coroa"])
    return f"<h1>Resultado:</h1><p>{resultado}</p><a href='/'>Voltar</a>"

@app.route("/senha")
def gerar_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(12))
    return f"<h1>Sua senha:</h1><p>{senha}</p><a href='/'>Voltar</a>"

app.run(debug=True)
