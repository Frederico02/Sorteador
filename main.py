import random
import tkinter as tk
from PIL import Image, ImageTk
import os

integrantes = ["LUCAS", "LUCIANA", "KEL", "DANIEL", "LUIZ", "WESLEY", "BRUNA", "DIEGO"]

def sortear():
    sorteado = random.choice(integrantes)
    resultado_label.configure(text=sorteado)

    imagem_path = f"Q:/Lucas/Imagens/{sorteado}.png"
    imagem = Image.open(imagem_path)
    imagem = imagem.resize((200, 200), Image.LANCZOS)

    imagem_tk = ImageTk.PhotoImage(imagem)
    imagem_label.configure(image=imagem_tk)
    imagem_label.image = imagem_tk # armazenar uma referência à imagem para evitar que seja coletada pelo garbage collector

def encerrar():
    janela.destroy()

janela = tk.Tk()
janela.geometry("450x500")
janela.title("Sorteio Sala")

titulo_label = tk.Label(janela, text="Sortear Integrante")
titulo_label.pack(pady=20)

sortear_button = tk.Button(janela, text="Sortear", command=sortear)
sortear_button.pack(pady=10)

imagem_label = tk.Label(janela)
imagem_label.pack(pady=20)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=20)

botao_sair = tk.Button(janela, text="Encerrar programa", command=janela.quit)
botao_sair.pack(side=tk.BOTTOM, pady=25)

# Define o caminho do arquivo de imagem do ícone
caminho_icone = "Q:/Lucas/Imagens/icon.ico"

# Define o ícone da janela do Tkinter
janela.iconbitmap(caminho_icone)

janela.mainloop()
