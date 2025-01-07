from googleapiclient.discovery import build
import pickle
import csv

# 保存された認証情報を読み込む
with open('credentials.pkl', 'rb') as token:
    credentials = pickle.load(token)

# Search Console API サービスを作成
service = build('searchconsole', 'v1', credentials=credentials)

# 対象サイトのURLを指定
site_url = 'https://www.kuretom.com/'

# 検索分析データを取得
query_request = {
    'startDate': '2023-12-01',
    'endDate': '2023-12-31',
    'dimensions': ['query'],
    'rowLimit': 50
}

response = service.searchanalytics().query(siteUrl=site_url, body=query_request).execute()

# CSVファイルに保存
csv_file = 'search_analytics_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['検索クエリ', 'クリック数', '表示回数', 'CTR', '平均順位'])
    for row in response.get('rows', []):
        query = row['keys'][0]
        clicks = row.get('clicks', 0)
        impressions = row.get('impressions', 0)
        ctr = row.get('ctr', 0)
        position = row.get('position', 0)
        csvwriter.writerow([query, clicks, impressions, ctr, position])

print(f"データをCSVに保存しました: {csv_file}")
