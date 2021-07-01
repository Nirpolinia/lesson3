
# w - write; r - read; a - add
#\n - перенос строки, \t - tab

with open('referat.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    file_len = len(text)
    print(file_len)
    words = len(text.split())
    print(words)
    text = text.replace(".","!")
    #print(text)
with open('referat2.txt', 'w', encoding='utf-8') as f:
    f.write(text)
with open('referat.txt', 'w', encoding='utf-8') as f:
    text = text.replace("!",".")
    f.write(text)