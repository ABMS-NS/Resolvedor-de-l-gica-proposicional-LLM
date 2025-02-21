import textwrap
import os
import time
import csv
import psutil
import socket
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

class Qwen:
   
    correct_responses = 0
    total_responses = 0

    
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
            # Medição da latência da rede usando socket
            def measure_latency(host, port=443, timeout=10):
                try:
                    start_time = time.time()
                    with socket.create_connection((host, port), timeout=timeout) as sock:
                        end_time = time.time()
                    return (end_time - start_time) * 1000  
                except Exception as e:
                    print(f"> Erro ao medir latência: {e}")
                    return None

            # Mede a latência da rede para o host da API
            api_host = "dashscope-intl.aliyuncs.com"
            network_latency = measure_latency(api_host)
            if network_latency is None:
                network_latency = 0  

            # Inicia a medição de tempo e uso de recursos
            start_time = time.time()
            process = psutil.Process(os.getpid())  # Processo atual
            cpu_start = process.cpu_percent(interval=None)  # Uso inicial de CPU
            memory_start = process.memory_info().rss  # Uso inicial de memória (em bytes)

            # Chamada à API
            completion = client.chat.completions.create(
                model="qwen-plus",
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
                max_tokens=700  # Limite máximo de tokens na resposta
            )

            # Finaliza a medição de tempo e uso de recursos
            end_time = time.time()
            cpu_end = process.cpu_percent(interval=None)
            memory_end = process.memory_info().rss

            # Calcula as métricas
            response_time = end_time - start_time
            cpu_usage = cpu_end - cpu_start
            memory_usage = memory_end - memory_start
            server_processing_time = (response_time * 1000) - network_latency

            # Obtém o número de tokens usados diretamente da API
            tokens_used = completion.usage.total_tokens

            # Retorna a resposta, métricas e tokens usados
            return {
                "response": completion.choices[0].message.content,
                "response_time": response_time,
                "tokens_used": tokens_used,  # Tokens usados obtidos da API
                "cpu_usage": cpu_usage,
                "memory_usage": memory_usage,
                "network_latency": network_latency,
                "server_processing_time": server_processing_time
            }
        except Exception as e:
            return {
                "response": f"Erro ao gerar texto: {e}",
                "response_time": None,
                "tokens_used": None,
                "cpu_usage": None,
                "memory_usage": None,
                "network_latency": None,
                "server_processing_time": None
            }

    # Exibe a resposta para um prompt dado
    @staticmethod
    def ask(prompt: str):
        result = Qwen.get_response(prompt)
        if result["response"]:
            print(Qwen.to_markdown_terminal(result["response"]))
            print(f"> Tempo de resposta total: {result['response_time']:.2f} segundos")
            print(f"> Tokens usados: {result['tokens_used']}")
            print(f"> Uso de CPU: {result['cpu_usage']}%")
            print(f"> Uso de Memória: {result['memory_usage'] / (1024 * 1024):.2f} MB")
            print(f"> Latência da Rede: {result['network_latency']:.2f} ms")
            print(f"> Tempo de Processamento no Servidor: {result['server_processing_time']:.2f} ms")
        else:
            print("Não foi possível gerar uma resposta.")

        # Salva os dados em arquivos CSV e .txt
        Qwen.save_metrics(prompt, result)

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
            print(Qwen.to_markdown_terminal(result["response"]))
            print(f"> Tempo: {result['response_time']:.2f}s | Tokens: {result['tokens_used']} | CPU: {result['cpu_usage']}% | Memória: {result['memory_usage'] / (1024 * 1024):.2f}MB | Rede: {result['network_latency']:.2f}ms | Servidor: {result['server_processing_time']:.2f}ms")
        else:
            print("Não foi possível gerar uma resposta.")

        # Validação da resposta
        is_correct = input("> A resposta gerada está correta? (S/N): ").strip().upper()
        if is_correct == "S":
            Qwen.correct_responses += 1
        Qwen.total_responses += 1

        # Calcula a precisão
        accuracy = (Qwen.correct_responses / Qwen.total_responses) * 100 if Qwen.total_responses > 0 else 0
        print(f"> Precisão atual: {accuracy:.2f}% ({Qwen.correct_responses}/{Qwen.total_responses})")

        # Salva os dados em arquivos CSV e .txt
        Qwen.save_metrics(prompt, result)

    @staticmethod
    def save_metrics(prompt: str, result: dict):
        # Dados a serem salvos
        log_entry = {
            "Prompt": prompt,
            "Response": result["response"],
            "Response Time": result["response_time"],
            "Tokens Used": result["tokens_used"],
            "CPU Usage (%)": result["cpu_usage"],
            "Memory Usage (MB)": result["memory_usage"] / (1024 * 1024),
            "Network Latency (ms)": result["network_latency"],
            "Server Processing Time (ms)": result["server_processing_time"],
            "Correctness": "Correta" if result["response"] and "não foi possível provar" not in result["response"].lower() else "Incorreta"
        }

        # Salva em um arquivo CSV
        with open("metrics.csv", "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=log_entry.keys())
            if csvfile.tell() == 0:  # Escreve o cabeçalho apenas na primeira linha
                writer.writeheader()
            writer.writerow(log_entry)

        # Salva em um arquivo .txt
        with open("metrics.txt", "a", encoding="utf-8") as txtfile:
            txtfile.write(f"Prompt: {log_entry['Prompt'].strip()}\n")
            txtfile.write(f"Response: {log_entry['Response'].strip()}\n")
            txtfile.write(f"Response Time: {log_entry['Response Time']:.2f}s\n")
            txtfile.write(f"Tokens Used: {log_entry['Tokens Used']}\n")
            txtfile.write(f"CPU Usage: {log_entry['CPU Usage (%)']}%\n")
            txtfile.write(f"Memory Usage: {log_entry['Memory Usage (MB)']:.2f}MB\n")
            txtfile.write(f"Network Latency: {log_entry['Network Latency (ms)']:.2f}ms\n")
            txtfile.write(f"Server Processing Time: {log_entry['Server Processing Time (ms)']:.2f}ms\n")
            txtfile.write(f"Correctness: {log_entry['Correctness']}\n")
            txtfile.write("-" * 50 + "\n")

        print(f"> Resposta avaliada como: {log_entry['Correctness']}")
