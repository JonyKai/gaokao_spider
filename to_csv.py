import json
f = open("result.txt", "w", encoding="utf-8")
for i in range(2014, 2020, 1):
    with open(str(i)+'.json', 'r', encoding="utf-8") as json_file:
        result = json.load(json_file)
        for line in result[str(i)]:
            f.write(",".join([line["名称"],str(i), str(line["所在地区id"]),line["批次"],str(line["最低值"]),str(line["平均值"])]))
            f.write("\n")


