import json
from mitmproxy import ctx
import os

OUTPUT_FOLDER = 'movies'
os.path.exists(OUTPUT_FOLDER) or os.makedirs(OUTPUT_FOLDER)


def response(flow):
    url = 'https://app5.scrape.center/api/movie/'
    if flow.request.url.startswith(url):
        text = flow.response.text
        if not text:
            return
        data = json.loads(text)
        items = data.get('results')
        for item in items:
            ctx.log.info(str(item))
            with open(f'{OUTPUT_FOLDER}/{item["name"]}.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(item, ensure_ascii=False, indent=2))


