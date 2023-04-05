from transliterate import translit


def write_words(lines):
    file1 = open("src/files/eng_rus_words.txt", encoding='utf-8', mode="w")  # append mode
    for l in lines:
        l = l.replace("'", "")[:-1]
        if len(l) < 5:
            continue
        file1.write(l+'\n')
    file1.close()


with open("src\\files\\new_rus_words.txt", encoding='utf-8', mode="r") as f:
    lines = []
    for line in f:
        line_eng = translit(line, 'ru', reversed=True)
        lines.append(line_eng)
    write_words(lines)
