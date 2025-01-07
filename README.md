
# Google Search Console データ取得ツール

このプロジェクトは、Google Search Console API から認証、サイトリストの取得、データクエリを行うための Python スクリプトを提供します。指定されたウェブサイトの検索アナリティクスデータを取得し、結果を CSV ファイルに保存することができます。

このツールは、Google Search Console の検索パフォーマンスデータへのアクセスと分析のプロセスを簡素化することを目的としています。OAuth 2.0 を使用した認証を行い、API と対話するためのステップバイステップのアプローチを提供することで、開発者やウェブマスターがウェブサイトの検索状況についてのインサイトを得やすくしています。

## 関連リンク

このプロジェクトの詳細な背景や使用例については、以下のブログ記事をご覧ください：

- [Pythonで始めるGoogle Search Console API：セットアップから動作確認まで完全解説](https://www.kuretom.com/google-search-console-api-python-guide/)


## 主な機能

- Google API を利用した OAuth 2.0 認証
- Google Search Console に関連付けられたウェブサイトのリスト表示
- 検索アナリティクスデータ（クエリ、クリック数、表示回数、CTR、平均掲載順位）の取得
- さらなる分析のための CSV 形式へのデータエクスポート

## リポジトリ構成

- `client_secret.json`: OAuth 2.0 クライアント設定ファイル(自身のJSONファイルをプロジェクトのディレクトリに格納してください。)
- `step1_authenticate.py`: Google API での認証を行うスクリプト
- `step2_list_sites.py`: Google Search Console に関連付けられたウェブサイトをリストするスクリプト
- `step3_query_data.py`: 検索アナリティクスデータをクエリしてエクスポートするスクリプト
- `requirements.txt`: 依存関係のライブラリ

## 使用手順

### インストール

1. Python 3.6 以上がインストールされていることを確認します。
2. 必要な依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```

### 開始方法

1. **認証**:
   自身のOAuth2.0のシークレットをプロジェクトのルートディレクトリに格納してください。
   `step1_authenticate.py`内の`client_secret.json`の箇所を自身のシークレットのファイル名に置き換えてください。
   認証スクリプトを実行して、資格情報を取得し保存します：
   ```
   python step1_authenticate.py
   ```
   このスクリプトはブラウザウィンドウを開き、Google アカウントで認証を行います。認証が成功すると、資格情報が `credentials.pkl` に保存されます。

2. **関連ウェブサイトのリスト表示**:
   Google Search Console アカウントに関連付けられたウェブサイトを確認します：
   ```
   python step2_list_sites.py
   ```
   このスクリプトは、サイト URL とそれに対応する権限レベルのリストを表示します。

3. **検索アナリティクスデータのクエリ**:
   特定のウェブサイトの検索アナリティクスデータを取得します：
   `https://www.example.com/`の部分は、自身のサイトURLに置き換えて実行してください。
   ```
   python step3_query_data.py
   ```
   `step3_query_data.py` 内の `site_url`、`startDate`、`endDate` 変数を修正して、対象ウェブサイトとデータ取得期間を指定します。

### 設定

`step3_query_data.py` では、以下のパラメータを調整できます：
- `site_url`: 分析対象のウェブサイトの URL
- `startDate` と `endDate`: データ取得期間
- `dimensions`: クエリに含めるディメンション（デフォルトは `['query']`）
- `rowLimit`: 取得する行の最大数（デフォルトは 50）

## 主なユースケース

- **月次検索パフォーマンスレポート**:
  `step3_query_data.py` の日付範囲を前月に設定し、スクリプトを実行して月次の検索パフォーマンスデータを含む CSV ファイルを生成します。

- **上位パフォーマンスクエリの特定**:
  `step3_query_data.py` の `rowLimit` を高い値（例：1000）に設定し、より多くのクエリを取得します。その後、クリック数や表示回数でソートして、上位の検索キーワードを特定します。

## トラブルシューティング

### 認証エラー

**問題**: `step1_authenticate.py` 実行時に「無効なクライアントシークレットファイル」エラーが発生  
**解決策**:  
- `client_secret_*.json` ファイルがスクリプトと同じディレクトリにあることを確認してください。
- スクリプト内のファイル名が実際のファイル名と一致していることを確認してください。

### データが空

**問題**: 特定のサイトをクエリした際にデータが返されない  
**診断手順**:  
1. `step3_query_data.py` 内の `site_url` が `step2_list_sites.py` でリストされた URL と完全に一致しているか確認します。
2. 指定した日付範囲が、データが存在する期間を含んでいるか確認します。
3. 指定されたサイトに対して Google Search Console 内で必要な権限を持っていることを確認します。

## データフロー

このアプリケーションのデータフローは以下の手順に従います：

1. **ユーザー認証** (`step1_authenticate.py`)
2. **資格情報の保存** (`credentials.pkl`)
3. **サイトリストの取得** (`step2_list_sites.py`)
4. **データのクエリ** (`step3_query_data.py`)
5. **CSV ファイルの出力** (`search_analytics_data.csv`)

```
[ユーザー] -> [認証] -> [資格情報の保存]
                                     |
                                     v
[Google Search Console API] <-> [サイトリストの取得]
                                     |
                                     v
                              [データのクエリ]
                                     |
                                     v
                              [CSV 出力]
```

**注意**: クエリを実行するサイトに対して Google Search Console で必要な権限を持っていることを確認してください。このデータフローは、各ステップで認証と承認が成功することを前提としています。
