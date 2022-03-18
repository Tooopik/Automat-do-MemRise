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
    for i in read_data():
        if i[1].endswith(' ') or i[1].startswith(' '):
            print(f'{i[0]}  --{i[1]}--')


# check_white_space()
#print(f'Dane po odczycie z pliku: {read_data()}')
print(f'Lista słowek dla Chrupka: {get_words_list()}')
