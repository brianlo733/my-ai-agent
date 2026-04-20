import os
import requests

def run_report():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY is missing.")
        return

    # 模擬賽馬資料 (Racing Data)
    racing_data = "Date: 2026-04-22, Venue: Happy Valley, Race 7: Heroic Master, Capital Delight, 嫡愛心."

    # 呢度列出所有 OpenRouter 仲有機會行得通嘅免費模型 ID
    # 佢哋會逐個試，直到有一個唔係 404 為止
    models_to_try = [
        "meta-llama/llama-3.1-8b-instruct",
        "meta-llama/llama-3.1-8b-instruct:free",
        "mistralai/mistral-7b-instruct:free",
        "google/gemini-flash-1.5-8b",
        "huggingfaceh4/zephyr-7b-beta:free",
        "openchat/openchat-7b:free"
    ]

    print("🚀 Starting AI Model Recovery Mode...")

    for model in models_to_try:
        print(f"Trying Model: {model} ...", end=" ")
        
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a pro horse racing expert. Provide a detailed analysis in English."},
                {"role": "user", "content": f"Analyze these horses for tomorrow's race: {racing_data}"}
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            result = response.json()
            
            if response.status_code == 200:
                print("✅ SUCCESS!")
                content = result['choices'][0]['message']['content']
                print("\n" + "★"*40)
                print(f"AI ANALYSIS REPORT (via {model})")
                print("★"*40)
                print(content)
                print("★"*40)
                return # 成功就退出程序
            else:
                error_msg = result.get('error', {}).get('message', 'Unknown error')
                print(f"❌ Failed (Reason: {error_msg})")
        except Exception as e:
            print(f"💥 Connection Error: {e}")

    print("\n😭 All free models failed. OpenRouter might be having a major outage.")

if __name__ == "__main__":
    run_report()
