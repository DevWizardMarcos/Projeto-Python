import sqlite3
import flet as ft

def conectar():
    return sqlite3.connect('estoque.db')

def criar_tabela():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )                                 
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        if conn:
            conn.close()

def cadastrar_produto(nome, quantidade, preco):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO produtos (nome, quantidade, preco)
        VALUES (?, ?, ?)
        ''', (nome, quantidade, preco))
        conn.commit()
        return "Produto cadastrado com sucesso!"
    except sqlite3.Error as e:
        return f"Erro ao cadastrar o produto: {e}"
    finally:
        if conn:
            conn.close()

def listar_produtos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, quantidade, preco FROM produtos')
        produtos = cursor.fetchall()
        return produtos
    except sqlite3.Error as e:
        return f"Erro ao listar produtos: {e}"
    finally:
        if conn:
            conn.close()

def main(page: ft.Page):
    page.title = "Sistema de Gerenciamento de Estoque"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "black"

    nome_input = ft.TextField(label="Nome do Produto", autofocus=True, border_color="#fb0100", width=500)
    quantidade_input = ft.TextField(label="Quantidade", keyboard_type=ft.KeyboardType.NUMBER, border_color="#fb0100", width=500)
    preco_input = ft.TextField(label="Preço", keyboard_type=ft.KeyboardType.NUMBER, border_color="#fb0100", width=500)

    

    def on_cadastrar_click(e):
        nome = nome_input.value
        quantidade = int(quantidade_input.value)
        preco = float(preco_input.value)
        
        resultado = cadastrar_produto(nome, quantidade, preco)
        
        resultado_label.value = resultado
        nome_input.value = ""
        quantidade_input.value = ""
        preco_input.value = ""
        page.update()

    cadastrar_button = ft.ElevatedButton("Cadastrar Produto", on_click=on_cadastrar_click, width=200 , bgcolor = "red" , color = "white")

    resultado_label = ft.Text("", size=16)

    def on_listar_click(e):
        produtos = listar_produtos()
        
        produtos_lista.clear()
        
        for produto in produtos:
            produtos_lista.add(ft.Text(f"ID: {produto[0]} - {produto[1]} | Quantidade: {produto[2]} | Preço: R${produto[3]:.2f}"))
        
        page.update()
    
    listar_button = ft.ElevatedButton("Listar Produtos", on_click=on_listar_click, width=200 , bgcolor = "#4bc228" ,  color = "white")

    produtos_lista = ft.Column()

    imagem_logo = ft.Image(src="background_image.jpg", width=400, height=400)

    page.add(
        imagem_logo,
        nome_input,
        quantidade_input,
        preco_input,
        cadastrar_button,
        resultado_label,
        listar_button,
        produtos_lista
        
    )



if __name__ == "__main__":
    criar_tabela()
    ft.app(target=main)


