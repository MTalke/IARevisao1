# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from collections import deque



if __name__ == "__main__":
    
    def questao1():
        print("Ola Mundo")
        
        Menu()
        
    def questao2():
        tamanho = 10
        x = 1
        vetor = []
        while x <= tamanho:
            opcao = int(input("digite o numero: "))
            vetor.append(opcao)
            x = x + 1
            
        print(vetor)
        
        Menu()
    
    def questao3():
        matriz = [] # lista vazia
        tamanho = 10
        valor = 0
        n_linhas = tamanho
        n_colunas = tamanho
        for i in range(n_linhas):
            # cria a linha i
            linha = [] # lista vazia
            for j in range(n_colunas):
                linha.append(valor)

            # coloque linha na matriz
            matriz.append(linha)
            
        print(matriz)
        
        Menu()
    
    def questao4():
        pilha = [] # pilha vazia
        tamanho = 10

        for i in range(tamanho):
            # cria a linha i
            numero = int(input("digite o numero: "))
            pilha.append(numero)
       
        print(pilha)
        print("Desempilhando")
        
        for i in range(tamanho):
            # cria a linha i
            pilha.pop()
            print(pilha)
        
        Menu()
            
    def questao5():
        fila = deque([]) # pilha vazia
        tamanho = 5

        for i in range(tamanho):
            # cria a linha i
            numero = int(input("digite o numero: "))
            fila.append(numero)
       
        print(fila)
        print("Desinfileirando")
        
        for i in range(tamanho):
            # cria a linha i
            fila.popleft()
            print(fila)
            
        Menu()
        
    class Tarefa():
        def __init__(self, nome, descricao, prioridade):
            self.nome = nome
            self.descricao = descricao
            self.prioridade = prioridade

        def criandoTarefa(self, nome, descricao, prioridade):
            self.nome = nome
            self.descricao = descricao
            self.prioridade = prioridade
            
        def getTarefas(self):
            return self.nome, self.descricao, self.prioridade
    
    def questao6():
        tamanho = 2
        tarefas = []
        for i in range(tamanho):
            nome = raw_input("digite o nome da tarefa:")
            descricao = raw_input("digite a descricao da tarefa: ")
            prioridade = int(input("digite de 0 a 5 a prioridade da tarefa: "))
            tarefas.append(Tarefa(nome,descricao,prioridade))
            
        for tarefa in tarefas:
            print "\"%s\"  %s (%s)" % (tarefa.nome, tarefa.descricao, tarefa.prioridade)
        #Ordena a lista baseada na prioridade do maior para o menor
        prioridade = sorted(tarefas, key=lambda x: x.prioridade,reverse=True)
        print("Nome da tarefas por prioridade")
        for tarefa in prioridade:
            print(tarefa.nome)
            print(tarefa.descricao)


        Menu()
            
    def Menu():    
        print("Escolha a opcao que deseja")
        print("Escolha 1 para questao 1")
        print("Escolha 2 para questao 2")
        print("Escolha 3 para questao 3")
        print("Escolha 4 para questao 4")
        print("Escolha 5 para questao 5")
        print("Escolha 6 para questao 6")
        opcao = int(input("digite a opcao: "))

        if (opcao == 1):
            questao1()
        elif(opcao == 2):
            questao2()
        elif(opcao == 3 ):
            questao3()
        elif(opcao == 4):
            questao4()
        elif(opcao == 5):
            questao5()
        elif(opcao == 6):
            questao6()
        else:
            print("Nao tem essa questao")
            Menu()
            
    Menu()