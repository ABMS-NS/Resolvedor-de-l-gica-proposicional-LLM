from gemini import Gemini
from qwen import Qwen
from deepseek import DeepSeek

#scan the logical problem for the best
problem = input("Enter the problem: ")

#resolve the problem with Gemini
resolution = DeepSeek.resolver(problem)

#appraise the resolution with Qwen and DeepSeek
appraisal_qwen = Qwen.appraiser(resolution)
appraisal_gemini = Gemini.appraiser(resolution)

#display the resolution and appraisals
print(f"{resolution}\n------------------------------------------------------------\n")
print(f"Qwen: {appraisal_qwen}\n------------------------------------------------------------\n")
print(f"Gemini: {appraisal_gemini}\n------------------------------------------------------------\n")
