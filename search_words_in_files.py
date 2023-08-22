import os

def search_words_in_files(directory, word_list):
    results = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.sh')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line_num, line in enumerate(lines, start=1):
                        for word in word_list:
                            if word in line:
                                results.append((file, word, line_num))

    return results

def main():
    directory = input("Digite o caminho do diretório a ser pesquisado: ")
    word_list = input("Digite as palavras a serem pesquisadas (separadas por espaço): ").split()

    results = search_words_in_files(directory, word_list)

    with open('resultados.txt', 'w') as result_file:
        for result in results:
            result_file.write(f"Arquivo: {result[0]}, Palavra: {result[1]}, Linha: {result[2]}\n")

    print("Resultados foram salvos no arquivo 'resultados.txt'.")

if __name__ == "__main__":
    main()
