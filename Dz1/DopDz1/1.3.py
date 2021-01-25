# Написать скрипт, который принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
from operator import itemgetter

t = input('ваш текст: ')
a = ["0", "1", "2", "3", "4", "—", "5", "6", "7", "8", "9", "-", "- ", "+", "/", "*", "@", "&", ",", ";", ":",
     "!", "?", ".", "...",
     "(", ")", "'"]
for i in a:
    t = t.replace(i, "")

b = t.lower()
c = t.split()

long = max(c, key=len)
print(f"Самое длинное слово: {long}")

d = []

for i in c:
    q = 0
    m = 0
    while q < len(c):
        if i == c[q]:
            m += 1
        q += 1
    d.append([i, m])

d.sort(key=itemgetter(1), reverse=True)

n = d[1]

print(f"Чаще всего в этом тексте употребляемся слово '{n[0]}'")