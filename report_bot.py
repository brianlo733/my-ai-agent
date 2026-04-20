import os
import google.generativeai as genai

# 1. 設置 API
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 2. 換成目前最穩定嘅免費模型 1.5 Flash
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 測試
prompt = "Brian 嘅 AI 助手報告：確認系統連結成功。請用一句話介紹今日係咩日子。"

try:
    # 加少少安全機制
    if not api_key:
        print("錯誤：搵唔到 API Key，請檢查 GitHub Secrets 設定。")
    else:
        response = model.generate_content(prompt)
        print("--- AI 回應開始 ---")
        print(response.text)
        print("--- AI 回應結束 ---")
except Exception as e:
    print(f"仲係有錯誤：{e}")
