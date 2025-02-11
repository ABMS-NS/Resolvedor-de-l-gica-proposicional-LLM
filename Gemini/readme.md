# Resolvedor de Problemas Lógicos com Gemini AI

Este projeto utiliza a API Gemini da Google para resolver problemas lógicos baseados em sentenças proposicionais. O usuário fornece sentenças e regras lógicas, e o modelo retorna a solução explicada.

## Requisitos

- Python 3.8+
- Conta no Google AI Studio para acesso à API Gemini
- Biblioteca `google-generativeai`

## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/resolvedor-logico.git
   cd resolvedor-logico
   ```
2. Instale as dependências:
   ```sh
   pip install google-generativeai
   ```
3. Configure sua chave de API Gemini substituindo `GOOGLE_API_KEY` no arquivo `gemini.py`.

## Como Usar

1. Execute o script `main.py`:
   ```sh
   python main.py
   ```
2. Insira o número de sentenças.
3. Digite as sentenças no formato:
   ```
   A: Chuva
   B: Rua Molhada
   C: Rua Escorregadia
   ```
4. Digite o problema lógico no formato:
   ```
   1-A → B
   2-B → C
   3-A
   ```
5. O programa enviará os dados para a API Gemini e exibirá a solução.

## Estrutura do Projeto
```
resolvedor-logico/
├── main.py       # Interface de entrada do usuário
├── gemini.py     # Classe para interagir com a API Gemini
└── README.md     # Documentação do projeto
```

## Observação
- Certifique-se de não compartilhar sua chave de API publicamente.
- A precisão das respostas depende da capacidade do modelo AI.

## Licença
Este projeto está sob a licença MIT.

