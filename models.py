# -*- coding: UTF-8 -*-
'Enconding'

#Orientação a objetos
class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        'Método utilizado para imprimir os valores do objeto'
        print 'Nome: %s, Telefone: %s, Empresa: %s, Curtidas: %s' % (self.nome, self.telefone, self.empresa, self.__curtidas)

    def curtir(self):
        'Método utilizado para incrementar o total de curtidas'
        self.__curtidas += 1

    def obter_curtidas(self):
        'Método utilizado para retornar o total de curtidas'
        return self.__curtidas

class Data(object):
    'Classe utilizada para informar a data'

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimi(self):
        'Método utilizado para imprimir os valores do objeto'
        print '%s/%s/%s' % (self.dia, self.mes, self.ano)

class Pessoa(object):
    'Classe utilizada para calculo do IMC de uma pessoa'

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = int(peso)
        self.altura = float(altura)

    def imprime_imc(self):
        'Método utilizado para imprimir o calculo do IMC'
        altura = (self.altura * self.altura)
        imc = self.peso / altura
        print 'Imc de %s: %s' % (self.nome, imc)
        