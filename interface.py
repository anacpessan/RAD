import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sqlite3
from tkinter.ttk import Button, Entry, Radiobutton
    
    
def salvar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    experiencia = entry_experiencia.get()
    soft_skills = entry_soft_skills.get()
    status = entry_status.get()
    linkedin = entry_linkedin.get()
    expectativa_salario = entry_expectativa_salario.get()

    # Salvar o currículo como um blob
    curriculo = None
    curriculo_path = btn_curriculo["text"]
    if curriculo_path != "Carregar Currículo":
        with open(curriculo_path, 'rb') as file:
            curriculo = file.read()

    conn = sqlite3.connect('desenvolvedores.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO desenvolvedores (nome, idade, cidade, estado, telefone, email, experiencia, soft_skills, status, linkedin, expectativa_salario,  curriculo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nome, idade, cidade, estado, telefone, email, experiencia, soft_skills, status, linkedin, expectativa_salario,  curriculo))
    conn.commit()

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_experiencia.set(0)
    entry_soft_skills.delete(0, tk.END)
    entry_status.set(1)
    entry_linkedin.delete(0, tk.END)
    entry_expectativa_salario.delete(0, tk.END)
    btn_curriculo.config(text="Carregar Currículo")

    print("Dados salvos com sucesso!")

def carregar_curriculo():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos PDF/Word", "*.pdf;*.docx")])
    if file_path:
        btn_curriculo.config(text=file_path)
    else:
        print("Nenhum arquivo selecionado.")

root = tk.Tk()
root.title("Search Tech")

root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.configure(bg='#4682B4')

titulo_label = tk.Label(root, text="Search Tech", font=("Aptos 50 bold"), bg='#FF6347', foreground='white')
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

btn_admin = tk.Button(root, text="Administrador", bg='#FF6347', fg='white', font=("bold"), borderwidth=3, relief="groove")
btn_admin.place(x=10, y=10)

def criar_interface(root): # Chame a função criar_interface, passando a janela 'root'
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    frame_candidatos = ttk.Frame(notebook)
    notebook.add(frame_candidatos, text="Candidatos")

def criar_frame_com_moldura(root, titulo, row):
    frame = tk.Frame(root, bd=5, relief=tk.GROOVE)
    frame.grid(row=row, column=0, sticky="ew", padx=10, pady=10)

    subtitulo = tk.Label(frame, text=titulo, font=("Helvetica 14 bold"), justify="left")
    subtitulo.grid(row=0, column=0, sticky="w", columnspan=2, pady=10)

    return frame

frame_info_pessoais = criar_frame_com_moldura(root, "Informações Pessoais", 1)
frame_localizacao = criar_frame_com_moldura(root, "Localização", 2)
frame_info_contato = criar_frame_com_moldura(root, "Informações de Contato", 3)
frame_experiencia = criar_frame_com_moldura(root, "Experiência Profissional", 4)
frame_curriculo = criar_frame_com_moldura(root, "Currículo", 5)

# Labels e entradas
label_nome = tk.Label(frame_info_pessoais, text="Nome:")
label_nome.grid(row=1, column=0, sticky="ew")
entry_nome = Entry(frame_info_pessoais)
entry_nome.grid(row=1, column=1, sticky="w", padx=10, pady=1)

label_idade = tk.Label(frame_info_pessoais, text="Idade:")
label_idade.grid(row=2, column=0, sticky="w")
entry_idade = Entry(frame_info_pessoais)
entry_idade.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

label_cidade = tk.Label(frame_localizacao, text="Cidade:")
label_cidade.grid(row=1, column=0, sticky="w")
entry_cidade = Entry(frame_localizacao)
entry_cidade.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

label_estado = tk.Label(frame_localizacao, text="Estado:")
label_estado.grid(row=2, column=0, sticky="w")
entry_estado = Entry(frame_localizacao)
entry_estado.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

label_telefone = tk.Label(frame_info_contato, text="Telefone:")
label_telefone.grid(row=1, column=0, sticky="w")
entry_telefone = Entry(frame_info_contato)
entry_telefone.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

label_email = tk.Label(frame_info_contato, text="E-mail:")
label_email.grid(row=2, column=0, sticky="w")
entry_email = Entry(frame_info_contato)
entry_email.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

label_experiencia = tk.Label(frame_experiencia, text="Possui experiência profissional?")
label_experiencia.grid(row=1, column=0, sticky="w", columnspan=2)
entry_experiencia = tk.IntVar()
entry_experiencia_sim = Radiobutton(frame_experiencia, text='Sim', variable=entry_experiencia, value=1)
entry_experiencia_sim.grid(row=2, column=0, sticky="w", padx=10)
entry_experiencia_nao = Radiobutton(frame_experiencia, text='Não', variable=entry_experiencia, value=0)
entry_experiencia_nao.grid(row=2, column=1, sticky="w", padx=10)

label_soft_skills = tk.Label(frame_experiencia, text="Soft Skills:")
label_soft_skills.grid(row=3, column=0, sticky="w")
entry_soft_skills = Entry(frame_experiencia)
entry_soft_skills.grid(row=3, column=1, sticky="ew", padx=10, pady=10)

label_status = tk.Label(frame_experiencia, text="Status:")
label_status.grid(row=4, column=0, sticky="w", columnspan=2)
entry_status = tk.IntVar()
entry_status.set(1)
entry_status_empregado = Radiobutton(frame_experiencia, text='Empregado', variable=entry_status, value=1)
entry_status_empregado.grid(row=5, column=0, sticky="w", padx=10)
entry_status_open = Radiobutton(frame_experiencia, text='Open to Work', variable=entry_status, value=2)
entry_status_open.grid(row=5, column=1, sticky="w", padx=10)

label_expectativa_salario = tk.Label(frame_experiencia, text="Qual sua expectativa salarial?")
label_expectativa_salario.grid(row=6, column=0, sticky="w")
entry_expectativa_salario = Entry(frame_experiencia)
entry_expectativa_salario.grid(row=6, column=1, sticky="ew", padx=10, pady=10)

label_linkedin = tk.Label(frame_curriculo, text="Linkedin:")
label_linkedin.grid(row=7, column=0, sticky="w")
entry_linkedin = Entry(frame_curriculo)
entry_linkedin.grid(row=7, column=1, sticky="ew", padx=10, pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.grid(row=8, column=0, columnspan=2, pady=10)

btn_curriculo = Button(frame_curriculo, text="Carregar Currículo", command=carregar_curriculo)
btn_curriculo.grid(row=9, column=0, columnspan=2, sticky="ew", padx=0, pady=1)

btn_submit = Button(frame_buttons, text="Enviar", command=salvar_dados)
btn_submit.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

root.mainloop()
