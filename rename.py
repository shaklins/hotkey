import keyboard
import json
import time


def ChangeStore():
    Store = input('Insert name store for start (Adidas or Ralf): ')
    return Store


def BindKey(dictStore: dict, Store: str):
    def renameFile(namefile):
        keyboard.send('F2')
        keyboard.send('Backspace')
        keyboard.write(f'{namefile}')
        keyboard.send('enter')
    for k, v in dictStore[Store].items():
        keyboard.add_hotkey(k, renameFile, args=[v])


def renameAll():
    i = 8
    keyboard.send('F2')
    time.sleep(1)
    while True:
        keyboard.send('tab')
        i -= 1
        if i == 0:
            break
    keyboard.send('enter')


with open('dictStore.json', 'r', encoding='UTF-8') as file:
    dictStore = json.load(file)

Store = ChangeStore()
BindKey(dictStore, Store)
keyboard.add_hotkey('b', renameAll)

keyforstop = 'n'
print(f'Hotkey activate \nPress "{keyforstop}" for end program')
keyboard.wait(keyforstop)
print('Program end')
