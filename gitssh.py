# -*- coding: utf-8 -*-
import time
from datetime import datetime
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
#2020-12-13 cowrieログ分析について
import pandas as pd
import datetime
import gzip
import datetime
#=======ハニーポットWordPress書き込みプログラム=========#
#=======各種設定=========#
id="WordPressID"
password="PASS"
url="#WordPressURL/xmlrpc.php"
which="publish"
#which="draft"
wp = Client(url, id,password)
#=======================#
#===========ハニーポットログ分析プログラム=================
dt_now = datetime.datetime.now()
year=dt_now.year
mon=dt_now.month
day=dt_now.day
if day!=1:
    day1=day-1
elif day==1:
    if mon==1:
        mon=12
        day1=31
    elif mon==2:
        mon=mon-1
        day1=28
    elif mon==3 and mon==5 and mon==7 and mon==8 and mon==10:
        mon=mon-1
        day1=31
    else:
        mon=mon-1
        day1=30
print(mon)
print(day1)
if mon==12 and day1==31:
    year=year-1
if mon<=9:
    fname = 'cowrie.json.'+str(year)+'-0'+str(mon)+'-'+str(day1)
    if day1<=9:
        fname = 'cowrie.json.'+str(year)+'-0'+str(mon)+'-0'+str(day1)
    else:
        fname = 'cowrie.json.'+str(year)+'-0'+str(mon)+'-'+str(day1)
elif mon>=9:
    if day1<=9:
        fname = 'cowrie.json.'+str(year)+'-'+str(mon)+'-0'+str(day1)
    else:
        fname = 'cowrie.json.'+str(year)+'-'+str(mon)+'-'+str(day1)
print(fname)
access = pd.read_json(fname,lines=True)
df=pd.DataFrame(access)
df['timestamp']=pd.to_datetime(df['timestamp'])
#ログインに失敗したID
df1=df.query('eventid == "cowrie.login.failed"')
noid=df1['username'].value_counts()
print(noid)
#ログインに成功したPASS
df2=df.query('eventid == "cowrie.login.success"')
print("ログイン成功回数："+str(len(df2)))
password=df2['password'].value_counts()
print(password)
#ログインに失敗したPASS
df3=df.query('eventid == "cowrie.login.failed"')
print("ログイン失敗回数："+str(len(df3)))
nopassword4=df3['password'].value_counts()
print(nopassword4)
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
#=================================================================================
#===========================ブログ書き込み===========================================
post = WordPressPost()
post.post_status = which
post.title =str(year)+'-'+str(mon)+'-'+str(day)
post.content = "<h2>ログインに失敗したID</h2>"+"<br>"+str(noid)+"<br><br>"+"<h2>ログインに成功したPASS</h2>"+"<br>"+str(password)+"<br><br>"+"<h2>ログインに失敗したPASS</h2>"+"<br>"+str(nopassword4)+"<br><br>"+"<h2>実行に成功したコマンド</h2>"+"<br>"+str(df3['input'])+"<br><br>"+"<h2>実行に失敗したコマンド</h2>"+"<br>"+str(df4['input'])+"<br><br>"+"<h2>ダウンロードしたファイル</h2>"+"<br>"+str(df5['destfile'])
wp.call(NewPost(post))

#参考URL
#https://np-sys.com/pythonでwordpressに自動で投稿する（python-wordpress-xmlrpc）/
