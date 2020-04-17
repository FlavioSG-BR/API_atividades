from models import Pessoas
from models import Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome="Flavio", Idade=30)
    print(pessoa)
    pessoa.save()


def consulta():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Flavio').first()
    print(pessoa.Idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Flavio').first()
    pessoa.nome = 'Godoy'
    pessoa.save()

def altera_idade():
    pessoa = Pessoas.query.filter_by(nome='Flavio').first()
    pessoa.Idade = 31
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Flavio').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuarios = Usuarios(login=login, senha=senha)
    usuarios.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_pessoas()
    #consulta()
    #altera_pessoa()
    #altera_idade()
    #exclui_pessoa()
    insere_usuario('flavio', '123')
    insere_usuario('godoy', '321')
    consulta_todos_usuarios()
