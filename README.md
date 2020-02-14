# 爬虫 for JS
爬取的网站：https://gkcx.eol.cn/lineschool，获取大学的录取分数线
由于网站采用了JS的动态加载，因此无法直接通过查看网页源代码获得。因此这里，我们首先用chrome的开发者模式分析JS提交的表单。
可以看到获取的方法为"POST"
请求的内容为：
'''
https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_dual_class=&keyword=%E5%8C%97%E4%BA%AC%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6&local_batch_id=&local_type_id=1&page=1&province_id=&school_type=&signsafe=&size=20&type=&uri=apidata/api/gk/score/province&year=2019
'''