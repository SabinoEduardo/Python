from minhas_funcoes import adicionar_tarefa, deletar_tarefa, repor_tarefa
from time import sleep


lista_tarefas = list()
tarefas_deletadas = list()

print("de - deletar tarefa")
print("re - Refazer tarefa")
print('ls - Listar tarefas')
print('sr - Fechar Programa')
while True:
    tarefa = str(input("Digite uma tarefa ou de, re, ls, sr: "))
    if tarefa == 'de':
        deletar_tarefa(lista_tarefas, tarefas_deletadas)
    elif tarefa == "re":
        repor_tarefa(lista_tarefas, tarefas_deletadas)
    elif tarefa == "ls":
        if not lista_tarefas:
            print("A lista está vazia")
        else:
            for index, tarefa in enumerate(lista_tarefas):
                print(f"Tarefa {index + 1} - {tarefa}")
    elif tarefa == "sr":
        print("Fechando o programa...")
        sleep(1.5)
        break
    else:
        adicionar_tarefa(lista_tarefas, tarefa)
