import serial
from time import sleep

port = serial.Serial(port='COM3', baudrate=9600, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

answer_titles = ['ST', 'MODE', 'CTR', 'TOGL', 'CH', 'CMD', 'FMT', 'D0', 'D1', 'D2', 'D3', 'ID0', 'ID1', 'ID2',
                'ID3', 'CRC', 'SP']

def send_command(id0, id1, id2, id3):
    # Команда switch
    package = bytearray([171, 2, 9, 0, 0, 4, 0, 0, 0, 0, 0, id0, id1, id2, id3, 0, 172])
    # Подсчет контрольной суммы
    byte_summ = 0
    for byte_value in range(0, 15):
        byte_summ += package[byte_value]
    crc = byte_summ % 256
    package[15] = crc
    port.write(package)

    answer = port.read(size=17)

    answer_code_ctr = answer[2]
    answer_dict = dict(zip(answer_titles, answer))
    print(answer_dict)
    # Передача следующей комады возможна не раньше, чем придет ответ от предыдущей команды
    # или после максимального таймаута в 5-7 секунд
    if answer_code_ctr == 1 or answer_code_ctr == 2:
        print("waiting...")
        sleep(5)
    else:
        sleep(0)

for times in range(0, 64):
    send_command(0, 1, 98, 27)
    send_command(0, 1, 98, 28)
