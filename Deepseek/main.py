from deepseek import DeepSeek


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
                    print('-=' * 40)
                    break
                entries.append(entry)
            print("Resumo do que foi inserido:")
            print("\n".join(entries))
            confirmacao = input(
                "Os dados estão corretos? Digite 'SIM' para continuar ou 'NÃO' para editar: ").strip().upper()[0]
            if confirmacao == "S":
                print('-=' * 40)
                return "\n".join(entries)
            else:
                print('-=' * 40)
                print('Ok! Vamos tentar novamente...')

    # Captura as sentenças
    sentencas = capture_input(
        "Digite as sentenças (digite 'FIM' para finalizar):",
        "A: Chuva\nB: Rua Molhada\nC: Rua Escorregadia\n"
    )

    # Captura o problema
    problema = capture_input(
        "Agora, digite o problema utilizando quebra de linha para separar cada sentença\nE o número da mesma na frente (digite 'FIM' para finalizar):",
        "1-A → B\n2-B → C\n3-A\n"
    )
    print('Gerando resposta...')
    # Chama o resolvedor
    DeepSeek.resolvedor(n_sentencas, sentencas, problema)


if __name__ == "__main__":
    main()
