with open('adjectives.txt', 'r') as file1, open('nouns.txt', 'r') as file2, \
        open('wordlist_full.txt', 'w') as output_file:
    # Читаем слова из файлов и сохраняем их в списки
    words1 = [line.strip() for line in file1.readlines()]
    words2 = [line.strip() for line in file2.readlines()]

    # Создаем множество combinations, чтобы избежать повторяющихся сочетаний
    combinations = set()

    # Обходим все возможные пары слов из обоих списков
    for word1 in words1:
        for word2 in words2:
            # Составляем строку сочетания в формате "{слово1} {слово2}"
            combination = f"{word1} {word2}"
            # Добавляем сочетание в множество, если оно еще не встречалось
            if combination not in combinations:
                combinations.add(combination)

    # Записываем все сочетания в выходной файл,
    # каждое сочетание новой строкой
    output_file.write('\n'.join(combinations))
