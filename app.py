from flask import Flask, render_template

# Inicializa a aplicação Flask
app = Flask(__name__)

# --- Definição das Rotas (Páginas) ---

# Rota para a Página Inicial (ex: http://127.0.0.1:5000/)
@app.route('/')
def index():
    # Renderiza o arquivo 'index.html' que está na pasta 'templates'
    return render_template('index.html')

# Rota para a página "Sobre" (ex: /sobre)
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota para a página "Membros" (ex: /membros)
@app.route('/membros')
def membros():
    return render_template('membros.html')

# --- Rotas para as outras páginas do seu menu ---
# (Elas vão funcionar assim que você adicionar os .html na pasta /templates)

@app.route('/atuacao')
def atuacao():
    # Quando você criar o atuacao.html, mude a linha abaixo
    # return render_template('atuacao.html')
    return "Página 'Linhas de Atuação' em construção!", 404

@app.route('/publicacoes')
def publicacoes():
    return "Página 'Publicações' em construção!", 404

@app.route('/noticias')
def noticias():
    return "Página 'Notícias' em construção!", 404

@app.route('/contato')
def contato():
    return "Página 'Contato' em construção!", 404

# --- Roda o servidor ---
if __name__ == '__main__':
    # O debug=True faz o servidor reiniciar automaticamente
    # quando você salva uma alteração no código.
    app.run(debug=True)