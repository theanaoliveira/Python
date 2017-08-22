# -*- coding: UTF-8 -*-
'Enconding'

def cadastrar(lista_nomes):
    nome = raw_input()
    lista_nomes.append(nome)
    #print '%s' %(lista_nomes)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome    

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    item_remove = raw_input()
    nomes.remove(item_remove)
    listar(nomes)

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome_a_ser_alterado = raw_input()
    if(nome_a_ser_alterado in nomes):
        posicao_nome = nomes.index(nome_a_ser_alterado)
        print 'Digite o novo nome:'
        novo_nome = raw_input()
        nomes[posicao_nome] = novo_nome
    else:
        print 'Nome não encontrado na lista'

def procurar(nomes):
    print 'Digite nome a procurar:'
    nome_a_procurar = raw_input()

    if(nome_a_procurar in nomes):
        print 'Nome encontrado.'
    else:
        print 'Nome não encontrado.'

import re
def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print(resultados)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):    
        print '\n\nDigite: 1 para cadastrar\nDigite: 2 para listar os nomes\nDigite: 3 para remover algum nome da lista\nDigite: 4 para alterar algum nome da lista\nDigite: 0 para terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)
        
        if(escolha == '3'):
            remover(nomes)
        
        if(escolha == '4'):
            alterar(nomes)

menu() #estamos chamando o menu
