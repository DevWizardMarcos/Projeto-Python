import sqlite3

try:
        

    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()



    cursor.execute('''

CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
)                                 
        ''')

    print("Conexão com Banco de dados bem sucessedida !!")
    print("Tabela 'produtos' criada ou já existente")

except sqlite3.Error as e: 
    print("Error  ao conectar ao banco de dados", e )

finally: 

    if conn : 
            conn.commit()
            conn.close()
            print("Conexão com o banco de dados finalizada")




import sqlite3

def cadastrar_produtos():
    try:
        conn = sqlite3.connect('estoque.db')
        cursor = conn.cursor()

        nome = input("Digite o nome do produto que queira cadastrar: ")
        quantidade = int(input("Digite a quantidade de produto escolhido: "))
        preco = float(input("Digite o valor do produto escolhido: "))

        cursor.execute('''
        INSERT INTO produtos (nome, quantidade, preco)
        VALUES (?, ?, ?)
        ''', (nome, quantidade, preco))

        conn.commit()
        print("Produto cadastrado com sucesso!")

    except sqlite3.Error as e:
        print("Erro ao cadastrar o produto:", e)

    finally:
        if conn:
            conn.close()
            print("Conexão com o banco de dados finalizada.")

         

if __name__ == "__main__":
    while True:
        print("\n1. Cadastrar Produto")
        print("2. Sair")
        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            cadastrar_produtos()
        elif opcao == "2":
            print("Encerrando o Sistema de Cadastro de Produtos :(")
            break
        else:
            print("Opção inválida!")

