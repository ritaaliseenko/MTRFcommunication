import serial
from time import sleep

port = serial.Serial(port='COM3', baudrate=9600, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

answer_title = ['ST', 'MODE', 'CTR', 'TOGL', 'CH', 'CMD', 'FMT', 'D0', 'D1', 'D2', 'D3', 'ID0', 'ID1', 'ID2',
                'ID3', 'CRC', 'SP']

def send_command(id0, id1, id2, id3):
    # Команда switch
    command_package = bytearray([171, 2, 9, 0, 0, 4, 0, 0, 0, 0, 0, id0, id1, id2, id3, 0, 172])
    # Подсчет контрольной суммы
    byte_summ = 0
    for byte_value in range(0, 15):
        byte_summ += command_package[byte_value]
    crc = byte_summ % 256
    command_package[15] = crc
    port.write(command_package)
    answer = port.read(size=17)
    answer_byte_ctr = answer[2]
    answer_dictionary = dict(zip(answer_title, answer))
    print(answer_dictionary)
    # Передача следующей комады возможна не раньше, чем придет ответ от предыдущей команды
    # или после максимального таймаута в 5-7 секунд
    if answer_byte_ctr == 1 or answer_byte_ctr == 2:
        print("waiting...")
        sleep(5)
    else:
        sleep(0)

for times in range(0, 64):
    send_command(0, 1, 98, 27)
    send_command(0, 1, 98, 28)
