from googleapiclient.discovery import build
import pickle

# 保存された認証情報を読み込む
with open('credentials.pkl', 'rb') as token:
    credentials = pickle.load(token)

# Search Console API サービスを作成
service = build('searchconsole', 'v1', credentials=credentials)

# サイト一覧を取得
response = service.sites().list().execute()
print("サイト一覧:")
for site in response['siteEntry']:
    print(f"サイトURL: {site['siteUrl']}, 権限レベル: {site['permissionLevel']}")
