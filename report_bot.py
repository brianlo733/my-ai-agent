import os
from openai import OpenAI

# 1. 設置 DeepSeek API
# 使用你喺 GitHub Secrets 設定嘅 DEEPSEEK_API_KEY
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def run_report():
    try:
        # 2. 呼叫 DeepSeek-V3 (即 deepseek-chat)
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你係一個精簡嘅廣東話助手。"},
                {"role": "user", "content": "用一句廣東話同 Brian 講聲早晨，並確認系統已經成功轉用 DeepSeek。"}
            ],
            max_tokens=50,  # 嚴格限制字數，極致慳錢
            stream=False
        )
        
        print("--- DeepSeek 回應開始 ---")
        print(response.choices[0].message.content)
        print("--- DeepSeek 回應結束 ---")
        
    except Exception as e:
        print(f"DeepSeek 執行出錯：{e}")

if __name__ == "__main__":
    run_report()
