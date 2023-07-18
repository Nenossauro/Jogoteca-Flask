from flask import Flask, render_template, request, redirect, session, flash
import os, pymongo
#Importando os módulos necessários para o projeto Flask.

app = Flask(__name__)
app.secret_key = 'enzo'
#Criando uma instância do objeto Flask e definindo a chave secreta para uso nas sessões.

os.system("cls")
#Executando o comando "cls" para limpar a tela do console.

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["biblioteca"]
collection = db["users"]
collection_livros = db["livros"]
#Estabelecendo a conexão com o banco de dados MongoDB, especificando o banco de dados "biblioteca" e a coleção "users".
#Se você quiser abrir o programa ai na sua casa, é só criar um banco de dados com essas caracteristicas

@app.route('/')
def index():
    return render_template('index.html')
#Definindo a rota principal (/) para renderizar o template 'index.html'.

@app.route('/inicio')
def inicio():
    if 'user_logged' not in session or session['user_logged'] == None:
        return redirect('/')
    return render_template('land.html',pessoa =session['user_logged'])
#Definindo a rota '/inicio', que requer autenticação. 
#Se o usuário não estiver logado, será redirecionado para a página principal ('/'). 
#Caso contrário, o template 'land.html' será renderizado, passando a variável 'pessoa' com o valor da sessão 'user_logged'.

@app.route('/estante')
def estante():
    if 'user_logged' not in session or session['user_logged'] == None:
        return redirect('/')
    livros_id = collection_livros.find()
    livro = []
    ids = []
    for item in livros_id:
        v_item = item["capa"]
        v_id = item["id"]
        livro.append(v_item)
        ids.append(int(v_id))
    return render_template('estante.php',pessoa =session['user_logged'],livro = livro,ids = ids)
@app.route('/perfil')
def perfil():
    if 'user_logged' not in session or session['user_logged'] == None:
        return redirect('/')
    return render_template('perfil.php',pessoa =session['user_logged'])

@app.route('/criar', methods=['POST',])
def criar():
    user = request.form['userr']
    nome = request.form['nomer']
    senha = request.form['senhar']
    collection.insert_one({"nome":user,"email":nome,"senha":senha})
    return redirect('/')
#Definindo a rota '/criar', que recebe uma solicitação POST para criar um novo usuário. 
#Os dados do formulário são recuperados e um novo documento é inserido na coleção 'users' no banco de dados. 
#Após a inserção, o usuário é redirecionado para a página principal ('/').

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        temp_user = ''
        temp_senha = ''
        usuario = collection.find({"email": nome})
        for users in usuario:
            temp_user = users["email"]
            temp_senha = users["senha"]
            nome_user = users["nome"]
        if nome == temp_user:
            if senha == temp_senha:
                session['user_logged'] = nome_user
                flash(session['user_logged']+'! Usuario logado com sucesso!')
                return redirect('/inicio')
            else:
                flash("Senha invalida")
                return redirect('/')
        else:
            flash("Email invalido")
            return redirect('/')
    else:
        return "Método não permitido."
#Definindo a rota '/autenticar', que recebe uma solicitação POST com os dados do formulário de login. 
#A função verifica se as credenciais fornecidas correspondem a um usuário existente no banco de dados. 
#Se as credenciais forem válidas, o usuário é autenticado e armazenado na sessão. Caso contrário, mensagens de erro são exibidas. 
#A função também inclui o uso de flash messages para fornecer feedback ao usuário.    
    
@app.route('/logout')
def logout():
    session['user_logged'] = None
    return redirect('/')
#Definindo a rota '/logout' para efetuar o logout do usuário. 
#A sessão 'user_logged' é definida como None e o usuário é redirecionado para a página principal ('/').







app.run(debug=True)
#Iniciando o servidor Flask.