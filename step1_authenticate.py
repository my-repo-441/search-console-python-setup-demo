from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

# スコープを設定
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

# OAuth 2.0 認証フロー
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES)

# ポートを固定してローカルサーバーを起動
credentials = flow.run_local_server(port=8080)

# 認証情報を保存
with open('credentials.pkl', 'wb') as token:
    pickle.dump(credentials, token)