# WEB SCRAPER

Este projeto é um web scraper para baixar redações do portal Professor24h e fazer o upload para uma pasta específica no Google Drive.

## Configuração

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu-usuario/MyWebScraper.git
    cd MyWebScraper
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure as credenciais da API do Google Drive:
    - Baixe o arquivo `credentials.json` e coloque-o no diretório raiz do projeto.

## Uso

Execute o script principal:
```sh
python main.py
