import os
from openai import OpenAI

# 1. 設置 OpenRouter API
client = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def run_report():
    try:
        # 2. 使用免費模型 (呢度揀 Gemini 1.5 Flash 免費版)
        response = client.chat.completions.create(
            model="google/gemini-flash-1.5:free", 
            messages=[
                {"role": "user", "content": "用一句廣東話同 Brian 講聲早晨。"}
            ],
            extra_headers={
                "HTTP-Referer": "https://github.com/brianlo733/my-ai-agent", # 隨便填
                "X-Title": "Brian AI Agent"
            }
        )
        
        print("--- OpenRouter 回應 ---")
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"OpenRouter 出錯：{e}")

if __name__ == "__main__":
    run_report()
