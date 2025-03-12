import textwrap
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class Qwen:
   
    @staticmethod
    def to_markdown_terminal(text):
        # Remove delimitadores LaTeX desnecessários
        text = text.replace('$', '')  
        text = text.replace(r'\(', '').replace(r'\)', '')  
        text = text.replace(r'\boxed{', '(').replace('}', ')')  

        # Substitui símbolos LaTeX por equivalentes legíveis
        text = text.replace('\\neg', '¬')  
        text = text.replace('\\lor', '∨') 
        text = text.replace('\\land', '∧')  
        text = text.replace('\\to', '→')  
        text = text.replace('\\rightarrow', '→')  
        text = text.replace('\\leftrightarrow', '↔')  
        text = text.replace('•', '*') 

        # Adiciona quebras de linha adequadas para Markdown
        text = text.replace("###", "\n###")  
        text = text.replace("====", "\n====\n")  

        # Remove espaços extras e adiciona indentação para melhor visualização
        return textwrap.indent(text.strip(), '> ')

    # Obtém a resposta do modelo Qwen através da API OpenAI
    @staticmethod
    def get_response(prompt: str):
        client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
        )
        try:
            # Chamada à API
            completion = client.chat.completions.create(
                model="qwen-max",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Você é um tutor especializado em lógica proposicional. Ajude estudantes a resolver problemas usando regras de inferência (Modus Ponens, Modus Tollens, etc.) "
                            "e equivalências (Dupla Negação, De Morgan, etc.). Explique passo a passo de forma clara e concisa, justificando cada etapa com base nas regras aplicadas."
                        )
                    },
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1200
            )
            
            return {
                "response": completion.choices[0].message.content
            }
        except Exception as e:
            return {
                "response": f"Erro ao gerar texto: {e}"
            }

    # Monta o prompt com as sentenças e o problema de lógica e exibe a resposta
    @staticmethod
    def resolvedor(n_sentencas: str, sentencas: str, problema: str):
        # Executa o resolvedor
        prompt = f"""
            ### Contexto
            Você é um tutor especializado em lógica proposicional. Explique de forma clara e concisa.
            ### Objetivo
            Resolva o problema usando:
            - Regras de Inferência: Modus Ponens, Modus Tollens, etc.
            - Regras de Equivalência: Dupla Negação, De Morgan, etc.
            Use Chain of Thought (CoT) para decompor o problema.
            ### Sentenças
            {n_sentencas} sentenças fornecidas:
            {sentencas}
            ### Problema
            {problema}
            ### Saída Esperada
            Forneça explicações passo a passo e a conclusão final no formato:
            - Passo 1: [Explicação]
            - Passo 2: [Explicação]
            - Conclusão: [Resultado]
            Se não for possível provar, explique por quê.
            ### Delimitadores
            Use '===' para separar seções.
            ### Exemplo de Saída
            ===
            - Passo 1: Suponha A ∨ C. Assuma ¬(B ∨ C) como hipótese para Redução ao Absurdo.
            - Passo 2: Pela Lei de De Morgan, ¬(B ∨ C) é equivalente a ¬B ∧ ¬C.
            - Passo 3: De ¬B ∧ ¬C, concluímos ¬C e ¬B por Eliminação da Conjunção.
            - Passo 4: De A ∨ C e ¬C, concluímos A por Silogismo Disjuntivo.
            - Passo 5: De A → B e A, aplicamos Modus Ponens para concluir B.
            - Passo 6: B contradiz ¬B, então rejeitamos ¬(B ∨ C) e concluímos B ∨ C por Redução ao Absurdo.
            - Conclusão: Por prova condicional, a partir da hipótese A ∨ C e da conclusão B ∨ C, provamos que (A ∨ C) → (B ∨ C).
            ===
            """
        result = Qwen.get_response(prompt)
        if result["response"]:
            return(Qwen.to_markdown_terminal(result["response"]))
        else:
            print("Não foi possível gerar uma resposta.")
            
        return result["response"]

    # Avalia a resposta gerada pelo modelo Qwen 
    @staticmethod
    def avaliador(resposta1: str, resposta2: str):
        prompt = (
            f"Por meio das Regras de Lógica Proposicional, avalie qual das respostas a seguir é a melhor"
            f" Resposta 0: {resposta1}\n\nResposta 2: {resposta2}\n"
            f"Se a resposta 0 for melhor, digite apenas '0'. Se a resposta 2 for melhor, digite apenas '2'."
        )
    

        result = Qwen.get_response(prompt)
        response_text = result["response"].strip()

        print(f"Qwen {response_text}")  # debug

        if response_text == "0":
            return 0
        elif response_text == "2":
            return 2
        else:
            print("Não foi possível gerar uma avaliação satisfatível(Qwen).")
            return None
    
    @staticmethod
    def avaliadorbinario(resposta: str):
        response = Qwen.get_response(f"Por meio das regras de lógica proposicional avalie a resposta que irei lhe entregar e diga apenas se concorda ou discorda da resolução. \n\n"
                                       f"Resposta em questão: {resposta}.")

        if response:
            return(Qwen.to_markdown_terminal(response))
        else:
            return("Não foi possível gerar uma resposta. (Qwen)")      

    #função dedicada a resolver problemas de lógica proposicional em 
    @staticmethod
    def resolver(problem: str): 
        response = Qwen.get_response(f" Solve the following logic proof problem and provide a detailed, step-by-step explanation (step-by-step proof construction) using the natural deduction method through the use of logical inference rules like Modus Ponens, Modus Tollens, Hypothetical Sylogism, as well as rules for replacement (like De Morgan’s Law, Double Negation). The explanation should be tailored for undergraduate students in introductory logic courses, meaning you should define any technical terms and explain each step clearly (step-by-step proof construction). Problem:  {problem}")
        
        if response:
            return(Qwen.to_markdown_terminal(response))
        else:
            return("Não foi possível gerar uma resposta. (Qwen)")          


    #função dedicada a avaliar problemas de lógica proposicional em inglês
    @staticmethod
    def appraiser(answer: str):
        response = Qwen.get_response(f"Evaluate the following logical proof resolution and provide a detailed explanation, evaluating the method of natural deduction through the use of logical inference rules such as Modus Ponens, Modus Tollens, Hypothetical Syllogism, as well as rules for substitution (such as De Morgan's Law, Double Negation). The evaluating should be adapted for undergraduate students in introductory logic courses, which means you should evaluate any technical terms and explain each step clearly if it is correct or not. Problem: {answer}")

        if response:
            return(Qwen.to_markdown_terminal(response))
        else:
            return("Não foi possível gerar uma resposta. (Qwen)")         
