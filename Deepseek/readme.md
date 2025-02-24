# DeepSeek Logical Solver

Este projeto utiliza a API do DeepSeek para resolver problemas lógicos baseados em sentenças proposicionais fornecidas pelo usuário.

## Funcionalidade

O script `main.py` solicita ao usuário um conjunto de sentenças e um problema lógico baseado nessas sentenças. Em seguida, a API do DeepSeek é acionada para processar e resolver o problema.

## Estrutura do Projeto

```
/
|-- main.py           # Script principal que captura entrada do usuário e aciona a API
|-- deepseek.py       # Classe DeepSeek que se comunica com a API para processar a lógica
|-- README.md         # Documentação do projeto
```

## Como Usar

1. **Instale as dependências**:
   
   O projeto requer a biblioteca `requests` para fazer chamadas à API. Instale-a com:
   ```sh
   pip install requests
   ```

2. **Configure sua chave de API**:
   
   No arquivo `deepseek.py`, substitua `API_KEY` por sua chave de API válida.
   
3. **Execute o script**:
   ```sh
   python main.py
   ```
   
   O programa solicitará:
   - O número de sentenças do problema.
   - As sentenças proposicionais.
   - O problema lógico a ser resolvido.

   Digite `FIM` para finalizar a entrada de dados.

4. **Aguarde a resposta**:
   
   O DeepSeek processará o problema e retornará a solução com uma explicação.

## Exemplo de Entrada e Saída

**Entrada:**
```
Digite o número de sentenças que existem no seu problema: 3
Digite as sentenças (digite 'FIM' para finalizar):
A: Chuva
B: Rua Molhada
C: Rua Escorregadia
FIM
Agora, digite o problema utilizando quebra de linha para separar cada sentença:
1-A → B
2-B → C
3-A
FIM
```

**Saída esperada:**
```
Gerando resposta...
Resposta do DeepSeek:
Se A é verdadeira (Chuva), então B também é verdadeira (Rua Molhada). Se B é verdadeira, então C também é verdadeira (Rua Escorregadia). Logo, C é verdadeira.
```

## Observações
- Caso ocorra um erro na API, o código exibirá a mensagem de erro.
- A temperatura do modelo está definida como `0.7` para permitir um equilíbrio entre criatividade e previsibilidade.
