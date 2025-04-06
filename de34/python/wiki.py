import requests
from datetime import datetime, timedelta
import win32com.client

# 10年前の日付を計算
today = datetime.now()
ten_years_ago = today - timedelta(days=365 * 10)

# 10年前の出来事を取得
def get_historical_events(date):
    url = f"https://history.muffinlabs.com/date/{date.month}/{date.day}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('Events', [])
        else:
            print(f"APIエラー: ステータスコード {response.status_code}")
            return []
    except Exception as e:
        print(f"APIリクエストエラー: {e}")
        return []

# Outlookを使用したメール送信関数
def send_outlook_email(subject, body, to_email):
    try:
        outlook = win32com.client.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)  # 0はメールアイテムを示す
        mail.To = to_email
        mail.Subject = subject
        mail.Body = body
        mail.Send()
        print("Outlook経由でメールが送信されました。")
    except Exception as e:
        print(f"Outlookメール送信エラー: {e}")

# メイン処理
def main():
    events = get_historical_events(ten_years_ago)
    
    if events:
        event_details = "\n".join([f"{event['year']}: {event['text']}" for event in events])
        subject = f"10年前の今日 ({ten_years_ago.strftime('%Y-%m-%d')}) の出来事"
        body = f"10年前の{ten_years_ago.strftime('%Y-%m-%d')}に起こった出来事:\n\n{event_details}"
    else:
        subject = f"10年前の今日 ({ten_years_ago.strftime('%Y-%m-%d')}) の出来事"
        body = "10年前の今日の出来事は取得できませんでした。"

    # 送信先メールアドレスを指定
    to_email = "r202401795pu@jindai.jp"
    send_outlook_email(subject, body, to_email)

if __name__ == "__main__":
 main()