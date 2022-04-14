import time
import os
import urllib.request


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
            if line[1].endswith(' '):
                wordsList.append(
                    line[1][:-1].replace("'", '').replace('?', '').replace('.', '').replace(' ', '_').lower())
            else:
                wordsList.append(line[1].replace(
                    "'", '').replace('?', '').replace('.', '').replace(' ', '_').replace('-', '_').lower())
    return wordsList


def words_to_download_audio():  # Funkcja sprawdza do których słowek nie ma pliku audio
    wordsIn = []
    wordsToDown = []
    for item in os.listdir('.\\audio'):
        wordsIn.append(item[:-4])

    for word in get_words_list():
        if word not in wordsIn:
            wordsToDown.append(word)
    return wordsToDown


wordErrorEn = []
wordError = []
for word in words_to_download_audio():
    time.sleep(1)
    try:
        urllib.request.urlretrieve(
            'https://www.diki.pl/images-common/en/mp3/'+word+'.mp3', '.\\audio\\'+word+'.mp3')

    except:
        wordErrorEn.append(word)
        print(f'ERROR: {word}')
    else:
        print(f'Download - OK: {word}')

if len(wordErrorEn) > 0:
    for word in wordErrorEn:
        time.sleep(1)
        try:
            urllib.request.urlretrieve(
                'https://www.diki.pl/images-common/en-ame/mp3/'+word+'.mp3', '.\\audio\\'+word+'.mp3')

        except:
            wordError.append(word)
            print(f'ERROR: {word}')
        else:
            print(f'Download - OK: {word}')

if len(wordError) > 0:
    print(f'Błędy przy pobieraniu: {len(wordError)} słów')
    print("="*50)
    for word in wordError:
        print(word)
    print("="*50)
