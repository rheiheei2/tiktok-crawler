from TikTokApi import TikTokApi
import json, datetime

api = TikTokApi(default_client='web')
videos = api.trending(count=20)

items = [{
    "id": v.id,
    "desc": v.desc,
    "plays": v.stats.play_count,
    "likes": v.stats.digg_count,
    "hashtags": [h.title for h in v.hashtags],
    "video_url": v.video.address
} for v in videos]

fname = f"tiktok_{datetime.date.today()}.json"
json.dump(items, open(fname, "w"), ensure_ascii=False, indent=2)
print(f"Saved → {fname}") 