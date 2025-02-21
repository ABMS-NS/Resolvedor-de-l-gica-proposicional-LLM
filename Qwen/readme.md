# Resolvedor de Problemas Lógicos com Qwen AI

Este projeto utiliza a API **Qwen** da Alibaba Cloud para resolver problemas lógicos baseados em sentenças proposicionais. O usuário fornece sentenças e regras lógicas, e o modelo retorna a solução explicada passo a passo.

---

## Requisitos

- Python 3.8+
- Conta na Alibaba Cloud para acesso à API Qwen
- Bibliotecas necessárias: `openai`, `psutil`, `dotenv`
- Arquivo `.env` configurado com sua chave de API Qwen

---

## Instalação

1. **Clone este repositório**:
   ```
   git clone https://github.com/seu-usuario/resolvedor-logico-qwen.git
   cd resolvedor-logico-qwen


   Instale as dependências :

   pip install openai psutil python-dotenv


   Configure sua chave de API Qwen :
Crie um arquivo .env no diretório raiz do projeto.
Adicione sua chave de API Qwen ao arquivo .env


DASHSCOPE_API_KEY=sua_chave_de_api_aqui

Execute o script principal :

python main.py

Como Usar
Insira o número de sentenças :
O programa solicitará o número de sentenças que você deseja fornecer.

Digite as sentenças no formato :

A: O aluno estudou
B: O aluno obteve uma boa nota
C: O aluno foi aprovado

Digite o problema lógico no formato :

1-A → B
2-B → C
3-A

Conclusão desejada :

Prove que o aluno foi aprovado (C).

O programa enviará os dados para a API Qwen :
O modelo processará as informações e retornará uma explicação detalhada da solução.
Avalie a resposta :
Após a execução, o programa perguntará se a resposta está correta (S/N) para fins de registro.

resolvedor-logico-qwen/
├── main.py       # Interface de entrada do usuário
├── qwen.py       # Classe para interagir com a API Qwen
├── .env          # Arquivo de configuração para a chave de API
├── metrics.csv   # Registro das métricas de cada execução
├── metrics.txt   # Registro detalhado das respostas e prompts
└── README.md     # Documentação do projeto


Funcionalidades Principais
Resolução Lógica :
O programa resolve problemas de lógica proposicional usando regras de inferência (Modus Ponens, Modus Tollens, etc.) e equivalências lógicas (Dupla Negação, De Morgan, etc.).
Chain of Thought (CoT) :
O modelo explica cada passo do raciocínio, facilitando o entendimento do processo lógico.
Monitoramento de Métricas :
O programa registra métricas como tempo de resposta, uso de CPU, uso de memória, latência da rede e tokens utilizados.
Avaliação de Respostas :
Após cada execução, o usuário pode avaliar se a resposta gerada está correta ou incorreta. Essa avaliação é salva nos arquivos metrics.csv e metrics.txt.


Exemplo de Saída
Prompt
### Contexto
Você é um tutor especializado em lógica proposicional. Explique de forma clara e concisa.
### Objetivo
Resolva o problema usando:
- Regras de Inferência: Modus Ponens, Modus Tollens, etc.
- Regras de Equivalência: Dupla Negação, De Morgan, etc.
Use Chain of Thought (CoT) para decompor o problema.
### Sentenças
A: O aluno estudou
B: O aluno obteve uma boa nota
C: O aluno foi aprovado
### Problema
1-A → B
2-B → C
3-A
Conclusão desejada: Prove que o aluno foi aprovado (C).



===
- Passo 1: Da premissa 3, temos que $ A $ é verdadeira.
- Passo 2: Da premissa 1 ($ A \rightarrow B $) e do fato de que $ A $ é verdadeira, aplicamos **Modus Ponens** para concluir que $ B $ é verdadeira.
- Passo 3: Da premissa 2 ($ B \rightarrow C $) e do fato de que $ B $ é verdadeira, aplicamos novamente **Modus Ponens** para concluir que $ C $ é verdadeira.
- Conclusão: Com base nas premissas fornecidas e nas regras de inferência aplicadas, provamos que $ C $ (O aluno foi aprovado).
===


Observações
Certifique-se de não compartilhar sua chave de API publicamente.
A precisão das respostas depende da capacidade do modelo Qwen.
Para problemas mais complexos, ajuste o parâmetro max_tokens no arquivo qwen.py para permitir respostas mais longas.
Licença
Este projeto está sob a licença MIT.


