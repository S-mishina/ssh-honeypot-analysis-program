from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
#認証
gauth = GoogleAuth()
#ローカルWebサーバとautoを作成
#Googleドライブの認証処理
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
#アップロードするフォルダパス指定
x="cowrie.json.2021-01-09"
f = drive.CreateFile({'title' : x})
#ローカルのファイルをセットしてアップロード
f.SetContentFile(os.path.join(x))
#Googleドライブにアップロード
f.Upload()
f = None
#参考サイト
#