from customtkinter import *
from random import randint

try:
    app = CTk()
    app.title("Jogo do número secreto")
    app.geometry("500x300")
    set_appearance_mode("dark")
    numero_secreto = 0
    tentativas = 0

    def restart_program():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def iniciar():
        global tentativas
        global numero_secreto
        numero_secreto = randint(1, 100)
        tentativas = 0

        def fazer_palpite():
            global tentativas
            tentativas += 1
            valor_palpite = palpite.get()
            valor_palpite = int(valor_palpite)

            contador_tentativas.configure(text=f'Tentativas: {tentativas}')

            if valor_palpite == numero_secreto:
                palpite_text.configure(text=f'Parabéns! Você acertou o número secreto com {tentativas} tentativas')
                botao_chute.configure(text='Tentar novamente', command=restart_program)
            elif valor_palpite > numero_secreto:
                palpite_text.configure(text=f'Quase lá, o número secreto é menor que {valor_palpite}')
            elif valor_palpite < numero_secreto:
                palpite_text.configure(text=f'Quase lá, o número secreto é maior que {valor_palpite}')

        titulo = CTkLabel(app, text='JOGO DO NÚMERO SECRETO:', text_color='#fff')
        titulo.pack(padx=10, pady=20)

        contador_tentativas = CTkLabel(app, text=f'Tentativas: {tentativas}', text_color='#fff')
        contador_tentativas.pack(padx=10, pady=0)

        palpite = CTkEntry(app, placeholder_text='Chute um número de 1 a 100', text_color='#000', placeholder_text_color='#000', fg_color='#fff', width=177)
        palpite.pack(padx=10, pady=10)

        palpite_text = CTkLabel(app, text='', text_color='#fff')
        palpite_text.pack(padx=10, pady=10)

        botao_chute = CTkButton(app, text='Chutar!', text_color='#fff', command=fazer_palpite)
        botao_chute.pack(padx=10, pady=10)

    iniciar()

    app.mainloop()
except KeyboardInterrupt:
    print('Programa finalizado por ação externa')
