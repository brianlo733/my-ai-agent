import os
import google.generativeai as genai

# 1. 設置 API
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 2. 用最通用嘅模型名，避開版本偵測問題
# 嘗試用 1.5-flash，如果唔得就用 gemini-pro
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "請用兩句廣東話同 Brian 講聲早晨，並話畀佢聽 AI 已經成功連線。"
    response = model.generate_content(prompt)
    print("--- AI 回應開始 ---")
    print(response.text)
    print("--- AI 回應結束 ---")
except Exception as e:
    print(f"嘗試 1.5-flash 失敗，改用 gemini-pro... 錯誤原因: {e}")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("你好 Brian！")
    print(response.text)
