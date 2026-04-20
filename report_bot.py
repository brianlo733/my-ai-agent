import os
import requests

def run_report():
    # 1. 取得 API Key (請確保 GitHub Secret 名稱為 OPENROUTER_API_KEY)
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ 錯誤：搵唔到 OPENROUTER_API_KEY，請檢查 GitHub Secrets。")
        return

    # 2. 模擬賽馬資料 (地基打通後，下一步我哋會將呢度變做自動抓取)
    racing_data = """
    賽事日期: 2026-04-22 (星期三)
    賽場: 跑馬地 (Happy Valley)
    重點場次: 第7場 - 三級賽 (1200米)
    注目馬匹: 
    1. 英雄豪邁 (表現穩定，路程專才)
    2. 財駿 (近日試閘出色，狀態大勇)
    3. 嫡愛心 (配搭強勢，值得關注)
    """

    # 3. 設定 OpenRouter API
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # 使用目前最強嘅免費模型：Gemini 2.0 Flash Exp (Free)
    payload = {
        "model": "google/gemini-2.0-flash-exp:free",
        "messages": [
            {
                "role": "system", 
                "content": "你係一個香港專業馬評家。請用道地、生動嘅廣東話為 Brian 分析賽馬資訊。語氣要似報紙馬經，多用專業術語（例如：穩陣、試閘、配搭）。"
            },
            {
                "role": "user", 
                "content": f"根據以下資料，幫我寫一份簡單嘅聽日跑馬地重點分析報告：\n{racing_data}"
            }
        ],
        "extra_headers": {
            "HTTP-Referer": "https://github.com/brianlo733/my-ai-agent",
            "X-Title": "Brian Racing AI"
        }
    }

    try:
        print("🚀 正在透過 OpenRouter 呼叫 Gemini 2.0 免費版...")
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        
        if response.status_code == 200:
            # 成功攞到回應
            content = result['choices'][0]['message']['content']
            print("\n" + "★"*20)
            print("🐎 聽日跑馬地賽馬重點分析")
            print("★"*20)
            print(content)
            print("★"*20)
        else:
            msg = result.get('error', {}).get('message', '未知錯誤')
            print(f"⚠️ OpenRouter 報錯：{msg}")
            
    except Exception as e:
        print(f"❌ 程式連線出錯：{e}")

if __name__ == "__main__":
    run_report()
        print("這通常代表你的 API Key 被 Google 判定為地區不支援，或者 Key 已過期。")

if __name__ == "__main__":
    run_report()
