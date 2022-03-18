
with open('input\Słówka SPEAK UP - Arkusz1.tsv', 'r', encoding='UTF-8') as file:
    words = file.read().splitlines()

convertData = []

for data in words[1:]:
    convertData.append(data.replace('\t', '/').split('/'))

wordsList = []
for line in convertData:
    if line[1] != '':
        wordsList.append(line[1])

print(wordsList)
