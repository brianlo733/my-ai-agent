import os
import requests

def run_report():
    # 1. 取得 API Key
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found.")
        return

    # 2. 模擬賽馬資料 (Mock Racing Data)
    racing_data = """
    Date: 2026-04-22 (Wednesday)
    Venue: Happy Valley Racecourse
    Key Race: Race 7 - Class 3 (1200m)
    Horses to watch: 
    1. Heroic Master (Consistent form, specialist at this distance)
    2. Capital Delight (Excellent recent trial, peak condition)
    3.嫡愛心 (Strong jockey-trainer combination, highly competitive)
    """

    # 3. OpenRouter 設定
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # 使用之前唯一成功過嘅 Llama 3.1 8B
    payload = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {
                "role": "system", 
                "content": "You are a professional horse racing analyst. Provide a concise summary in English."
            },
            {
                "role": "user", 
                "content": f"Please analyze the following racing info and provide a brief report for Brian:\n{racing_data}"
            }
        ],
        "extra_headers": {
            "HTTP-Referer": "https://github.com/brianlo733/my-ai-agent",
            "X-Title": "Brian Racing AI"
        }
    }

    try:
        print("🚀 Connecting to OpenRouter (Llama 3.1 8B)...")
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        
        if response.status_code == 200:
            content = result['choices'][0]['message']['content']
            print("\n" + "="*40)
            print("🐎 Horse Racing Report (English Version)")
            print("="*40)
            print(content)
            print("="*40)
        else:
            print(f"⚠️ API Error: {result.get('error', {}).get('message', 'Unknown Error')}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    run_report()
