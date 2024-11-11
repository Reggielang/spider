# 1. 找到未加密的参数   window.asrsea(参数,xxx,xxx,xxx)
# 2. 想办法把参数进行加密(必须参考网易的逻辑) params - encText, encSeckey - encSeckey
# 3. 请求到网易云,拿到评论信息
import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
from Crypto.Util.Padding import pad

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 请求方式是post
data = {
    "csrf_token":"",
    'cursor':"-1",
    'offset':"0",
    'orderType':"1",
    'pageNo':"1",
    'pageSize':"20",
    'rid':"R_SO_4_32507038",
    'threadId':"R_SO_4_32507038"
}
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "UTR7UC2ccxeFK3HM" #手动固定的 -人家的函数是随机的

def get_enSenkey():
    #由于i是固定的，那么encSenkey是固定的
    return "c999e827b9aa3e6fb54f25e74adbc309c6f01c85489099b3e078895c6277a8bc3c07b4fd644222d28d63b8729cca3bd2714999b152627c199805e95b52f54dc246fb000bc4f3c89642df183e64c711ce381c0d7f4945e7becf71ea7d60f696b271b6ec6f877b72efa3fc05f3e072d775f2be83c3f3f0dc7eda0c4d4b00c87fab"

#获取加密的参数过程
def get_parms(data): #默认这里接受到的字符串
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second

# def to_16(data):
#     pad = 16-len(data) %16
#     data = chr(pad) *pad
#     return data

# 加密过程
def enc_params(data,key):
    if isinstance(data, str):
        data_bytes = data.encode('utf-8')
    else:
        data_bytes = data
    iv="0102030405060708"
    aes = AES.new(key = key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC) #创造加密器
    # 填充数据以满足 AES 块大小要求
    padded_data = pad(data_bytes, AES.block_size)
    bs = aes.encrypt(padded_data)  # 加密 加密内容的长度必须是16的倍数
    #转换成字符串
    return  str(b64encode(bs),"utf-8")


# 处理加密过程
"""
    function a(a) { # 随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1) #循环16次
            e = Math.random() * b.length, #随机数 1.2345
            e = Math.floor(e),  # 取整 1 
            c += b.charAt(e); #取字符串中的xxx位置 b
        return c
    }
    function b(a, b) { #a 是要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b) # b 就是秘钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a) #e是数据
          , f = CryptoJS.AES.encrypt(e, c, {# c加密的秘钥
            iv: d, #iv 偏移量
            mode: CryptoJS.mode.CBC 模式是CBC
        });
        return f.toString()
    }
    function c(a, b, c) { # c里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { d=参数 bse8W(["流泪", "强"]) bse8W(RR7K.md) , bse8W(["爱心", "女孩", "惊恐", "大笑"])
        var h = {}
          , i = a(16); #i就是16位的随机值 把i设置成定值
        return h.encText = b(d, g), #g 就是秘钥
        h.encText = b(h.encText, i), #返回的就是params #i 也是秘钥
        h.encSecKey = c(i, e, f), #得到的就是encSeckey e和f是定死的 此时把i固定得到的key一定是固定的
        h
    }
    
    encText两次加密过程：
    数据+g => b => 第一次加密+i => params 
"""

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}

resp = requests.post(url,data={"params":get_parms(json.dumps(data)),"encSecKey":get_enSenkey()},headers=headers)
print(resp.text)