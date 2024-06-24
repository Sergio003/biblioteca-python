# Biblioteca para limpar o terminal
# Biblioteca para deixar o tempo de resposta um pouco mais lento
# Biblioteca para sair do programa

import os
import time
import sys

# Função para gerenciar colaboradores
def gerenciar_colaboradores():
    colaboradores = {}
    os.system("cls")
    while True:
        print("\n")
        print("="*82)
        print("""
              
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽⡋⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠙⠝⠂⠄⢘⠋⠃⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ 
        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                                                                                                        """)
        
        print("                           [1] Adicionar colaborador                                       ")
        print("                           [2] Remover colaborador                                         ")
        print("                           [3] Listar colaboradores                                        ")
        print("                           [4] Voltar ao menu principal                                    ")
        print("\n")
        print("="*82)        
        
        opcao = input("\nDigite um número e aperte enter: ")

        if opcao == "1":
            nome = input("Digite o nome do colaborador: ")
            senha = input("Digite a senha: ")
            colaboradores[nome] = senha
            print("Colaborador adicionado com sucesso!")
            time.sleep(4)
            os.system("cls")

        elif opcao == "2":
            nome = input("Digite o nome do colaborador que deseja remover: ")
            if nome in colaboradores:
                del colaboradores[nome]
                print("Colaborador removido com sucesso!")
            else:
                print("Colaborador não encontrado.")
            time.sleep(4)
            os.system("cls")

        elif opcao == "3":
            print("\nLista de colaboradores:")
            for nome, senha in colaboradores.items():
                print(f"Nome: {nome}, Senha: {senha}")
            if len(colaboradores) == 0:
                print("Não tem ninguém na lista... ")
            time.sleep(6)
            os.system("cls")
        elif opcao == "4":
            os.system("cls")
            main()

        else:
            print("Opção inválida, escolha um número do menu e aperte enter...")
            time.sleep(4)
            os.system("cls")



# Função para login
def login(colaboradores):
    while True:
        nome = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        if nome in colaboradores and colaboradores[nome] == senha:
            print("Administrador Logado com sucesso!")
            return nome
        else:
            print("Usuário ou senha inválidos, tente novamente.")
            print("Limpando console, por favor aguarde... ")
        time.sleep(4)
        os.system("cls")
        main()

# Função para cadastrar livros
def cadastrar_livros():
    livros = []
    os.system("cls")

    while True:
        print("\n")
        print("="*85)
        print("""
                ____________________________________________________
               |____________________________________________________|
               |                   | P |  _                         |
               | __     __   ____  | Y | | |____    ____     _  __ _|
               ||  |__ |--|_| || |_| T | |_|**|*|__|+|+||___| ||  | |
               ||==|^^||--| |=||=| | H | | |~~|~|  |=|=|| | |~||==| |
               ||  |##||  | | || | | O | |-|  | |==|+|+||-|-|~||__| |
               ||__|__||__|_|_||_|_|_N_|_|_|__|_|__|_|_||_|_|_||__|_|
               |____________________________________________________|
               | __________________________________________________ |
               ||=|=|=|=|=|=|=|=|=|=|=|   ..\/ |  |_|  ||#||==|  / /|
               || | | | | | | | | | | |/\ \  \\ |++|=|  || ||==| / / |
               ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
               |____________________ /\~()/()~//\ __________________|
               | __   __    _  _     \_  (_ .  _/ _    ___     _____|
               ||~~|_|..|__| || |_ _   \ //\\ /   |=|__|~|~|___| | | |
               ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
               ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
               |_________________ _/    \/\/\/    \_ _______________|
               | _____   _   __  |/      \../      \|  __   __   ___|
               ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
               ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
               ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
               |_________ __________\___\____/___/___________ ______|
               |__    _  /    ________     ______           /| _ _ _|
               |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
               | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
               |  \/\|/   /(____|/ //                    /  /||~|~|~|
               |___\_/   /________//   ________         /  / ||_|_|_|
               |___ /   (|________/   |\_______\       /  /| |______|
        
                                                        """)
        print("                              [1] Adicionar livro                         ")
        print("                              [2] Listar livros                           ")
        print("                              [3] Voltar ao menu principal                ")
        print("\n")
        print("="*85)
        
        opcao = input("\nDigite um número e aperte enter: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            ano = input("Digite o ano de publicação: ")
            livros.append({"Título": titulo, "Autor": autor, "Ano": ano})
            print("Livro cadastrado com sucesso!")
            time.sleep(5)
            os.system("cls")

        elif opcao == "2":
            print("\nLista de livros cadastrados:")
            for livro in livros:
                print(f"Título: {livro['Título']}, Autor: {livro['Autor']}, Ano: {livro['Ano']}")
            if len(livros) == 0:
                print("Você ainda não cadastrou nenhum livro...")
            time.sleep(8)
            os.system("cls")

        elif opcao == "3":
            os.system("cls")
            main()

        else:
            print("Opção inválida, escolha um número do menu e aperte enter...")
            time.sleep(5)
            os.system("cls")

# Função principal
def main():
    os.system("cls")
    colaboradores = {"admin": "admin"}  # Colaborador padrão para iniciar o sistema
    usuario_logado = None
    
    while True:

        if usuario_logado:
            print(f"\nBem-vindo, {usuario_logado}!")
            time.sleep(5)
            os.system("cls")
            main()
        else:
            print("\n")
            print("="*85)
            print("""
                  
                             ,..........   ..........,         
                         ,..,'          '.'          ',..,     
                        ,' ,'            :            ', ',    
                       ,' ,'             :             ', ',   
                      ,' ,'              :              ', ',      
                     ,' ,'............., : ,.............', ', 
                    ,'  '............   '.'   ............'  ',
                   '''''''''''''''''''';''';'''''''''''''''''''' 
                                        '''                                     
                  """)
            print("                                 [1] Login                                   ")
            print("                                 [2] Gerenciar Usuários                      ")
            print("                                 [3] Cadastrar livros                        ")
            print("                                 [4] Sair                                    ")
            print("\n")
            print("="*85)
            print("\n")
        try:
            opcao = input("Digite um número do menu principal e aperte enter: ")
        
            if opcao == "1":
                usuario_logado = login(colaboradores)
            elif opcao == "2":
                gerenciar_colaboradores()
            elif opcao == "3":
                cadastrar_livros()
            elif opcao == "4":
                print("Quando entrar novamente, utilize o usuário\ne a senha abaixo para fazer login. ")
                print("Usuário padrão: admin ")
                print("Senha padrão: admin ")
                time.sleep(5)
                sys.exit()
            else:
                print("\nVocê digitou nenhuma opção do menu principal, tente novamente. ")
                print("Limpando console, por favor aguarde... ")
                time.sleep(4)
                os.system("cls")
                main()
        except:
            print("Obrigado e até a próxima! ")
            time.sleep(2)
            sys.exit()
            
            
if __name__ == "__main__":
    main()