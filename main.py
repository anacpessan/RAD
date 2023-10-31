import tkinter as tk
import sqlite3
from interface import criar_interface, salvar_dados, carregar_curriculo

if __name__ == "__main__":
    conn = sqlite3.connect('desenvolvedores.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS desenvolvedores (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER,
            cidade TEXT,
            estado TEXT,
            telefone TEXT,
            email TEXT,
            experiencia BOOLEAN,
            soft skills, TEXT,
            hard skills, TEXT,
            linkedin TEXT,
            status atual BOOLEAN,
            expectativa salario INTEGER,
            curriculo TEXT,
            
        )
    ''')

    root = tk.Tk()
    root.title("Search Tech - Unindo os melhores Jobs com os melhores Devs!")

    criar_interface(root)  # Chame a função criar_interface, passando a janela 'root'

    root.mainloop()

