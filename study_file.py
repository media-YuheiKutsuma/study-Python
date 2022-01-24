# ファイル監視＆メールで通知
import glob
import time
import smtplib
from email.mime.text import MIMEText

FROM = '***@gmail.com'
TO = '***@gmail.com'
PASS = '**'

mail = MIMEText('ファイルが更新されました')
mail['Subject'] = 'System Report' # 件名
mail['From'] = FROM # 送信元
mail['To'] = TO # 送信先

# ファイル監視
old_file = set(glob.glob('*'))
print(old_file)

while True:
    time.sleep(2)
    new = set(glob.glob('*'))
    if added := new - old_file:
        print(f'{"Added":10}', added)
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo() # EHLOコマンド
            smtp.starttls() # TLSで接続
            smtp.ehlo() # EHLOコマンド
            smtp.login(FROM, PASS) # ログイン
            smtp.sendmail(FROM, TO, mail.as_string()) # メール送信
    if remove := old_file - new:
        print(f'{"Remove":10}', remove)
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo() # EHLOコマンド
            smtp.starttls() # TLSで接続
            smtp.ehlo() # EHLOコマンド
            smtp.login(FROM, PASS) # ログイン
            smtp.sendmail(FROM, TO, mail.as_string()) # メール送信

    old_file = new

    


