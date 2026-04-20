import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_racing_data():
    return """
    賽事日期: 2026-04-22 (星期三)
    賽場: 跑馬地 (Happy Valley)
    重點場次: 第7場 - 三級賽 (1200米)
    注目馬匹: 1. 英雄豪邁 (穩定), 2. 財駿 (試閘好), 3. 嫡愛心 (強配)
    """

def run_report():
    racing_info = get_racing_data()
    
    # 呢兩個係 OpenRouter 目前最有效嘅免費中文模型 ID
    models_to_try = [
        "qwen/qwen-2-7b-instruct:free",
        "google/gemini-flash-1.5-8b:free",
        "meta-llama/llama-3.1-8b-instruct:free"
    ]
    
    for model_name in models_to_try:
        try:
            print(f"正在嘗試模型：{model_name}...")
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": "你係一個精通香港賽馬嘅分析師，用流利廣東話回答。"},
                    {"role": "user", "content": f"幫我簡單總結聽日跑馬地呢場重點，唔好講廢話：\n{racing_info}"}
                ],
                extra_headers={
                    "HTTP-Referer": "https://github.com/brianlo733/my-ai-agent",
                    "X-Title": "Brian AI Agent"
                },
                max_tokens=300
            )
            
            print(f"--- 🐎 聽日賽馬情報 ({model_name}) ---")
            print(response.choices[0].message.content)
            return # 成功就收工
            
        except Exception as e:
            print(f"{model_name} 失敗：{e}")
            continue

if __name__ == "__main__":
    run_report()
