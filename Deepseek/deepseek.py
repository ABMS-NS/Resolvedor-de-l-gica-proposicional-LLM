import requests

class DeepSeek:

    #Key coletada do OpenRouter para uso do DeepSeek V3 (free)
    API_KEY = "KEY"
    API_URL = "https://openrouter.ai/api/v1/chat/completions"

    @staticmethod
    def get_response(prompt: str): #Uso de uma requisição HTTP para acessar a API do DeepSeek.
        headers = {
            "Authorization": f"Bearer {DeepSeek.API_KEY}",
            "Content-Type": "application/json"
        }

        #Descrição de como a mensagem do DeepSeek aparecerá para o usuário.
        data = {
            "model": "deepseek/deepseek-chat:free",  # Modelo gratuito do DeepSeek dentro do OpenRouter
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 1000
        }

        #Avisar ao usuário caso a API dê erro.
        try:
            response = requests.post(DeepSeek.API_URL, json = data, headers = headers)

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"Erro na API: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Erro ao conectar à API: {e}"

    #Resolvedor antigo. Prompt enviado ao main.py do deepseek.py (somente) para que ele resolva o problema de lógica proposicional
    @staticmethod
    def resolvedorOld(n_sentencas: str, sentencas: str, problema: str):
        prompt = (
            f"Resolva esse problema de lógica apresentado a seguir segundo as regras de lógica proposicional:\n\n"
            f"Número de sentenças que serão apresentadas para você: {n_sentencas}.\n"
            f"Agora, serão mostradas a entrada das sentenças no seguinte formato: 'A: sentença' sendo 'A' a letra que irá "
            f"representar tal sentença no problema e 'sentença' sendo a sentença em linguagem natural.\n"
            f"Sentenças postas pelo usuário: {sentencas}.\n"
            f"Agora, irei te mostrar o problema lógico que quero que resolva a partir do que mostrei: {problema}.\n"
            f"A partir disso quero que me diga a resposta do problema me dizendo como chegou até ela."
        )

        response = DeepSeek.get_response(prompt)

        if response:
            print(response)
        else:
            print("Não foi possível gerar uma resposta.")

    #Avaliador. Comparativo entre as LLMs. Prompt enviado ao DeepSeek se referindo às respostas do Gemini e do Qwen
    def avaliador(resposta1: str, resposta2: str):
        prompt = (
            f"Por meio das regras de lógica proposicional avalie qual das respostas a seguir é a melhor\n"
            f"Resposta 0: '{resposta1}'\nResposta 1: '{resposta2}'\n"
            f"Se a resposta 0 for melhor, digite apenas '0'. Se a resposta 1 for melhor, digite apenas '1'."
        )

        response = DeepSeek.get_response(prompt)

        #Conversor de string para inteiro
        if response == "0":
            return 0
        elif response == "1":
            return 1
        else:
            print("Não foi possível gerar uma avaliação satisfatível. (DeepSeek)")

    def resolvedor(n_sentencas: str, sentencas: str, problema: str): #Resolvedor novo. Prompt enviado ao 3_step_verification.py para que ele resolva o problema de lógica proposicional
        prompt = (
            f"Resolva esse problema de lógica apresentado a seguir segundo as regras de lógica proposicional:\n\n"
            f"Número de sentenças que serão apresentadas para você: {n_sentencas}.\n"
            f"Agora, serão mostradas a entrada das sentenças no seguinte formato: 'A: sentença' sendo 'A' a letra que irá "
            f"representar tal sentença no problema e 'sentença' sendo a sentença em linguagem natural.\n"
            f"Sentenças postas pelo usuário: {sentencas}.\n"
            f"Agora, irei te mostrar o problema lógico que quero que resolva a partir do que mostrei: {problema}.\n"
            f"A partir disso quero que me diga a reposta do problema me dizendo como chegou até ela."
            )
        
        response = DeepSeek.get_response(prompt)

        if response:
            return (response)
        else:
            print("Não foi possível gerar uma resposta.")
