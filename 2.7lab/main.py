with open('file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Считаем абзацы
paragraphs = 0
prev_line_empty = True  # считаем, что перед первым абзацем пустая строка

for line in lines:
    if line.strip() == '':  # если строка пустая
        prev_line_empty = True
    else:
        if prev_line_empty:  # если предыдущая строка была пустой, значит это новый абзац
            paragraphs += 1
        prev_line_empty = False

print(f"Количество абзацев: {paragraphs}")
