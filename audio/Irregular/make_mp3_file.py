import os


def read_data():  # Funkcja do odczytu plików .tsv
    with open('Słówka - Irregular.tsv', 'r', encoding='UTF-8') as file:
        words = file.read().splitlines()
    convertData = []
    for data in words[1:]:
        convertData.append(data.replace('\t', '/').split('/'))
    return convertData


def get_words_list():  # Funkcja do wygenerowania listy angielskich słówek
    wordsList = []
    for line in read_data():
        if line[0] != '':
            if line[0].endswith(' '):
                wordsList.append(
                    line[0][:-1].replace("'", '').replace(',', '').replace(' ', '_').lower())
            else:
                wordsList.append(line[0].replace(
                    "'", '').replace(',', '').replace(' ', '_'))
    return wordsList


def words_to_make_file():  # Funkcja sprawdza do których słowek nie ma pliku audio
    wordsIn = []
    wordsToDown = []
    for item in os.listdir('.\\'):
        wordsIn.append(item[:-4])

    for word in get_words_list():
        if word not in wordsIn:
            wordsToDown.append(word)
    return wordsToDown


for word in words_to_make_file():
    try:
        open(word + '.mp3', 'x')
    except:
        print("error")
