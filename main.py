import tkinter as tk
from tkinter import messagebox

# Variáveis globais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


# Funções de ação
def depositar():
    global saldo, extrato
    try:
        valor = float(entrada_valor.get())
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            atualizar_saldo()
            messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
        else:
            messagebox.showwarning("Erro", "O valor informado é inválido.")
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um valor válido.")
    entrada_valor.delete(0, tk.END)


def sacar():
    global saldo, extrato, numero_saques
    try:
        valor = float(entrada_valor.get())
        if valor > 0:
            if valor > saldo:
                messagebox.showwarning("Erro", "Saldo insuficiente.")
            elif valor > limite:
                messagebox.showwarning("Erro", "O valor do saque excede o limite.")
            elif numero_saques >= LIMITE_SAQUES:
                messagebox.showwarning("Erro", "Número máximo de saques excedido.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                atualizar_saldo()
                messagebox.showinfo("Sucesso", "Saque realizado com sucesso!")
        else:
            messagebox.showwarning("Erro", "O valor informado é inválido.")
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um valor válido.")
    entrada_valor.delete(0, tk.END)


def exibir_extrato():
    global extrato
    extrato_str = extrato if extrato else "Não foram realizadas movimentações."
    messagebox.showinfo("Extrato", f"{extrato_str}\n\nSaldo: R$ {saldo:.2f}")


def atualizar_saldo():
    label_saldo["text"] = f"Saldo: R$ {saldo:.2f}"


def sair():
    janela.quit()


janela = tk.Tk()
janela.title("Sistema de Caixa")
janela.geometry("400x300")

label_titulo = tk.Label(janela, text="Controle de Caixa", font=("Arial", 16, "bold"))
label_titulo.pack(pady=10)

label_saldo = tk.Label(janela, text=f"Saldo: R$ {saldo:.2f}", font=("Arial", 14))
label_saldo.pack(pady=5)

label_valor = tk.Label(janela, text="Valor:", font=("Arial", 12))
label_valor.pack(pady=5)

entrada_valor = tk.Entry(janela, width=20, font=("Arial", 12))
entrada_valor.pack(pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_depositar = tk.Button(frame_botoes, text="Depositar", command=depositar, width=10)
botao_depositar.grid(row=0, column=0, padx=5)

botao_sacar = tk.Button(frame_botoes, text="Sacar", command=sacar, width=10)
botao_sacar.grid(row=0, column=1, padx=5)

botao_extrato = tk.Button(
    frame_botoes, text="Extrato", command=exibir_extrato, width=10
)
botao_extrato.grid(row=1, column=0, padx=5, pady=5)

botao_sair = tk.Button(frame_botoes, text="Sair", command=sair, width=10)
botao_sair.grid(row=1, column=1, padx=5, pady=5)

# Janela
janela.mainloop()
