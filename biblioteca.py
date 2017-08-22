# -*- coding: UTF-8 -*-
'Enconding'

def gera_nome_convite(convite):
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial:posicao_final]
    return parte1 + ' ' + parte2

def envia_convite(nome_convite):
    print 'Enviando convite para %s' % (nome_convite)

def processa_convite(nome_convidado):
    nome = gera_nome_convite(nome_convidado)
    envia_convite(nome)

from datetime import date
'Importa a classe date'

def calcula_idade():
    print 'Digite seu ano de nascimento:'
    ano_como_string = raw_input()
    ano_atual = date.today().year
    idade = ano_atual - int(ano_como_string)
    print 'Sua idade e: %s' %(idade)
