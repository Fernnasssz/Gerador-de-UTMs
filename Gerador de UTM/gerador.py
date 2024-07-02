import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import pyperclip

# Função para gerar o link UTM e copiá-lo para a área de transferência
def generate_utm_link():
    date = date_entry.get()
    medium = medium_var.get()
    campaign_type = campaign_var.get()
    if campaign_type == "Outros":
        campaign_type = custom_campaign_entry.get()
    brand = brand_var.get()
    
    utm_link = f"?utm_source=mmkt&utm_medium={medium}&utm_campaign={date}-{campaign_type}-{brand}"
    result_label.config(text=utm_link)
    
    # Copiar o link para a área de transferência
    pyperclip.copy(utm_link)

# Criando a janela principal
root = tk.Tk()
root.title("Gerador de Links UTM")

# Campo de data
tk.Label(root, text="Data do Disparo:").grid(row=0, column=0, padx=10, pady=10)
date_entry = DateEntry(root, date_pattern='yyyy-mm-dd')
date_entry.grid(row=0, column=1, padx=10, pady=10)

# Campo de medium (email ou sms)
tk.Label(root, text="Medium:").grid(row=1, column=0, padx=10, pady=10)
medium_var = tk.StringVar()
tk.Radiobutton(root, text="Email", variable=medium_var, value="email").grid(row=1, column=1, sticky=tk.W)
tk.Radiobutton(root, text="SMS", variable=medium_var, value="sms").grid(row=1, column=2, sticky=tk.W)
medium_var.set("email")  # Valor padrão

# Campo de campaign
tk.Label(root, text="Tipo de Campanha:").grid(row=2, column=0, padx=10, pady=10)
campaign_var = tk.StringVar()
campaign_options = ["Novos", "Seminovos", "Pos-venda", "Servico", "Evento", "Outros"]
campaign_dropdown = ttk.Combobox(root, textvariable=campaign_var, values=campaign_options, state='readonly')
campaign_dropdown.grid(row=2, column=1, padx=10, pady=10)
campaign_var.set("Novos")  # Valor padrão

# Campo customizado para campaign (aparece apenas se "Outros" for selecionado)
custom_campaign_entry = tk.Entry(root)
def update_custom_campaign_entry(*args):
    if campaign_var.get() == "Outros":
        custom_campaign_entry.grid(row=3, column=1, padx=10, pady=10)
    else:
        custom_campaign_entry.grid_forget()
campaign_var.trace('w', update_custom_campaign_entry)

# Campo de brand
tk.Label(root, text="Marca:").grid(row=4, column=0, padx=10, pady=10)
brand_var = tk.StringVar()
brand_options = ["Honda", "Nissan", "Vw", "VWCO", "Triumph", "RioHD", "BHHD", "Volvo", "BYD", "Mercedes", "GrupoAB"]
brand_dropdown = ttk.Combobox(root, textvariable=brand_var, values=brand_options, state='readonly')
brand_dropdown.grid(row=4, column=1, padx=10, pady=10)
brand_var.set("Honda")  # Valor padrão

# Botão para gerar o link UTM
generate_button = tk.Button(root, text="Gerar Link UTM", command=generate_utm_link)
generate_button.grid(row=5, column=0, columnspan=2, pady=20)

# Label para exibir o link gerado
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Iniciando o loop da interface
root.mainloop()
