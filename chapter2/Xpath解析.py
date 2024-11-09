# Xpath 是XML文档中搜索内容的一门语言
# HTML是XML的子集，所以Xpath也可以用于解析HTML文档
# lxml 是Xpath解析的库

# 使用 lxml 的 etree 库
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     
     </ul>
     <div>
        <a>热热热</a>
     </div>
     <span>
        <a>热热热2</a>
     </span>
 </div>
'''

#利用etree.HTML，将字符串解析为HTML文档
html = etree.XML(text)
# text()拿文本
# result = html.xpath('/div/ul/li/a/text()')
result = html.xpath('/div//a/text()') #// 后代节点
result = html.xpath('/div/*/a/text()') #* 任意的节点，通配符
result = html.xpath('/div//a/text()') #* 任意的节点，通配符


print(result)