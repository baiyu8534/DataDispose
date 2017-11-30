import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从csv中获取数据绘制图表
filename = 'test.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    header_dict = dict(zip(list(range(1, len(header_row) + 1)), header_row))

    for index, value in header_dict.items():
        print(str(index) + ":" + value)

    highs = []
    for row in reader:
        highs.append(row[13])

    print('highs::', highs)
    for index, v in enumerate(highs):
        if v == '':
            highs[index] = '0'

    print('highs::', highs)

figure = plt.figure(figsize=(10, 6))
plt.plot(list(range(0, 20)), highs[0:20], c='red')
plt.title("Highs", fontsize='8')
plt.xlabel("date", fontsize='16')
plt.ylabel("H")
figure.autofmt_xdate()
plt.tick_params(axis='both')

plt.show()


