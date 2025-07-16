#importa o framework Flask
from flask import Flask

#Cria a aplicação
app= Flask(__name__)

#Define uma rota para o endereço principal"/"
@app.route("/")
def home ():
    return "Bem vindo à minha  Flask!"

#Define uma rota extra chamada "/sobre"
@app.route("/sobre")
def sobre ():
    return "Essa é a minha página sobre."

#Roda o servidor local com debug ativado
if __name__ == "__main__":
    app.run (debug=True)
