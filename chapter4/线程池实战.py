# 1. 如何提取单个页面的数据
# 2. 上线程池,多个页面同时抓取
import time

import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_one_page(url, i):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    }

    limit = 20
    new_url = f"{url}?current={i}&limit={limit}"
    try:
        response = requests.get(new_url, headers=headers)
        response.raise_for_status()  # 检查响应状态码
        txt = response.json()
    except requests.RequestException as e:
        print(f"请求出错: {new_url} - {e}")
        return None

    data = []
    # 解析数据
    pro_li = txt.get('list', [])
    for item in pro_li:
        prodName = item.get('prodName')
        lowPrice = item.get('lowPrice')
        highPrice = item.get('highPrice')
        avgPrice = item.get('avgPrice')
        place = item.get('place')
        unitInfo = item.get('unitInfo')
        data.append({
            'prodName': prodName,
            'lowPrice': lowPrice,
            'highPrice': highPrice,
            'avgPrice': avgPrice,
            'place': place,
            'unitInfo': unitInfo
        })
    df = pd.DataFrame(data)
    print(new_url, "提取完成!")
    return df


if __name__ == '__main__':
    url = "http://www.xinfadi.com.cn/getPriceData.html"  # 替换为实际的URL
    all_dfs = []

    with ThreadPoolExecutor(50) as pool:
        for i in range(1,200):
            # 提交任务并收集Future对象
            futures = []
            futures.append(pool.submit(download_one_page, url, i))
            time.sleep(0.8)

            # 等待所有任务完成
            for future in futures:
                try:
                    df = future.result()
                    if df is not None:
                        all_dfs.append(df)
                except Exception as e:
                    print(f"任务出错: {e}")


    # 合并所有DataFrame
    final_df = pd.concat(all_dfs, ignore_index=True)
    final_df.to_csv('data.csv', index=False)
