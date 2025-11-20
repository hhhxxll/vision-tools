def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        # 替换常见标点为空格，保证单词正确分割
        text = text.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace(
            ':', ' ').replace('(', ' ').replace(
            ')', ' ').replace('?', ' ').replace('!', ' ')
        words = text.split()
        print(f"单词数量：{len(words)}")
# 调用：将test.txt放在同一目录
count_words("test.txt")