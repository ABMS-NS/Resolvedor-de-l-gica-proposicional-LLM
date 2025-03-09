from gemini import Gemini
from qwen import Qwen 
from deepseek import DeepSeek
import sys


n_sentencas = input("Digite o número de sentenças que existem no seu problema: ")
print("Digite as sentenças (pressione Ctrl+D para finalizar):\nEx:\nA: Chuva\nB: Rua Molhada\nC: Rua Escorregadia\n")
sentencas = sys.stdin.read().strip()
print("Digite o problema utilizando quebra de linha para separar cada sentença e o número da mesma na frente (pressione Ctrl+D para finalizar): \nEx:\n1-A → B\n2-B → C\n3-A\n")
problema = sys.stdin.read().strip()

resposta = Gemini.resolvedor(n_sentencas,sentencas,problema)

avaliacao_qwen = Qwen.avaliadorbinario(resposta)
avaliacao_ds = DeepSeek.avaliadorbinario(resposta)

print ("Resposta: ",resposta)
print("Avaliação Qwen: ",avaliacao_qwen)
print("Avaliação DeepSeek: ",avaliacao_ds)
