import os
import google.generativeai as genai

# 1. 由 GitHub Secrets 攞粒 API Key 出嚟
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 2. 揀選模型 (Gemini 2.0 Flash 速度快又免費)
model = genai.GenerativeModel('gemini-2.0-flash')

# 3. 測試指令：叫佢簡單自我介紹
prompt = "你依家係一個由 Brian 開發嘅 AI 助手。請簡單用兩句說話同 Brian 講聲早晨，並確認你已經準備好幫佢處理每日報告。"

try:
    response = model.generate_content(prompt)
    print("--- AI 回應開始 ---")
    print(response.text)
    print("--- AI 回應結束 ---")
except Exception as e:
    print(f"出咗錯喇：{e}")
