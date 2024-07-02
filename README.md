# Gerador de Links UTM

Este projeto é um gerador de links UTM desenvolvido em Python, utilizando a biblioteca Tkinter para criar uma interface gráfica amigável. O objetivo deste projeto é facilitar a geração de links UTM para tracking de campanhas de email marketing, permitindo que o usuário selecione parâmetros como data de disparo, medium, tipo de campanha e marca.

## Funcionalidades

- Seleção de data de disparo através de um calendário.
- Escolha entre "Email" e "SMS" para o campo "Medium" usando botões de rádio.
- Seleção do tipo de campanha através de um menu dropdown, com a opção "Outros" que abre um campo de texto para entrada personalizada.
- Seleção de marcas através de um menu dropdown.
- Geração do link UTM com base nos parâmetros fornecidos.
- Cópia automática do link UTM gerado para a área de transferência do usuário.

## Tecnologias Utilizadas

- Python
- Tkinter
- tkcalendar
- pyperclip

## Instalação

1. Clone o repositório para sua máquina local:
    ```sh
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd nome-do-repositorio
    ```
3. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
4. Instale as dependências necessárias:
    ```sh
    pip install tkcalendar pyperclip
    ```

## Uso

Execute o script Python para abrir a interface gráfica do gerador de links UTM:
```sh
python gerador_utm.py
