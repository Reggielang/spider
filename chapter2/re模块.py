import re

# 正则表达式
#findall 匹配所有符合条件的字符串
# li = re.findall(r"\d+","我的电话号码是：10086，我女朋友的电话是10010")
# print(li)

# !!!!效率比列表高很多
#finditer: 匹配字符串的所有内容，[但是返回的是迭代器],从迭代器中拿到内容需要.group()
# it = re.finditer(r"\d+","我的电话号码是：10086，我女朋友的电话是10010")
# print(it)
# for i in it:
#     print(i.group())

#search 返回的结果是match对象，拿数据也需要.group() -- 找到一个结果就返回
# s = re.search(r"\d+","我的电话号码是：10086，我女朋友的电话是10010")
# print(s)

# # match 默认从头开始匹配 等于加了^
# s = re.match(r"\d+","我的电话号码是：10086，我女朋友的电话是10010")
# print(s.group())

# 预加载正则表达式
# obj = re.compile(r"\d+")
# obj.finditer(r"\d+","我的电话号码是：10086，我女朋友的电话是10010")


s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>范思哲</span></div>
<div class='man'><span id='3'>宋铁</span></div>
<div class='jack'><span id='4'>大聪明</span></div>
"""
# (?P<分组名字>正则) 可以单独从正则匹配结果中提取数据
# re.S 让.能匹配换行符
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>",re.S)
res = obj.finditer(s)
for i in res:
    print(i.group("id"))
    print(i.group("name"))
