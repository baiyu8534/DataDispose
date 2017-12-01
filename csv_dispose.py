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

    # 相当于做了错误数据检查，把不合法的数据转换为合法数据。也可以用try,遇到不合法数据跳过
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
# 可以让x轴的值斜着显示
figure.autofmt_xdate()
plt.tick_params(axis='both')

plt.show()

# datetime用法

data = datetime.strptime('2017-11-11', '%Y-%m-%d')
print(data)
# 2017-11-11 00:00:00

# 给两条折线之间填充颜色
# plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
