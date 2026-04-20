import os
import requests

def run_report():
    # 1. 取得 API Key
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ 錯誤：搵唔到 OPENROUTER_API_KEY。")
        return

    # 2. 模擬賽馬資料
    racing_data = """
    賽事日期: 2026-04-22 (星期三)
    賽場: 跑馬地 (Happy Valley)
    重點場次: 第7場 - 三級賽 (1200米)
    注目馬匹: 1. 英雄豪邁 (穩定), 2. 財駿 (試閘好), 3. 嫡愛心 (強配)
    """

    # 3. OpenRouter 設定
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "google/gemini-2.0-flash-exp:free",
        "messages": [
            {"role": "system", "content": "你係專業馬評人，請用廣東話分析資料。"},
            {"role": "user", "content": f"幫我簡單總結聽日跑馬地重點：\n{racing_data}"}
        ],
        "extra_headers": {
            "HTTP-Referer": "https://github.com/brianlo733/my-ai-agent",
            "X-Title": "Brian AI"
        }
    }

    try:
        print("🚀 正在連線 OpenRouter...")
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        
        if response.status_code == 200:
            content = result['choices'][0]['message']['content']
            print("\n" + "★"*20)
            print("🐎 聽日賽馬分析")
            print("★"*20)
            print(content)
            print("★"*20)
        else:
            print(f"⚠️ 出錯：{result}")
    except Exception as e:
        print(f"❌ 錯誤：{e}")

if __name__ == "__main__":
    run_report()
