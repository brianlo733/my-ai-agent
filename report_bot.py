import os
from openai import OpenAI

# 1. 設置 OpenRouter API
client = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_racing_data():
    # 呢度模擬抓取到嘅賽馬排位或重點資訊 (之後可以再加強爬蟲部分)
    # 假設係聽日 4月22日 跑馬地嘅資訊
    mock_data = """
    賽事日期: 2026-04-22 (星期三)
    賽場: 跑馬地 (Happy Valley)
    重點場次: 第7場 - 三級賽 (1200米)
    注目馬匹: 
    1. 英雄豪邁 (表現穩定)
    2. 財駿 (近日試閘出色)
    3. 嫡愛心 (強勢配搭)
    """
    return mock_data

def run_report():
    racing_info = get_racing_data()
    
    # 我哋用 Llama 3.1 8B 做測試，指令寫清楚啲等佢唔好「short short 哋」
    model_name = "meta-llama/llama-3.1-8b-instruct"
    
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
