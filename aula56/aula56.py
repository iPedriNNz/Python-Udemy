if __name__ == '__main__':
    tarefas = []
    ultima = ''


def todo_ls():
    print('#' * 30)
    count = 1
    for t in tarefas:
        print(f'Tarefa nº{count}: {t}')
        count += 1
    count = 1
    print('#' * 30)

def todo_rm():
    rm = input(f'Gostaria realmente de remover a tarefa "{tarefas[-1]}" da sua lista ? [S / N]').upper().strip()
    if rm == 'S':
        tarefas.pop()
        print('Tarefa removida com sucesso! ')
    elif rm == 'N':
        print('Operação cancelada!')
    else:
        print('Opção inválida, tente novamente !')

def todo_rf():
    rf = input(f'Gostaria realmente de refazer a tarefa "{ultima}" para sua lista ? [S / N]').upper().strip()
    if rf == 'S':
        tarefas.append(ultima)
        print('Tarefa refeita com sucesso! ')
    elif rf == 'N':
        print('Operação cancelada!')
    else:
        print('Opção inválida, tente novamente !')



while True:
    todo = str(input('Escolha uma das opções:\n'
        '[1] Adicionar tarefa\n'
        '[2] Listar tarefas\n'
        '[3] Desfazer\n'
        '[4] Refazer\n'
        '[5] Sair\n'
        'Sua escolha: '))

    if todo.isnumeric():
        todo = int(todo)
        if todo not in range(1, 6):
            print('Escolha entre as opções 1 e 4.')
    else:
        print('Você deve digitar apenas números.')
        continue

    if todo == 1:
        nome_tarefa = input('Digite o nome da tarefa a ser adicionada: ')
        ultima = nome_tarefa
        tarefas.append(nome_tarefa)

    elif todo == 2:
        todo_ls()

    elif todo == 3:
        todo_rm()

    elif todo == 4:
        todo_rf()

    elif todo == 5:
        print('Fechando o programa...')
        break
