import json
import datetime
import random

# テスト用のダミーデータを生成
def generate_dummy_data():
    dummy_videos = []
    
    for i in range(20):
        video = {
            "id": f"test_video_{i+1}",
            "desc": f"テスト動画 #{i+1} - トレンド投稿のサンプル",
            "plays": random.randint(10000, 1000000),
            "likes": random.randint(1000, 100000),
            "hashtags": [f"test{i+1}", "trending", "sample"],
            "video_url": f"https://test-url-{i+1}.example.com"
        }
        dummy_videos.append(video)
    
    return dummy_videos

# メイン処理
try:
    print("TikTok トレンドデータを収集中...")
    videos = generate_dummy_data()
    
    # JSONファイルに保存
    fname = f"tiktok_{datetime.date.today()}.json"
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 成功: {len(videos)}件のデータを {fname} に保存しました")
    
except Exception as e:
    print(f"❌ エラー: {e}")
    exit(1)
