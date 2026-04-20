import os
from openai import OpenAI

# 1. 設置 OpenRouter API
client = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://api.deepseek.com" if "sk-ds-" in os.environ.get("OPENROUTER_API_KEY", "") else "https://openrouter.ai/api/v1"
)

def run_report():
    # 嘗試三個最常用嘅免費模型名，避開 OpenRouter 嘅路徑問題
    models_to_try = [
        "google/gemini-flash-1.5-exp:free", # Gemini 1.5 Flash 實驗版
        "meta-llama/llama-3.1-8b-instruct:free", # Llama 3.1 (超穩定)
        "google/gemini-flash-1.5-8b:free" # Gemini 1.5 Flash 8B
    ]
    
    success = False
    for model_name in models_to_try:
        try:
            print(f"正在嘗試模型：{model_name}...")
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "user", "content": "用兩句廣東話同 Brian 講聲早晨，話佢聽 AI 轉咗去 OpenRouter 免費模型成功連線。"}
                ],
                extra_headers={
                    "HTTP-Referer": "https://github.com/brianlo733/my-ai-agent",
                    "X-Title": "Brian AI Agent"
                },
                max_tokens=100
            )
            
            print("--- OpenRouter 回應 ---")
            print(response.choices[0].message.content)
            success = True
            break # 成功咗就跳出迴圈
            
        except Exception as e:
            print(f"嘗試 {model_name} 失敗：{e}")
            continue

    if not success:
        print("所有免費模型暫時無法連線，請檢查 OpenRouter 餘額或稍後再試。")

if __name__ == "__main__":
    run_report()
