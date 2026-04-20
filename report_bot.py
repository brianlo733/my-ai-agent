import os
from google import genai

# 1. 設置 API
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def run_report():
    try:
        # 2. 注意模型名：喺 google-genai 入面直接打 'gemini-1.5-flash'
        response = client.models.generate_content(
            model='gemini-1.5-flash', 
            contents="Brian 你好！見到呢句代表你個 GitHub Agent 已經徹底成功連線喇！"
        )
        
        print("--- AI 回應開始 ---")
        print(response.text)
        print("--- AI 回應結束 ---")
        
    except Exception as e:
        # 呢度會幫你印出詳細錯誤，方便我哋 Debug
        print(f"執行出咗錯：{e}")

if __name__ == "__main__":
    run_report()
