import os
from google import genai

# 1. 設置 API (用新版 Client 寫法)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def run_report():
    try:
        # 2. 直接叫 2.0-flash，唔使理 v1beta 定 v1
        response = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents="請用廣東話同 Brian 講聲早晨，話畀佢聽你係佢嘅雲端助手，系統已經正式 Run 通咗！"
        )
        
        print("--- AI 回應開始 ---")
        print(response.text)
        print("--- AI 回應結束 ---")
        
    except Exception as e:
        print(f"都係有少少問題：{e}")

if __name__ == "__main__":
    run_report()
