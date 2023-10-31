import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    conn_login = sqlite3.connect('login.db')
    cursor_login = conn_login.cursor()
    
    # Verifique se o nome de usuário e senha estão corretos no banco de dados
    cursor_login.execute("SELECT * FROM login WHERE usuario=? AND senha=?", (usuario, senha))
    resultado = cursor_login.fetchone()
    conn_login.close()

    if resultado is not None:
        messagebox.showinfo("Login", "Login bem-sucedido")
        mostrar_interface_admin()
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos")

    conn_login.close()

def mostrar_interface_admin():
    notebook.tab(1, state="normal")  # Mostrar a aba de Admin
    carregar_dados_desenvolvedores()

def carregar_dados_desenvolvedores():
    conn_desenvolvedores = sqlite3.connect('desenvolvedores.db')
    cursor_desenvolvedores = conn_desenvolvedores.cursor()

    cursor_desenvolvedores.execute("SELECT * FROM desenvolvedores")
    dados = cursor_desenvolvedores.fetchall()

    tabela = ttk.Treeview(admin_frame, columns=("id", "Nome", "Idade", "Cidade", "Estado", "Telefone", "Email", "Experiência", "Soft Skills", "Status", "Linkedin", "Expectativa Salarial"))
    
    tabela.heading("#1", text="id")
    tabela.heading("#2", text="Nome")
    tabela.heading("#3", text="Idade")
    tabela.heading("#4", text="Cidade")
    tabela.heading("#5", text="Estado")
    tabela.heading("#6", text="Telefone")
    tabela.heading("#7", text="Email")
    tabela.heading("#8", text="Experiência")
    tabela.heading("#9", text="Soft Skills")
    tabela.heading("#10", text="Status")
    tabela.heading("#11", text="Linkedin")
    tabela.heading("#12", text="Expectativa Salarial")

    tabela.pack()

    for dado in dados:
        tabela.insert('', 'end', values=dado)
    
    scrollbar_x = ttk.Scrollbar(admin_frame, orient="horizontal", command=tabela.xview)
    tabela.configure(xscrollcommand=scrollbar_x.set)

    tabela.pack()
    scrollbar_x.pack(fill="x")

    conn_desenvolvedores.close()

root = tk.Tk()
root.title("Search Tech")

root.grid_rowconfigure(0, weight=2)
root.columnconfigure(0, weight=2)
root.configure(bg='#4682B4')

label_bem_vindo = tk.Label(root, text="Search Tech", font=("Aptos bold", 20), bg='#FF6347', foreground='white')
label_bem_vindo.pack(pady=20)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, pady=250, padx=200)

# Aba de login
login_frame = ttk.Frame(notebook)
notebook.add(login_frame, text="Login")

label_usuario = tk.Label(login_frame, text="Usuário:")
label_usuario.pack()
entry_usuario = tk.Entry(login_frame)
entry_usuario.pack()

label_senha = tk.Label(login_frame, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(login_frame, show="*")  # Para ocultar a senha
entry_senha.pack()

btn_login = tk.Button(login_frame, text="Login", command=fazer_login, padx=20)
btn_login.pack()

# Aba de Admin (inicialmente oculta)
admin_frame = ttk.Frame(notebook)
notebook.add(admin_frame, text="Admin")
notebook.tab(1, state="hidden")  # Ocultar a aba de Admin no início

root.mainloop()
