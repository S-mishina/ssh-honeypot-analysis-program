#2020-12-13 cowrieログ分析について
import pandas as pd
import datetime
import gzip
import datetime
import requests
dt_now = datetime.datetime.now()
year=dt_now.year
mon=dt_now.month
day=dt_now.day
day1=day-1
print(mon)
print(day1)
if mon<=9:
    if day1<=9:
        fname = 'cowrie.json.'+str(year)+'-0'+str(mon)+'-0'+str(day1)
    else:
        fname = 'cowrie.json.'+str(year)+'-0'+str(mon)+'-'+str(day1)
else:
    fname = 'cowrie.json.'+str(year)+'-'+str(mon)+'-'+str(day1)
access = pd.read_json(fname,lines=True)
df=pd.DataFrame(access)
df['timestamp']=pd.to_datetime(df['timestamp'])
#===========================================================#
#ログインしようとしたID（ユーザーネーム）
df1=df.query('eventid == "cowrie.login.failed"')
noid=df1['username'].value_counts()
noid1=df1['username'].value_counts(normalize=True)
print(noid)
print("パスワード頻度")
print(noid1)
#ログインに成功したログ
df2=df.query('eventid == "cowrie.login.success"')
print("ログイン成功回数："+str(len(df2)))
password=df2['password'].value_counts()
password1=df2['password'].value_counts(normalize=True)
print(password)
print("パスワード頻度")
print(password1)
#ログインに失敗したログ
df2=df.query('eventid == "cowrie.login.failed"')
print("ログイン失敗回数："+str(len(df2)))
nopassword=df2['password'].value_counts()
nopassword1=df2['password'].value_counts(normalize=True)
print(nopassword)
print("パスワード頻度")
print(nopassword1)
#実行に成功したコマンド
df3=df.query('eventid == "cowrie.command.input"')
print("実行に成功したコマンド")
print(df3['input'])
#実行に失敗したコマンド
df4=df.query('eventid == "cowrie.command.failed"')
print("実行に失敗したコマンド")
print(df4['input'])
#ダウンロードに成功
df5=df.query('eventid == "cowrie.session.file_download"')
print("ダウンロードに成功したもの")
print(df5['destfile'])
#ダウンロードに成功
print("ダウンロードに失敗したもの")
df6=df.query('eventid == "cowrie.session.file_download.failed"')
print(df6['destfile'])
#===========================================================#
def message1():
    line_notify_token = 'LINEAPI'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = 'メッセージを送信します'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
    print('メッセージの送信')
def message1():
    line_notify_token = 'LINEAPI'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = str(noid)
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
    print('ログインしようとしたID')
def message2():
    line_notify_token = 'LINEAPI'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = str(password)
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
    print('ログインに成功したログ')
def message3():
    line_notify_token = 'LINEAPI'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = str(nopassword)
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
    print('ログインに失敗したログ')
def message4():
    line_notify_token = 'LINEAPI'
    message = str(df3['input'])
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
    print('実行に成功したコマンド')
def message5():
    line_notify_token = 'LINEAPI'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = str(df4['input'])
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
    print('実行に成功したコマンド')
def message6():
    line_notify_token = 'LINEAPI'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = str(df5['destfile'])
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
    print('ダウンロードに成功したコマンド')
message1()
message2()
message3()
message4()
message5()
message6()