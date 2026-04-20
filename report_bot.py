import os
import requests

def run_report():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ 錯誤：搵唔到 GEMINI_API_KEY。")
        return

    racing_data = """
    賽事日期: 2026-04-22 (星期三)
    賽場: 跑馬地 (Happy Valley)
    重點場次: 第7場 - 三級賽 (1200米)
    注目馬匹: 1. 英雄豪邁 (穩定), 2. 財駿 (試閘好), 3. 嫡愛心 (強配)
    """

    # --- 關鍵修改位：改用 v1beta 並補全 models/ 前綴 ---
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": f"你係專業馬評人，用廣東話分析聽日跑馬地呢場重點：\n{racing_data}"}]
        }]
    }

    try:
        print("正在嘗試透過 v1beta 接口連線 Gemini...")
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        
        if response.status_code == 200:
            content = result['candidates'][0]['content']['parts'][0]['text']
            print("\n" + "="*30)
            print("🐎 聽日賽馬重點報告")
            print("="*30)
            print(content)
            print("="*30)
        else:
            # 如果連 v1beta 都唔得，佢會印出詳細原因
            print(f"失敗原因：{result}")
            
    except Exception as e:
        print(f"連線出錯：{e}")

if __name__ == "__main__":
    run_report()
