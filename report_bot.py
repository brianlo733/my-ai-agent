import os
from openai import OpenAI

# 1. 設置 OpenRouter API
# 確保 base_url 係正確嘅 OpenRouter 路徑
client = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def run_report():
    # 呢幾個係 OpenRouter 目前最穩定、唔容易報 404 嘅免費模型 ID
    models_to_try = [
        "mistralai/mistral-7b-instruct:free",
        "google/gemini-flash-1.5-8b",
        "meta-llama/llama-3.1-8b-instruct"
    ]
    
    success = False
    for model_name in models_to_try:
        try:
            print(f"正在嘗試模型：{model_name}...")
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "user", "content": "用兩句廣東話同 Brian 講早晨。"}
                ],
                extra_headers={
                    "HTTP-Referer": "https://github.com/brianlo733/my-ai-agent",
                    "X-Title": "Brian AI Agent"
                },
                max_tokens=50
            )
            
            print("--- OpenRouter 回應 ---")
            print(response.choices[0].message.content)
            success = True
            break
            
        except Exception as e:
            print(f"嘗試 {model_name} 失敗：{e}")
            continue

    if not success:
        print("依然無法連線。Brian，請去 OpenRouter 官網確認你粒 API Key 係咪已經設定咗正確嘅 Credits (就算 0 蚊都要有一個 Active Project)。")

if __name__ == "__main__":
    run_report()
