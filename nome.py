import tkinter as gui

janela = gui.Tk()

def intrudizirNome() :
    name = nome.get()
    boasVindas["text"] = f"oi {name}"


boasVindas = gui.Label(janela, text="nome")
boasVindas.pack()

nome = gui.Entry(janela)
nome.pack()
gui.Button(janela, text='submeter',command=intrudizirNome).pack()

janela.mainloop()