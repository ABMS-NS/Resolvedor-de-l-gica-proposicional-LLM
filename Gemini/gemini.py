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

    def resolvedorOld(n_sentencas: str, sentencas: str, problema: str):
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
            print("Não foi possível gerar uma resposta.")

    def avaliador(resposta1: str, resposta2: str):
        response = Gemini.get_response(f"Por meio das regras de lógica proposicional avalie qual das respostas a seguir é a melhor"
            f"\n\nResposta 1: {resposta1}\n\nResposta 2: {resposta2}\n"
            f"Se a resposta 1 for melhor, digite apenas '1'. Se a resposta 2 for melhor, digite apenas '2'.")
        
        #conversor de string para inteiro
        if response == "1": return 1
        elif response == "2": return 2
        else: print("Não foi possível gerar uma avaliação satisfatível.")
        
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
            return("Não foi possível gerar uma resposta.")