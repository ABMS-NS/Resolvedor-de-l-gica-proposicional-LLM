import textwrap
import google.generativeai as genai

class Gemini:
    #só uma função pra o texto aparecer certinho no terminal
    def to_markdown_terminal(text):
        text = text.replace('•', '*')
        return textwrap.indent(text, '> ')

    GOOGLE_API_KEY = "AIzaSyBpC_J5Dsl_gwqGBdC6nYRgT9Vk1pmKm_E"
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
            print(Gemini.to_markdown_terminal(response))
        else:
            print("Não foi possível gerar uma resposta.")
