import keyboard
import time


def renameFile(namefile):
    keyboard.send('F2')
    keyboard.send('Backspace')
    keyboard.write(f'{namefile}')
    keyboard.send('enter')

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

dictRalf = {
    'a' : 'Журнал ТО',
    'q' : 'СН',
    'z' : 'Чек лист 1',
    'x' : 'Чек лист 2',
    'c' : 'Чек лист 3'}

dictAdidas = {
    'q' : 'Акт',
    'a' : 'ТО 1',
    's' : 'ТО 2',
    'z' : 'ЧЛ 1',
    'x' : 'ЧЛ 2',
    'd' : 'Приемники 1',
    'f' : 'Приемники 2',
    'e' : 'Приемники 3',
    'r' : 'Приемники 4',
    'c' : 'ЧЛ 3',
    'v' : 'СИЗ 2'
    }

# hotkey = dictAdidas
hotkey = dictRalf

for k,v in hotkey.items():
    keyboard.add_hotkey(k, renameFile, args = [v])

keyboard.add_hotkey('b', renameAll)

keyforstop = 'n'
print('Hotkey activate')
print(f'Press "{keyforstop}" for end program')
keyboard.wait(keyforstop)
print('Program end')
