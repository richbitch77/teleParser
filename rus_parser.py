import re

def write_words(lines):
    file1 = open("src\\files\\new.txt", encoding='utf-8', mode="w")  # append mode
    for l in lines:
        words = l.split('\n')
        for word in words:
            if len(word) > 4:
                file1.write(word + '\n')
    file1.close()


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))



with open("src\\files\\rus_names.txt", encoding = 'utf-8', mode='r') as f:
    lines = []
    for line in f:
        # if line == '\n' or has_cyrillic(line):
        #     continue
        # l = line.split(', ')
        #line = line.replace('B', '\nB')[1:-1]
        #line = re.sub(r'[A-Z]', r'\n\g<0>', line)
        # for l2 in l:
        #     l2 = l2.replace('\n', '')
        #     lines.append(l2.lower())
        lines.append(line)
    write_words(lines)