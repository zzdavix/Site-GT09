from flask import Blueprint, render_template

# 1. Criamos um Blueprint. 
# O primeiro argumento ('main') é o nome do Blueprint.
# O segundo (__name__) diz ao Flask onde ele está localizado.
main_bp = Blueprint('main', __name__,
                    template_folder='templates', 
                    static_folder='static')

# 2. Mudamos todas as @app.route para @main_bp.route
# E mudamos o nome da função 'index' para 'index_route' 
# (para evitar conflito de nomes, é uma boa prática)

@main_bp.route('/')
def index_route():
    # Passamos a variável 'active_page' com o nome da função
    return render_template('index.html', active_page='index_route')

@main_bp.route('/sobre')
def sobre_route():
    return render_template('sobre.html', active_page='sobre_route')

@main_bp.route('/membros')
def membros_route():
    return render_template('membros.html', active_page='membros_route')

@main_bp.route('/atuacao')
def atuacao_route():
    # return render_template('atuacao.html', active_page='atuacao_route')
    return "Página 'Linhas de Atuação' em construção!", 404

@main_bp.route('/publicacoes')
def publicacoes_route():
    # return render_template('publicacoes.html', active_page='publicacoes_route')
    return "Página 'Publicações' em construção!", 404

@main_bp.route('/noticias')
def noticias_route():
    # return render_template('noticias.html', active_page='noticias_route')
    return "Página 'Notícias' em construção!", 404

@main_bp.route('/contato')
def contato_route():
    # return render_template('contato.html', active_page='contato_route')
    return "Página 'Contato' em construção!", 404