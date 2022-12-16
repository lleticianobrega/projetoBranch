print('estou modificando a minha branch conteudo')
class conteudo:
    def comandoLista(self):

        lista = []
        for recebe in range(2):
            nome = input('nome: ')
            idade = int(input('idade: '))
            profissao = input('prof: ')
            lista.append(nome)
            lista.append(idade)
            lista.append(profissao)
        print(lista)