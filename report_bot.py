import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_racing_data():
    # 模擬聽日 4月22日 跑馬地賽事
    return """
    賽事日期: 2026-04-22 (星期三)
    賽場: 跑馬地 (Happy Valley)
    重點場次: 第7場 - 三級賽 (1200米)
    注目馬匹: 1. 英雄豪邁 (穩定), 2. 財駿 (試閘好), 3. 嫡愛心 (強配)
    """

def run_report():
    racing_info = get_racing_data()
    # 換成 Qwen 呢隻中文超強嘅免費模型
    model_name = "alibaba/qwen-2-7b-instruct:free"
    
    try:
        print(f"正在用 Qwen 進行專業分析...")
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "你係一個精通香港賽馬嘅分析師，講廣東話，語氣要似馬評人。"},
                {"role": "user", "content": f"幫我簡單分析聽日跑馬地呢場重點：\n{racing_info}"}
            ],
            extra_headers={
                "HTTP-Referer": "https://github.com/brianlo733/my-ai-agent",
                "X-Title": "Brian AI Agent"
            },
            max_tokens=250
        )
        
        print("--- 🐎 聽日賽馬情報 (Qwen 廣東話版) ---")
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"分析失敗：{e}")

if __name__ == "__main__":
    run_report()
    
    try:
        print(f"正在分析賽馬資訊...")
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "你是一個專業的香港賽馬分析員，請用流利廣東話回答。"},
                {"role": "user", "content": f"根據以下賽馬資料，幫 Brian 總結聽日跑馬地嘅重點：\n{racing_info}"}
            ],
            extra_headers={
                "HTTP-Referer": "https://github.com/brianlo733/my-ai-agent",
                "X-Title": "Brian AI Agent"
            },
            max_tokens=200
        )
        
        print("--- 🐎 聽日賽馬情報 ---")
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"分析失敗：{e}")

if __name__ == "__main__":
    run_report()
