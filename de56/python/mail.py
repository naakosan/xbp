import requests
import feedparser
from datetime import datetime
from dateutil.relativedelta import relativedelta
import win32com.client

# RSSフィードのURL（Yahoo!ニュース トップ）
RSS_URL = "https://news.yahoo.co.jp/rss/topics/top-picks.xml"

# RSSフィードからニュースを取得
def get_japanese_news():
    try:
        feed = feedparser.parse(RSS_URL)
        if feed.entries:
            news_list = [
                f"{entry.published}: {entry.title}\n{entry.link}"
                for entry in feed.entries[:5]  # 上位5件のニュースを取得
            ]
            return "\n\n".join(news_list)
        else:
            return "ニュースを取得できませんでした。"
    except Exception as e:
        print(f"ニュース取得エラー: {e}")
        return "ニュース取得中にエラーが発生しました。"

# Wayback MachineのAPIで過去のURLを取得
def get_wayback_url(base_url, target_date):
    wayback_api = "http://archive.org/wayback/available"
    params = {"url": base_url, "timestamp": target_date}
    try:
        response = requests.get(wayback_api, params=params)
        if response.status_code == 200:
            data = response.json()
            snapshots = data.get("archived_snapshots", {})
            closest = snapshots.get("closest", {})
            if closest:
                return closest["url"]
            else:
                return None
        else:
            print(f"Wayback Machine APIエラー: ステータスコード {response.status_code}")
            return None
    except Exception as e:
        print(f"Wayback Machineリクエストエラー: {e}")
        return None

# Wayback MachineのURLからニュース情報をスクレイプ
def scrape_news_from_wayback(wayback_url):
    # 実際にニュースをスクレイプする処理をここに追加
    # 現時点ではサンプルとしてダミーのニュースを返す
    return f"過去のニュース（{wayback_url}）を取得しました。"

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
    # 10年前の日付を正確に計算
    ten_years_ago = datetime.now() - relativedelta(years=10)
    today = ten_years_ago.strftime("%Y年%m月%d日")
    
    # Wayback Machineで10年前のアーカイブURLを取得
    base_url = "https://news.yahoo.co.jp/topics"
    target_date = ten_years_ago.strftime("%Y%m%d")  # 10年前の日付をYYYYMMDD形式で取得
    
    # Wayback Machineから10年前のYahoo!ニュースのアーカイブURLを取得
    wayback_url = get_wayback_url(base_url, target_date)
    if wayback_url:
        news = scrape_news_from_wayback(wayback_url)
    else:
        news = "10年前のアーカイブが見つかりませんでした。"

    # メールの件名と本文を設定
    subject = f"10年前の今日 ({today}) の日本のニュース"
    body = f"10年前の{today}の最新日本ニュース:\n\n{news}"

    # 送信先メールアドレスを指定
    to_email = "r202401795pu@jindai.jp"
    send_outlook_email(subject, body, to_email)

if __name__ == "__main__":
    main()
