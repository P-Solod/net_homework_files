name_files = ['1file.txt', '2file.txt','3file.txt']
files_in_progress = ['new_1file.txt', 'new_2file.txt','new_3file.txt']
new_data_from_files = []
counter = 0

while counter < len(name_files):
    with open('task3/'+ name_files[counter], encoding='utf8') as file:
        text = file.readlines()
        number_lines = len(text)
    with open('task3/'+ name_files[counter], encoding='utf8') as file:
        text_2 = file.read()
    with open('task3/'+ files_in_progress[counter], 'w', encoding='utf8') as file:
        file.write(f'{name_files[counter]}\n{number_lines}\n{text_2}\n')
    counter += 1

for some_file in files_in_progress:
    with open('task3/' + some_file, encoding='utf8') as file:
        new_data = file.read()
        new_data_from_files.append(new_data)
new_data_from_files.sort(key=len)

with open('task3/merge_file.txt', 'a', encoding='utf8') as file:
    for some_pat in new_data_from_files:
        file.write(some_pat)