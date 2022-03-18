import os


def read_data():  # Funkcja do odczytu plików .tsv
    with open('input\Słówka - Arkusz1.tsv', 'r', encoding='UTF-8') as file:
        words = file.read().splitlines()
    convertData = []
    for data in words[1:]:
        convertData.append(data.replace('\t', '/').split('/'))
    return convertData


def get_words_list():  # Funkcja do wygenerowania listy angielskich słówek
    wordsList = []
    for line in read_data():
        if line[1] != '':
            wordsList.append(line[1])
    return wordsList


def check_white_space():  # Funkcja do sprawadzania białych zanków w pliku bazowym
    for record in read_data():
        if record[1].endswith(' ') or record[1].startswith(' '):
            print(f'{record[0]}  --{record[1]}--')


def words_to_download_audio():  # Funkcja sprawdza do których słowek nie ma pliku audio
    wordsIn = []
    wordsToDown = []
    for item in os.listdir('.\\audio'):
        wordsIn.append(item[:-4])

    for word in get_words_list():
        if word not in wordsIn:
            wordsToDown.append(word)
    return wordsToDown


# print(words_to_download_audio())

for chrupek in words_to_download_audio():
    print(chrupek)
