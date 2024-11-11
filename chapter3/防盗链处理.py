import requests


# 1.contId
# 2.拿到videoStatus返回的json - srcURL
# 3.把srcURL里面的内容进行修整
# 4.下载视频

# 1.contId
# 拉取视频的网址
url = "https://www.pearvideo.com/video_1707010"

contId = url.split("_")[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.017520701093717506"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    # 防盗链: 溯源,本次请求的上一级是谁
    "referer":url,
}
# 2.拿到videoStatus返回的json - srcURL
resp = requests.get(videoStatusUrl,headers=headers)
dic = resp.json()
print(dic)

# 3.把srcURL里面的内容进行修整
srcUrl = dic['videoInfo']["videos"]['srcUrl']
systemTime = dic['systemTime']
#播放链接
# https://video.pearvideo.com/mp4/adshort/20201114/cont-1707010-15483292_adpkg-ad_hd.mp4
# 取到的链接
# https://video.pearvideo.com/mp4/adshort/20201114/1731310439061-15483292_adpkg-ad_hd.mp4


srcUrl = srcUrl.replace(systemTime,f"cont-{contId}")
print(srcUrl)

# 下载视频
with open("videos/a.mp4","wb") as f:
    f.write(requests.get(srcUrl).content)



