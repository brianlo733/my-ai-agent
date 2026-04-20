import os
import requests
from bs4 import BeautifulSoup

def get_real_racing_data():
    print("正在抓取最新賽馬排位資料...")
    # 呢個係一個相對容易抓取嘅賽馬資訊來源
    url = "https://racing.sina.com.hk/racing/racecard/"
    
    try:
        response = requests.get(url, timeout=15)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 搵出第一場或者重點場次嘅馬名 (簡單示例)
        horses = []
        # 根據 Sina 嘅結構抓取馬匹名稱
        horse_elements = soup.select('.horse_name')[:8] # 攞前 8 隻馬
        
        if not horse_elements:
            return "No real-time data found today. Using default analysis."
            
        for h in horse_elements:
            horses.append(h.get_text(strip=True))
        
        return f"Upcoming Race Horses: {', '.join(horses)}"
    except Exception as e:
        print(f"爬蟲出錯: {e}")
        return "Upcoming Race Focus: Heroic Master, Capital Delight, 嫡愛心"

def run_report():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY missing.")
        return

    # 1. 獲取真實資料
    real_data = get_real_racing_data()
    print(f"取得資料: {real_data}")

    # 2. OpenRouter API 設定
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # 指令優化：要求簡短，避免長篇大論出亂碼
    payload = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {
                "role": "system", 
                "content": "You are a HK horse racing expert. Provide a BRIEF analysis in 5 bullet points (English only)."
            },
            {
                "role": "user", 
                "content": f"Briefly analyze these horses for the next race: {real_data}"
            }
        ]
    }

    try:
        print("🚀 Sending data to AI for analysis...")
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        
        if response.status_code == 200:
            content = result['choices'][0]['message']['content']
            print("\n" + "★"*40)
            print("🐎 REAL-TIME RACING ANALYSIS (English)")
            print("★"*40)
            print(content)
            print("★"*40)
        else:
            print(f"⚠️ API Error: {result}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    run_report()
