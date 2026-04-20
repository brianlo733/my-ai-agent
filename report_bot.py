import os
from google import genai

# 1. 設置 API
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def run_report():
    try:
        # 2. 試吓加返 models/ 前綴，睇吓新版 Library 係咪咁樣認
        response = client.models.generate_content(
            model='models/gemini-1.5-flash', 
            contents="Brian！系統終於正式連通喇！我係你嘅雲端助手。"
        )
        
        print("--- AI 回應開始 ---")
        print(response.text)
        print("--- AI 回應結束 ---")
        
    except Exception as e:
        print(f"嘗試 models/gemini-1.5-flash 失敗：{e}")
        # 如果上面都唔得，試吓用返唔加 models/ 嘅最原始寫法
        try:
            response = client.models.generate_content(
                model='gemini-1.5-flash', 
                contents="Hello Brian! (Second Try)"
            )
            print(response.text)
        except Exception as e2:
            print(f"第二次嘗試都失敗：{e2}")

if __name__ == "__main__":
    run_report()
