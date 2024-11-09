# Xpath 是XML文档中搜索内容的一门语言
# HTML是XML的子集，所以Xpath也可以用于解析HTML文档
# lxml 是Xpath解析的库

# 使用 lxml 的 etree 库
from lxml import etree

tree = etree.parse("a.html")
# result = tree.xpath('/html')
# result = tree.xpath('/html/body/ul/li/a/text()')
result = tree.xpath('/html/body/ul/li[1]/a/text()')  # xpath的索引是从1开始

result = tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')  # 指定属性
print(result)

ol_li_li = tree.xpath('/html/body/ol/li')
print(ol_li_li)

for li in ol_li_li:
    # 从每个li中提取到文字信息
    result= li.xpath("./a/text()") #在li中查找a标签，然后提取文字 就不是从根节点开始
    result2 = li.xpath("./a/@href") # 提取a标签的href属性
    print(result, result2)

print(tree.xpath('//ul/li/a/@href'))