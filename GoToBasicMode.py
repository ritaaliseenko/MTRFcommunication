import serial

port = serial.Serial(port='COM3', baudrate=9600, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
# Переход из режима обновления ПО (занимает 12 секунд) в основной режим работы
# Кажется, у меня это не срабатывает...
basicModeCommand = bytearray([171, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 172])
port.write(basicModeCommand)

answer_titles = ['ST', 'MODE', 'CTR', 'TOGL', 'CH', 'CMD', 'FMT', 'D0', 'D1', 'D2', 'D3', 'ID0', 'ID1', 'ID2',
               'ID3', 'CRC', 'SP']
answer = port.read(size=17)
named_answer_bytes = dict(zip(answer_titles, answer))
print(named_answer_bytes)