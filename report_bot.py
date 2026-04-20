import os
import requests

def run_report():
    # 1. 攞返你原本嗰粒 GEMINI_API_KEY
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("錯誤：搵唔到 GEMINI_API_KEY，請檢查 GitHub Secrets。")
        return

    # 2. 模擬賽馬資料
    racing_data = """
    賽事日期: 2026-04-22 (星期三)
    賽場: 跑馬地 (Happy Valley)
    重點場次: 第7場 - 三級賽 (1200米)
    注目馬匹: 1. 英雄豪邁 (穩定), 2. 財駿 (試閘好), 3. 嫡愛心 (強配)
    """

    # 3. 直接用 API URL (強制用 v1 版本避開 v1beta 嘅問題)
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": f"你係專業馬評人，用流利廣東話分析以下資訊，唔好講廢話：\n{racing_data}"}]
        }]
    }

    try:
        print("正在透過 Google 官方 API 分析賽馬資訊...")
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        
        if response.status_code == 200:
            content = result['candidates'][0]['content']['parts'][0]['text']
            print("--- 🐎 聽日賽馬情報 (Gemini 官方) ---")
            print(content)
        else:
            print(f"失敗原因：{result}")
            print("\n💡 如果見到 403，可能係 API Key 唔支援 GitHub 所在地區。")
            
    except Exception as e:
        print(f"連線出錯：{e}")

if __name__ == "__main__":
    run_report()
