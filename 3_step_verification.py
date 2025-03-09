from gemini import Gemini
from qwen import Qwen 
from deepseek import DeepSeek
import sys

# nessa main será realizado o processo da votação das respostas da LLM e a contagem dos votos
# e a exibição do resultado
n_sentencas = input("Digite o número de sentenças que existem no seu problema: ")
print("Digite as sentenças (pressione Ctrl+D para finalizar):\nEx:\nA: Chuva\nB: Rua Molhada\nC: Rua Escorregadia\n")
sentencas = sys.stdin.read().strip()
print("Digite o problema utilizando quebra de linha para separar cada sentença e o número da mesma na frente (pressione Ctrl+D para finalizar): \nEx:\n1-A → B\n2-B → C\n3-A\n")
problema = sys.stdin.read().strip()


answers = []
answers.append(Gemini.resolvedor(n_sentencas,sentencas,problema))
answers.append(Qwen.resolvedor(n_sentencas,sentencas,problema))
answers.append(DeepSeek.resolvedor(n_sentencas,sentencas,problema))


# colocação dos votos
votes = []

votes.append(Gemini.avaliador(answers[1],answers[2]))
votes.append(Qwen.avaliador(answers[0],answers[2]))
votes.append(DeepSeek.avaliador(answers[0],answers[1]))

if (votes[1] == 0 and votes [2] == 0):
    print(answers[0])
elif (votes[0] == 1 and votes [2] == 1):
    print(answers[1])
elif (votes[0] == 2 and votes [1] == 2):
    print(answers[2])
else:
    print("Não foi possível determinar uma resposta satisfatível")


