from gemini import Gemini
from qwen import Qwen 
from deepseek import DeepSeek

#scan the logical problem for the best
problem = input("Enter the problem: ")

#resolve the problem with Gemini
resolution = Qwen.resolver(problem)

#appraise the resolution with Qwen and DeepSeek
appraisal_gemini = Gemini.appraiser(resolution)
appraisal_ds = DeepSeek.appraiser(resolution)

#display the resolution and appraisals
print(f"{resolution}\n------------------------------------------------------------\n")
print(f"Qwen: {appraisal_gemini}\n------------------------------------------------------------\n")
print(f"DeepSeek: {appraisal_ds}\n------------------------------------------------------------\n")
