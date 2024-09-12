
word = str(input("Введите слово: "))
result = ""
letters = "йиуеёыаоэяюЙИУЕЁЫАОЭЯЮ"


prevletter = word[0]
for letter in word[1:]:
    if (letter not in letters or prevletter != letter):
        result += prevletter
    prevletter = letter

result += prevletter
print(result)
        