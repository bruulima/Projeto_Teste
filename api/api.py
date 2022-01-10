from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import csv
from csv import writer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

clienteFile = '../db/cliente.csv'
categoriaFile = '../db/categoria.csv'
tituloFile = '../db/titulo.csv'
autorFile = '../db/autor.csv'
colecaoFile = '../db/colecao.csv'
promocaoFile = '../db/promocao.csv'

@app.route('/cliente/inserir', methods=['POST'])
def inserirCliente():
    cliente = json.loads(request.data)
    inserirClienteCsv(cliente)
    return { 'message': 'Cliente salvo com sucesso' }


@app.route('/cliente/listar', methods=['GET'])
def listarCliente():
    clientes = listarClienteCsv()
    return json.dumps(clientes)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/cliente/deletar/<nroLinha>', methods=['DELETE'])
def deletarCliente(nroLinha):
    clientes = listarClienteCsv()
    novosClientes = []       

    i = 0
    for cliente in clientes:        
        if int(nroLinha) != i:
            novosClientes.append(cliente)
        i = i + 1

    reinserirClienteCsv(novosClientes)
    return { 'message': 'Cliente deletado com sucesso' }


def listarClienteCsv():
    clientes = []
    with open(clienteFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                clientes.append({ 
                    'nome': linha[0], 
                    'telefone': linha[1], 
                    'email': linha[2],
                    'cpf': linha[3]
                })
            count += 1

    return clientes


def inserirClienteCsv(cliente):
    novaLinha = [cliente["nome"], cliente["telefone"], cliente["email"], cliente["cpf"]]
    with open(clienteFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirClienteCsv(clientes):
    linhas = []
    linhas.append(["nome", "telefone", "email", "cpf"]) #é necessário inserir novamente o cabeçalho da planilha

    for cliente in clientes:
        novaLinha = [cliente["nome"], cliente["telefone"], cliente["email"], cliente["cpf"]]
        linhas.append(novaLinha)

    with open(clienteFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()


        ###########################################

# C A T E G O R I A

@app.route('/categoria/inserir', methods=['POST'])
def inserirCategoria():
    categoria = json.loads(request.data)
    inserirCategoriaCsv(categoria)
    return { 'message': 'Categoria salva com sucesso' }


@app.route('/categoria/listar', methods=['GET'])
def listarCategoria():
    categoria = listarCategoriaCsv()
    return json.dumps(categoria)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/categoria/deletar/<nroLinha>', methods=['DELETE'])
def deletarCategoria(nroLinha):
    categorias = listarCategoriaCsv()
    novosCategorias = []       

    i = 0
    for categoria in categorias:        
        if int(nroLinha) != i:
            novosCategorias.append(categoria)
        i = i + 1

    reinserirCategoriaCsv(novosCategorias)
    return { 'message': 'Categoria deletada com sucesso' }


def listarCategoriaCsv():
    categorias = []
    with open(categoriaFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                categorias.append({ 
                    'id': linha[0], 
                    'academico': linha[1], 
                    'romance': linha[2],
                    'espirita': linha[3]
                })
            count += 1

    return categorias


def inserirCategoriaCsv(categoria):
    novaLinha = [categoria["id"], categoria["academico"], categoria["romance"], categoria["espirita"]]
    with open(categoriaFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirCategoriaCsv(categorias):
    linhas = []
    linhas.append(["id", "academico", "romance", "espirita"]) #é necessário inserir novamente o cabeçalho da planilha

    for categoria in categorias:
        novaLinha = [categoria["id"], categoria["academico"], categoria["romance"], categoria["espirita"]]
        linhas.append(novaLinha)

    with open(categoriaFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()        

        ############################################

# T Í T U L O

@app.route('/titulo/inserir', methods=['POST'])
def inserirTitulo():
    titulo = json.loads(request.data)
    inserirTituloCsv(titulo)
    return { 'message': 'Título salvo com sucesso' }


@app.route('/titulo/listar', methods=['GET'])
def listarTitulo():
    titulos = listarTituloCsv()
    return json.dumps(titulos)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/titulo/deletar/<nroLinha>', methods=['DELETE'])
def deletarTitulo(nroLinha):
    titulos = listarTituloCsv()
    novosTitulos = []       

    i = 0
    for titulo in titulos:        
        if int(nroLinha) != i:
            novosTitulos.append(titulo)
        i = i + 1

    reinserirTituloCsv(novosTitulos)
    return { 'message': 'Título deletado com sucesso' }


def listarTituloCsv():
    titulos = []
    with open(tituloFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                titulos.append({ 
                    'id': linha[0], 
                    'idAutor': linha[1], 
                    'idEditora': linha[2],
                    'nomeDoTitulo': linha[3],
                    'quantidadeDePaginas': linha[4],
                    'valor': linha[5]
                })
            count += 1

    return titulos


def inserirTituloCsv(titulo):
    novaLinha = [titulo["id"], titulo["idAutor"], titulo["idEditora"], titulo["nomeDoTitulo"], titulo["quantidadeDePaginas"], titulo["valor"]]
    with open(tituloFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirTituloCsv(titulos):
    linhas = []
    linhas.append(["id", "idAutor", "idEditora", "nomeDoTitulo", "quantidadeDePaginas", "valor"]) #é necessário inserir novamente o cabeçalho da planilha

    for titulo in titulos:
        novaLinha = [titulo["id"], titulo["idAutor"], titulo["idEditora"], titulo["nomeDoTitulo"], titulo["quantidadeDePaginas"], titulo["valor"]]
        linhas.append(novaLinha)

    with open(tituloFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

####################################################

# A U T O R E S

@app.route('/autor/inserir', methods=['POST'])
def inserirAutor():
    autor = json.loads(request.data)
    inserirAutorCsv(autor)
    return { 'message': 'Autor salvo com sucesso' }


@app.route('/autor/listar', methods=['GET'])
def listarAutor():
    autores = listarAutorCsv()
    return json.dumps(autores)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/autor/deletar/<nroLinha>', methods=['DELETE'])
def deletarAutor(nroLinha):
    autores = listarAutorCsv()
    novosAutores = []       

    i = 0
    for autor in autores:        
        if int(nroLinha) != i:
            novosAutores.append(autor)
        i = i + 1

    reinserirAutorCsv(novosAutores)
    return { 'message': 'Autor deletado com sucesso' }


def listarAutorCsv():
    autores = []
    with open(autorFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                autores.append({ 
                    'id': linha[0], 
                    'nome': linha[1], 
                    'nacionalidade': linha[2]
                })
            count += 1

    return autores


def inserirAutorCsv(autor):
    novaLinha = [autor["id"], autor["nome"], autor["nacionalidade"]]
    with open(autorFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirAutorCsv(autores):
    linhas = []
    linhas.append(["id", "nome", "nacionalidade"]) #é necessário inserir novamente o cabeçalho da planilha

    for autor in autores:
        novaLinha = [autor["id"], autor["nome"], autor["nacionalidade"]]
        linhas.append(novaLinha)

    with open(autorFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

#############################################

# C O L E C A O

@app.route('/colecao/inserir', methods=['POST'])
def inserirColecao():
    colecao = json.loads(request.data)
    inserirColecaoCsv(colecao)
    return { 'message': 'Coleção salva com sucesso' }


@app.route('/colecao/listar', methods=['GET'])
def listarColecao():
    colecoes = listarColecaoCsv()
    return json.dumps(colecoes)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/colecao/deletar/<nroLinha>', methods=['DELETE'])
def deletarColecao(nroLinha):
    colecoes = listarColecaoCsv()
    novasColecoes = []       

    i = 0
    for colecao in colecoes:        
        if int(nroLinha) != i:
            novasColecoes.append(colecao)
        i = i + 1

    reinserirColecaoCsv(novasColecoes)
    return { 'message': 'Coleção deletada com sucesso' }


def listarColecaoCsv():
    colecoes = []
    with open(colecaoFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                colecoes.append({ 
                    'id': linha[0], 
                    'idTitulo': linha[1], 
                    'idAutor': linha[2],
                    'idEditora': linha[3]
                })
            count += 1

    return colecoes


def inserirColecaoCsv(colecao):
    novaLinha = [colecao["id"], colecao["idTitulo"], colecao["idAutor"], colecao["idEditora"]]
    with open(colecaoFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirColecaoCsv(colecoes):
    linhas = []
    linhas.append(["id", "idTitulo", "idAutor", "idEditora"]) #é necessário inserir novamente o cabeçalho da planilha

    for colecao in colecoes:
        novaLinha = [colecao["id"], colecao["idTitulo"], colecao["idAutor"], colecao["idEditora"]]
        linhas.append(novaLinha)

    with open(colecaoFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()


#####################################

# P R O M O C A O

@app.route('/promocao/inserir', methods=['POST'])
def inserirPromocao():
    promocao = json.loads(request.data)
    inserirPromocaoCsv(promocao)
    return { 'message': 'Promoção salva com sucesso' }


@app.route('/promocao/listar', methods=['GET'])
def listarPromocao():
    promocoes = listarPromocaoCsv()
    return json.dumps(promocoes)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/promocao/deletar/<nroLinha>', methods=['DELETE'])
def deletarPromocao(nroLinha):
    promocoes = listarPromocaoCsv()
    novosPromocoes = []       

    i = 0
    for promocao in promocoes:        
        if int(nroLinha) != i:
            novosPromocoes.append(promocao)
        i = i + 1

    reinserirPromocaoCsv(novosPromocoes)
    return { 'message': 'Promoção deletada com sucesso' }


def listarPromocaoCsv():
    promocoes = []
    with open(promocaoFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                promocoes.append({ 
                    'idTitulo': linha[0], 
                    'desconto': linha[1]
                })
            count += 1

    return promocoes


def inserirPromocaoCsv(promocao):
    novaLinha = [promocao["idTitulo"], promocao["desconto"]]
    with open(promocaoFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirPromocaoCsv(promocoes):
    linhas = []
    linhas.append(["idTitulo", "desconto"]) #é necessário inserir novamente o cabeçalho da planilha

    for promocao in promocoes:
        novaLinha = [promocao["idTitulo"], promocao["desconto"]]
        linhas.append(novaLinha)

    with open(promocaoFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()
