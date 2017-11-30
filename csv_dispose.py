import csv
# import

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
