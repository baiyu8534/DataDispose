import json

filename = 'json_test.json'

with open(filename) as f:
    # 得到json数据，是一个字典或列表
    jsondata = json.load(f)
    print(jsondata)

# 遍历列表 用字典的key获取对应的value
for itemdata in jsondata:
    if itemdata['Year'] == '1960':
        print('value::' + itemdata['Value'])

# 带小数点的str不能直接转int 如'111.222'
# 需要先转float再转int  a = int(float('111.222'))
