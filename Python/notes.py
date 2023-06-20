import json
from datetime import datetime

notes = []
path = "my_tasks/notes.json"

def load_notes():
    global notes
    try:
        with open(path, 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        pass

def save_notes():
    with open(path, 'w') as f:
        json.dump(notes, f)

def add_note():
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    created_at = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    note_id = 1
    for note in notes:
        if note["id"] == note_id:
            note_id += 1
    note = {'id': note_id, 'title': title, 'body': body, 'created_at': created_at, 'updated_at': created_at}
    notes.append(note)

    notes.sort(key= lambda x: x['id'])

    save_notes()
    print('Заметка добавлена!')

def view_notes():
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['body']}, Создано: {note['created_at']}, Обновлено: {note['updated_at']}")
    if not notes:
        print('Заметок нет')

def edit_note():
    note_id = int(input('Введите ID заметки, которую хотите отредактировать: '))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input('Введите новый заголовок заметки: ')
            note['body'] = input('Введите новый текст заметки: ')
            note['updated_at'] = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            save_notes()
            print('Заметка отредактирована!')
            break
    else:
        print('Заметка не найдена')

def delete_note():
    note_id = int(input('Введите ID заметки, которую хотите удалить: '))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes()
            print('Заметка удалена!')
            break
    else:
        print('Заметка не найдена')

load_notes()

while True:
    print('\nМеню:')
    print('1. Просмотр заметок')
    print('2. Добавление заметки')
    print('3. Редактирование заметки')
    print('4. Удаление заметки')
    print('5. Выход')
    choice = input('\nВыберите пункт меню: ')
    print()
    if choice == '1':
        view_notes()
    elif choice == '2':
        add_note()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        break
    else:
        print('Неверный пункт меню')