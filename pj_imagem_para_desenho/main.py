from tkinter import *
from tkinter import Tk, ttk, filedialog
from PIL import ImageTk, ImageTk, Image, ImageEnhance
import cv2

#Cores
co0 = "#000000" 
co1 = "#ffffff" 
co2 = "#00ff00" 
co3 = "#37465b" 
co4 = "#403a3a" 
co5 = "#f05534" 
co6 = "#028bfb" 
# Cores do modo escuro
bg_color = "#1e1e1e"  # Fundo escuro
fg_color = "#ffffff"  # Texto branco
accent_color = "#007acc"  # Azul
button_color = "#252526"  # Cinza escuro

# Criando a janela principal
janela = Tk()
janela.title("Conversor de Esboço a Lápis")
janela.geometry('500x600')
janela.configure(background=bg_color)
janela.resizable(width=FALSE, height=FALSE)

#Criando Interface Gráfica
frame_topo = Frame(janela, width=500, height=60, bg=bg_color)
frame_topo.grid(row=0, column=0, pady=5)

frame_previsao = Frame(janela, width=500, height=240, bg=bg_color)
frame_previsao.grid(row=1, column=0, pady=5)

frame_controles = Frame(janela, width=500, height=260, bg=bg_color)
frame_controles.grid(row=2, column=0, pady=5)



#Escolher a imagem
def escolher_imagem():
    global imagem_original
    caminho = filedialog.askopenfilename()
    if caminho:
        imagem_original = Image.open(caminho)
        previsualizacao = imagem_original.resize((200, 200))
        previsualizacao = ImageTk.PhotoImage(previsualizacao)
        label_original.config(image=previsualizacao)
        label_original.image = previsualizacao

# Converter imagem    
def converter_imagem():
    global imagem_original, imagem_convertida

    if imagem_original is None:
        return

    intensidade = escala_intensidade.get()
    brilho = escala_brilho.get() / 100
    contraste = escala_contraste.get() / 100

    imagem_cv = cv2.cvtColor(cv2.imread(imagem_original.filename), cv2.COLOR_BGR2GRAY)
    desfoque = cv2.GaussianBlur(imagem_cv, (21, 21), 0)
    esboco = cv2.divide(imagem_cv, desfoque, scale=intensidade)

    esboco_pil = Image.fromarray(esboco)
    esboco_pil = ImageEnhance.Brightness(esboco_pil).enhance(brilho)
    esboco_pil = ImageEnhance.Contrast(esboco_pil).enhance(contraste)

    imagem_convertida = esboco_pil
    previsualizacao = imagem_convertida.resize((200, 200))
    previsualizacao = ImageTk.PhotoImage(previsualizacao)
    label_convertida.config(image=previsualizacao)
    label_convertida.image = previsualizacao
    
#Salvar Imagem
def salvar_imagem():
    if imagem_convertida:
        caminho = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if caminho:
            imagem_convertida.save(caminho)
            


# Título
titulo = Label(frame_topo, text="Conversor de imagem", font=("Arial", 16, "bold"), bg=bg_color, fg=fg_color)
titulo.pack()

# Previsões
label_original = Label(frame_previsao, text="Imagem Original", bg=bg_color, fg=fg_color, font=("Arial", 12))
label_original.place(x=50, y=10)

label_convertida = Label(frame_previsao, text="Esboço Convertido", bg=bg_color, fg=fg_color, font=("Arial", 12))
label_convertida.place(x=280, y=10)

# Controles
ttk.Label(frame_controles, text="Intensidade", background=bg_color, foreground=fg_color).place(x=10, y=10)
escala_intensidade = Scale(frame_controles, from_=50, to=300, command=lambda x: converter_imagem(), orient=HORIZONTAL, length=300, bg=bg_color, fg=fg_color)
escala_intensidade.set(120)
escala_intensidade.place(x=10, y=30)

# Brilho
ttk.Label(frame_controles, text="Brilho", background=bg_color, foreground=fg_color).place(x=10, y=80)
escala_brilho = Scale(frame_controles, from_=50, to=200, command=lambda x: converter_imagem(), orient=HORIZONTAL, length=300, bg=bg_color, fg=fg_color)
escala_brilho.set(100)
escala_brilho.place(x=10, y=100)

# Contraste
ttk.Label(frame_controles, text="Contraste", background=bg_color, foreground=fg_color).place(x=10, y=150)
escala_contraste = Scale(frame_controles, from_=50, to=200, command=lambda x: converter_imagem(), orient=HORIZONTAL, length=300, bg=bg_color, fg=fg_color)
escala_contraste.set(100)
escala_contraste.place(x=10, y=170)

# Adicionando Botões
botao_escolher = Button(janela, text="Escolher Imagem", command=escolher_imagem, bg=button_color, fg=fg_color, font=("Arial", 10), width=15)
botao_escolher.place(x=30, y=540)

botao_converter = Button(janela, text="Converter", command=converter_imagem, bg=accent_color, fg=fg_color, font=("Arial", 10), width=15)
botao_converter.place(x=190, y=540)

botao_salvar = Button(janela, text="Salvar Imagem", command=salvar_imagem, bg=button_color, fg=fg_color, font=("Arial", 10), width=15)
botao_salvar.place(x=350, y=540)

janela.mainloop()



#Desenvolvido por Adriano Pereira Silva