import textwrap
import google.generativeai as genai

class Gemini:
    #só uma função pra o texto para aparecer de maneira bonita no terminal
    def to_markdown_terminal(text):
        text = text.replace('•', '*')
        return textwrap.indent(text, '> ')

    GOOGLE_API_KEY = ""
    genai.configure(api_key=GOOGLE_API_KEY,)

    def get_response(prompt: str):
        try:
        #configurar o modelo
            model = genai.GenerativeModel('gemini-1.5-flash')
        
        #gerar a resposta
            response = model.generate_content(prompt)
        
        #retornar o texto da resposta
            return response.text
        except Exception as e:
            return f"Erro ao gerar texto: {e}"


    def ask(prompt: str):
        response = Gemini.get_response(prompt)
    
        if response:
            print(Gemini.to_markdown_terminal(response))
        else:
            print("Não foi possível gerar uma resposta.")

    def resolvedorOld(n_sentencas: str, sentencas: str, problema: str): #função antiga de resolvedor
        response = Gemini.get_response(f"Resolva esse problema de lógica apresentado a seguir segundo as regras de lógica proposicional:\n\n"
            f"Número de sentenças que serão apresentadas para você: {n_sentencas}.\n"
            f"Agora, serão mostradas a entrada das sentenças no seguinte formato: 'A: sentença' sendo 'A' a letra que irá "
            f"representar tal sentença no problema e 'sentença' sendo a sentença em linguagem natural.\n"
            f"Sentenças postas pelo usuário: {sentencas}.\n"
            f"Agora, irei te mostrar o problema lógico que quero que resolva a partir do que mostrei: {problema}.\n"
            f"A partir disso quero que me diga a reposta do problema me dizendo como chegou até ela."
            )
            
        if response:
            print(Gemini.to_markdown_terminal(response))
        else:
            print("Não foi possível gerar uma resposta. (GEMINI)")

    def avaliador(resposta1: str, resposta2: str):
        response = Gemini.get_response(f"Por meio das regras de lógica proposicional avalie qual das respostas a seguir é a melhor"
            f"\n\nResposta 1: {resposta1}\n\nResposta 2: {resposta2}\n"
            f"Se a resposta 1 for melhor, digite apenas e unicamente '1'. Se a resposta 2 for melhor, digite apenas e unicamente '2'.")
        

        response = int(response)
        print(f"GEMINI {response}") #debug
        #conversor de string para inteiro
        if response == "1" or "'1'": return 1
        elif response == "2" or "'2'": return 2
        else: print("Não foi possível gerar uma avaliação satisfatível. (GEMINI)")
        
    def resolvedor(n_sentencas: str, sentencas: str, problema: str):
        response = Gemini.get_response(f"Resolva esse problema de lógica apresentado a seguir segundo as regras de lógica proposicional:\n\n"
            f"Número de sentenças que serão apresentadas para você: {n_sentencas}.\n"
            f"Agora, serão mostradas a entrada das sentenças no seguinte formato: 'A: sentença' sendo 'A' a letra que irá "
            f"representar tal sentença no problema e 'sentença' sendo a sentença em linguagem natural.\n"
            f"Sentenças postas pelo usuário: {sentencas}.\n"
            f"Agora, irei te mostrar o problema lógico que quero que resolva a partir do que mostrei: {problema}.\n"
            f"A partir disso quero que me diga a reposta do problema me dizendo como chegou até ela."
            )
            
        if response:
            return(Gemini.to_markdown_terminal(response))
        else:
            return("Não foi possível gerar uma resposta. (GEMINI)")
        
    def avaliadorbinario(resposta: str):
        response = Gemini.get_response(f"Por meio das regras de lógica proposicional avalie a resposta que irei lhe entregar e diga apenas se concorda ou discorda da resolução. \n\n"
                                       f"Resposta em questão: {resposta}.")


        if response:
            return(Gemini.to_markdown_terminal(response))
        else:
            return("Não foi possível gerar uma resposta. (GEMINI)")           
        

    #função dedicada a resolver problemas de lógica proposicional em inglês
    def resolver(problem: str): 
        response = Gemini.get_response(f" Solve the following logic proof problem and provide a detailed, step-by-step explanation (step-by-step proof construction) using the natural deduction method through the use of logical inference rules like Modus Ponens, Modus Tollens, Hypothetical Sylogism, as well as rules for replacement (like De Morgan’s Law, Double Negation). The explanation should be tailored for undergraduate students in introductory logic courses, meaning you should define any technical terms and explain each step clearly (step-by-step proof construction). Problem:  {problem}")
        
        if response:
            return(Gemini.to_markdown_terminal(response))
        else:
            return("Não foi possível gerar uma resposta. (GEMINI)")          


    #função dedicada a avaliar problemas de lógica proposicional em inglês
    def appraiser(aswer: str):
        response = Gemini.get_response(f"Evaluate the following logical proof resolution and provide a detailed explanation, evaluating the method of natural deduction through the use of logical inference rules such as Modus Ponens, Modus Tollens, Hypothetical Syllogism, as well as rules for substitution (such as De Morgan's Law, Double Negation). The evaluating should be adapted for undergraduate students in introductory logic courses, which means you should evaluate any technical terms and explain each step clearly if it is correct or not. Problem: {aswer}")

        if response:
            return(Gemini.to_markdown_terminal(response))
        else:
            return("Não foi possível gerar uma resposta. (GEMINI)")    