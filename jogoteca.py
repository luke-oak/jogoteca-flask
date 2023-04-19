from flask import Flask, render_template, request, redirect

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Console: {self.console}'

jogos = [
        Jogo('NBA 2K22', 'Esportes', 'PS5'), 
        Jogo('Overwatch 2', 'FPS', 'PC'), 
        Jogo('League of Legends', 'Moba', 'PC')
        ] 

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('lista.html', titulo='Jogos', jogos=jogos)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['senha'] == '1234':
        return redirect('/')
    else:
        return redirect('/login')


app.run(debug=True)

