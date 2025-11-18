if __name__ == "__main__":
    pass
def count_paragraphs(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    paragraphs = text.split('\n\n')
    return len([p for p in paragraphs if p.strip()])
