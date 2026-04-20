import os
import requests

def run_report():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ 錯誤：搵唔到 API KEY。")
        return

    # 準備測試清單：嘗試唔同嘅路徑同模型名組合
    # 呢度涵蓋晒所有 Google 認可嘅名
    versions = ["v1beta", "v1"]
    models = ["gemini-1.5-flash", "gemini-1.5-flash-latest", "gemini-1.0-pro"]
    
    racing_data = "跑馬地聽日第7場：英雄豪邁、財駿、嫡愛心。"
    payload = {"contents": [{"parts": [{"text": f"用廣東話簡單分析：{racing_data}"}]}]}
    headers = {'Content-Type': 'application/json'}

    print("🚀 開始全自動 API 路徑掃描...")
    
    success = False
    for v in versions:
        for m in models:
            url = f"https://generativelanguage.googleapis.com/{v}/models/{m}:generateContent?key={api_key}"
            try:
                print(f"嘗試路徑: {v} | 模型: {m} ...", end=" ")
                response = requests.post(url, headers=headers, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    content = result['candidates'][0]['content']['parts'][0]['text']
                    print("✅ 成功！")
                    print("\n" + "="*30)
                    print(f"🐎 賽馬報告 (來自 {m})")
                    print("="*30)
                    print(content)
                    print("="*30)
                    success = True
                    return # 成功就直接收工
                else:
                    print(f"❌ 失敗 (Status: {response.status_code})")
            except Exception as e:
                print(f"💥 出錯")
                continue

    if not success:
        print("\n😭 掃描完畢，所有官方路徑都唔通。")
        print("這通常代表你的 API Key 被 Google 判定為地區不支援，或者 Key 已過期。")

if __name__ == "__main__":
    run_report()
