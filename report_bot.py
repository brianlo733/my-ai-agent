import os
import requests
from bs4 import BeautifulSoup

def get_racing_data():
    print("正在抓取最新賽馬資料...")
    # 嘗試抓取 Sina Racing
    try:
        url = "https://racing.sina.com.hk/racing/racecard/"
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        horse_elements = soup.select('.horse_name')[:6]
        if horse_elements:
            horses = [h.get_text(strip=True) for h in horse_elements]
            return f"Current horses in spotlight: {', '.join(horses)}"
    except Exception as e:
        print(f"爬蟲暫時未能連線 (Error: {e})，使用精選馬匹資料備援。")
    
    # 備援資料 (Mock Data if scraper fails)
    return "Upcoming Focus: Heroic Master, Capital Delight, 嫡愛心 (Race 7, Happy Valley)"

def run_report():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY missing.")
        return

    racing_info = get_racing_data()
    
    # 呢度列出所有 OpenRouter 目前有機會成功嘅免費 ID
    models_to_try = [
        "meta-llama/llama-3.1-8b-instruct",
        "meta-llama/llama-3.1-8b-instruct:free",
        "mistralai/mistral-7b-instruct:free",
        "google/gemini-flash-1.5-8b",
        "huggingfaceh4/zephyr-7b-beta:free",
        "openchat/openchat-7b:free"
    ]

    print(f"🚀 開始 AI 分析 (資料: {racing_info})")

    for model in models_to_try:
        print(f"正在嘗試模型: {model} ...", end=" ")
        
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a professional horse racing analyst. Provide a brief 5-point analysis in English."},
                {"role": "user", "content": f"Analyze these horses for Brian: {racing_info}"}
            ],
            "extra_headers": {
                "HTTP-Referer": "https://github.com/brianlo733/my-ai-agent",
                "X-Title": "Brian Racing Agent"
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                print("✅ 成功！")
                print("\n" + "★"*40)
                print(f"🐎 AI ANALYSIS REPORT (Model: {model})")
                print("★"*40)
                print(content)
                print("★"*40)
                return
            else:
                print(f"❌ 失敗 (Status: {response.status_code})")
        except Exception:
            print("💥 連線超時")

    print("\n😭 今日 OpenRouter 所有免費通道都暫時失效，請稍後再試。")

if __name__ == "__main__":
    run_report()
