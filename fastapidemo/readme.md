# FastAPI

[公式ドキュメント](https://fastapi.tiangolo.com/ja/)


# 仮想環境の構築

```
python3 -m venv fastapidemo
```

```
source fastapidemo/bin/activate
```


# 仮想環境内にライブラリをインストールする

```
pip install fastapi[all]
```

# 実行する

- 開発サーバの起動

```
python main.py
```

- 開発サーバの起動(ホットリロードする場合)

```
python main.py --reload
```

- `uvicorn` を使用する場合

```
uvicorn main:app --reload
```

# SwaggerでDocumentを見る

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

