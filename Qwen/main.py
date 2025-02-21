from qwen import Qwen

def main():
    # Solicita o número de sentenças
    n_sentencas = input("Digite o número de sentenças que existem no seu problema: ")
    
    # Captura o Input
    def capture_input(prompt_message, example):
        while True:
            print(prompt_message)
            print(f"Exemplo:\n{example}")
            entries = []
            while True:
                entry = input()
                if entry.strip().upper() == "FIM":
                    break
                entries.append(entry)
            print("\nResumo do que foi inserido:")
            print("\n".join(entries))
            confirmacao = input("Os dados estão corretos? Digite 'SIM' para continuar ou 'NÃO' para editar: ").strip().upper()
            if confirmacao == "SIM":
                return "\n".join(entries)

    # Captura as sentenças
    sentencas = capture_input(
        "Digite as sentenças (digite 'FIM' para finalizar):",
        "A: Chuva\nB: Rua Molhada\nC: Rua Escorregadia"
    )

    # Captura a conclusão desejada
    conclusao = input("Digite a conclusão desejada (ex.: 'Prove que Mágico é verdadeiro'): ")

    # Captura o problema
    problema = capture_input(
        "Digite o problema utilizando quebra de linha para separar cada sentença e o número da mesma na frente (digite 'FIM' para finalizar):",
        "1-A → B\n2-B → C\n3-A"
    )

    # Combina a conclusão ao problema
    problema_com_conclusao = f"{problema}\nConclusão desejada: {conclusao}"

    # Chama o resolvedor
    Qwen.resolvedor(n_sentencas, sentencas, problema_com_conclusao)

if __name__ == "__main__":
    main()
