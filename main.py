import requests
import json
import time
import tqdm
api = "https://api.eol.cn/gkcx/api/?"
headers = {
"Accept": "application/json, text/plain, */*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
"Connection": "keep-alive",
"Content-Length": "286",
"Content-Type": "application/json;charset=UTF-8",
"Host": "api.eol.cn",
"Origin": "https://gkcx.eol.cn",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-site",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}
post_string = {
        "access_token": "",
        "admissions": "",
        "central": "",
        "department": "",
        "dual_class": "",
        "f211": "",  # 是否为211
        "f985": "",  # 是否为985
        "is_dual_class": "",  #是否为双一流
        "keyword": "", # 关键字查询
        "local_batch_id": "",  # 批次
        "local_type_id": 1,  # 文理科, 1-理科, 2-文科
        "page": 1,
        "province_id": "",  # 学校所在省份 11北京, 12天津, 13河北, 14山西, 23黑龙江, 51四川,
        "school_type": "",
        "size": 20,  # 每页显示的条数
        "type": "",
        "uri": "apidata/api/gk/score/province",
        "year": 2019
        }
for year in tqdm.tqdm(range(2014, 2020, 1)):
    year_result = {}
    year_result[str(year)] = []
    for page in tqdm.tqdm(range(0, 3001, 1)):
        post_string["page"] = page
        post_string["year"] = str(year)
        result = requests.post(api, data=post_string, headers=headers).json()
        if result["data"]["item"]:
            datas = result["data"]["item"]
            time.sleep(0.5)
            for data in datas:
                if data["local_province_name"] == "四川":
                    # row.add_row((data["name"], str(year), data["province_id"], data["local_batch_name"], data["min"], data["average"]))
                    year_result[str(year)].append({"名称": data["name"],
                                                   "所在地区id":data["province_id"],
                                                   "批次":data["local_batch_name"],
                                                   "最低值":data["min"],
                                                   "平均值":data["average"]})
        else:
            print("到达最后一页了！！")
            break
    filename = str(year)+'.json'
    with open(filename, 'w', encoding="utf-8") as file_obj:
        json.dump(year_result, file_obj, ensure_ascii=False,indent = 4)
# print(row)