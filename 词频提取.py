import jieba
from collections import Counter

file_name = '示例文本.txt'
 
# 使用with语句确保文件正确关闭
with open(file_name, 'r') as file:
    content = file.read()  # 读取文件全部内容
    print(content)
text = content
words = jieba.cut(text)
word_counts = Counter(words)
for word, count in word_counts.items():
    print(f"{word}: {count}")
