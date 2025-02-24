import requests

class DeepSeek:

    API_KEY = "KEY"
    API_URL = "https://openrouter.ai/api/v1/chat/completions"

    @staticmethod
    def get_response(prompt: str):
        headers = {
            "Authorization": f"Bearer {DeepSeek.API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "deepseek/deepseek-chat:free",  # Modelo gratuito do DeepSeek dentro do OpenRouter
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 500
        }

        try:
            response = requests.post(DeepSeek.API_URL, json = data, headers = headers)

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"Erro na API: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Erro ao conectar à API: {e}"

    @staticmethod
    def resolvedor(n_sentencas: str, sentencas: str, problema: str):
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
