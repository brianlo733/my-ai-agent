import os
import requests

def run_report():
    # 1. 取得 API Key (請確保 GitHub Secret 名稱為 GEMINI_API_KEY)
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ 錯誤：搵唔到 GEMINI_API_KEY，請檢查 GitHub Secrets 設定。")
        return

    # 2. 模擬賽馬資料 (之後可以升級做自動爬蟲)
    racing_data = """
    賽事日期: 2026-04-22 (星期三)
    賽場: 跑馬地 (Happy Valley)
    重點場次: 第7場 - 三級賽 (1200米)
    注目馬匹: 1. 英雄豪邁 (表現穩定), 2. 財駿 (試閘出色), 3. 嫡愛心 (強勢配搭)
    """

    # 3. 設定 Google API URL (使用 v1 版本最穩定)
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    headers = {'Content-Type': 'application/json'}
    
    # 4. 設定指令，強制要求廣東話同專業格式
    payload = {
        "contents": [{
            "parts": [{"text": f"你係一個香港專業馬評人。請根據以下資訊，用流利、生動嘅廣東話為 Brian 寫一份簡單嘅聽日賽馬重點報告。要求用列點方式，語氣要似報紙馬經：\n{racing_data}"}]
        }],
        "generationConfig": {
            "maxOutputTokens": 500,
            "temperature": 0.7
        }
    }

    try:
        print("正在連線至 Google Gemini 官方 API...")
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        
        if response.status_code == 200:
            # 成功攞到回應
            content = result['candidates'][0]['content']['parts'][0]['text']
            print("\n" + "="*30)
            print("🐎 聽日賽馬重點報告 (Gemini 官方版)")
            print("="*30)
            print(content)
            print("="*30)
        else:
            print(f"⚠️ API 回報錯誤：{result.get('error', {}).get('message', '未知錯誤')}")
            
    except Exception as e:
        print(f"❌ 連線程式出錯：{e}")

if __name__ == "__main__":
    run_report()
