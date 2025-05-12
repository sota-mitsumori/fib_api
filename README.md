# Fibonacci API

指定したn番目のフィボナッチ数を返すREST API。FastAPIを用いて作成し、Renderでデプロイしました。

## ソースコードの概要

```
GET /fib?={n} 
```
エンドポイントでn番目のフィボナッチ数を返します。ローカル開発、pytestによる自動テスト、Render へのデプロイを想定した構成です。

- 言語・フレームワーク：Python 3 、FastAPI

- テスト：pytest

- デプロイ先：Render Web Service  
https://fib-api-z5x5.onrender.com/ 

## ソースコードの構成

```
.
└── fibonacci-api/
    ├── app/
    │   ├── __init__.py  
    │   ├── main.py                 # FastAPIアプリとルート定義
    │   └── utils.py                # フィボナッチ計算関数部分
    ├── tests/                 
    │   └── test_fib.py             # fib関数のpytest関連
    ├── .gitignore
    ├── requirements.txt
    └── README.md                  


```
## 実行例
10番目のフィボナッチ数、すなわち55を取得したい際には、  
https://fib-api-z5x5.onrender.com/fib?n=10  
にアクセスすることで、以下のようなJSON形式の結果を得られます。

```
{
  "n": 10,
  "result": 55
}
```