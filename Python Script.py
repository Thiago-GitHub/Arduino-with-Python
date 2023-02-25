from tkinter import *
from tkinter import messagebox

import serial

porta = "COM5"
velocidade = 9600
ser = serial.Serial(porta, velocidade);

def ligar():
    ser.write(b'1')

def desligar():
    ser.write(b'0')

janela = Tk()
janela.title("Ligar e desligar LED")
janela.geometry("300x300")

botao1 = Button(janela, width=20, text="Ligar", command=ligar)
botao1.place(x=77, y=70)

botao2 = Button(janela, width=20, text="Desligar", command=desligar)
botao2.place(x=77, y=100)

janela.mainloop()

ser.close()

