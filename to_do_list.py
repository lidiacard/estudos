import json
import os

def carregar_arquivo():
    """
    Carrega o arquivo 'tarefas.json' caso exista.
    Retorna um dicionário com as listas 'lista' (tarefas atuais) 
    e 'removidas' (tarefas desfeitas).
    Se o arquivo não existir ou estiver corrompido, retorna um dicionário vazio inicial.
    """
    if os.path.exists('tarefas.json'):
        try:
            with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print('Atenção: O arquivo "tarefas.json" está corrompido. Iniciando com dados vazios.')
            return {'lista': [], 'removidas': []}
    return {'lista': [], 'removidas': []}


def salvar_arquivo(dados):
    """
    Salva o dicionário 'dados' no arquivo 'tarefas.json'.
    Usa indentação para facilitar a leitura manual do arquivo.
    """
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        

def menu():
    """
    Exibe o menu de comandos disponíveis para o usuário.
    """
    print(10 * '=')
    print('Comandos:\nlistar\ndesfazer\nrefazer\nsair')
    print(10 * '=')


def comando_ou_tarefa(dados):
    """
    Lê a entrada do usuário e executa o comando correspondente ou adiciona uma nova tarefa.
    Retorna False se o comando for 'sair', para encerrar o programa.
    """
    opcao = input('Digite um COMANDO ou uma TAREFA: ').strip().lower()
    if not opcao:
        print("Nenhuma entrada detectada. Por favor, digite um comando ou uma tarefa.")
        return True
    
    if opcao in ['listar', 'desfazer', 'refazer', 'sair']:
        if opcao == 'listar':
            listar_tarefas(dados)
        elif opcao == 'desfazer':
            desfazer_tarefa(dados)
        elif opcao == 'refazer':
            refazer_tarefa(dados)
        elif opcao == 'sair':
            print('Saindo...')
            return False
    else:
        dados['lista'].append(opcao) # Adiciona nova tarefa à lista
        salvar_arquivo(dados)
        print(f'Tarefa {opcao} acrescentada na lista.')
    return True


def listar_tarefas(dados):
    """
    Lista todas as tarefas atualmente salvas.
    Se não houver tarefas, exibe mensagem.
    """
    if dados['lista']:
        print('TAREFAS:')
        for tarefa in dados['lista']:
            print(f'- {tarefa}')
    else:
        print('Não há tarefas na lista.')


def desfazer_tarefa(dados):
    """
    Remove a última tarefa adicionada da lista 'lista' e adiciona na lista 'removidas' para possível refazer.
    Se não houver tarefas para desfazer, informa o usuário.
    """
    if dados['lista']:
        tarefa = dados['lista'].pop()
        dados['removidas'].append(tarefa)
        print('Desfeito:', tarefa)
        salvar_arquivo(dados)
    else:
        print('Nada a desfazer.')


def refazer_tarefa(dados):
    """
    Refaz a última tarefa que foi desfeita, movendo-a da lista 'removidas' para 'lista'.
    Se não houver tarefas para refazer, informa o usuário.
    """
    if dados['removidas']:
        tarefa = dados['removidas'].pop()
        dados['lista'].append(tarefa) # refaz a última tarefa removida
        print('Refeito: ', tarefa)
        salvar_arquivo(dados)
    else:
        print('Nada a refazer.')

# Carrega os dados do arquivo ou cria estrutura inicial
dados = carregar_arquivo()
# Loop principal do programa, exibe menu e processa comandos até o usuário sair
while True:
    menu()
    if not comando_ou_tarefa(dados):
        break
    