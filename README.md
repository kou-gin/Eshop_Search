# Eshop_Search

Eshop_Search は、地域・カテゴリ・店名で飲食店を検索・管理できる個人向けブックマークWebアプリです。  
自分のお気に入り飲食店をブラウザから素早く探せるよう設計されています。  

---

## 🔧 主な機能

- ✅ 地域による検索（例：東京、横浜など）
- ✅ 店名の部分一致検索
- ✅ カテゴリ検索（AND/OR 自動切り替え）
- ✅ 管理画面からの飲食店情報の追加・編集・削除
- ✅ Bootstrap によるスマホ対応UI
- ✅ Basic認証による管理者制限
- ✅ アクセスログ・エラーログの記録

---

## 🌐 公開URL

- 🔍 ユーザー画面（検索）  
  https://gins-net25.sakura.ne.jp/eshop_search

- 🛠 管理画面（Basic認証あり）  
  https://gins-net25.sakura.ne.jp/eshop_manage

---

## 🛠 使用技術

| 技術       | 内容                      |
|------------|---------------------------|
| Python     | Flask + flup（CGI WSGI） |
| HTML/CSS   | Bootstrap 4               |
| データベース | MySQL                     |
| その他     | dotenv, BeautifulSoup, tqdm など |

---

## 📂 ディレクトリ構成

```
Eshop_Search/
├── app/
│ ├── app.py
│ ├── dao/
│ ├── model/
│ ├── static/
│ ├── templates/
│ ├── log/
│ ├── lib/ ← Git管理外（共有サーバー用ライブラリ）
│ ├── .env ← Git管理外（Basic認証情報）
│ └── .env.example ← 公開用テンプレート
├── .gitignore
├── .htaccess
└── index.cgi
```

---

## 🚀 セットアップ手順

### 1. このリポジトリをクローン

```
git clone https://github.com/kou-gin/Eshop_Search.git
cd Eshop_Search
```
### 2. 必要なライブラリをインストール（共有サーバー向け）
```
pip install -r requirements.txt --target=app/lib
```
### 3. .env を作成
```
cp app/.env.example app/.env
# 中身を編集して Basic認証用のIDとパスを設定
```
## 環境変数の設定

接続情報や認証情報は .env にまとめており、GitHubには含めていません。  
.env.example を参考に、自分の環境用に .env を作成してください。

アプリケーションでは `python-dotenv` を使用して `.env` を読み込んでおり、  
**`db_connector.py` などで MySQL 接続情報として利用されています。**

### ■サーバー設置例（さくらの共用レンタルサーバー）
```
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ index.cgi/$1 [QSA,L]
```


## 📦 サンプルデータ

このアプリには、MySQL用のテーブル定義と初期データが付属しています：

- `create_tables.sql`：テーブル構造（categories, eshops）
- `sample_data.sql`：カテゴリ・飲食店の初期データ

ローカル環境でMySQLに取り込む場合は以下のように実行します：

```bash
mysql -u youruser -p yourdb < create_tables.sql
mysql -u youruser -p yourdb < sample_data.sql
