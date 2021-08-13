import sys
from PyPtt import PTT


def ptt_login():
    ptt_id = 'your id'  # your id
    password = 'your password'  # your password

    ptt_bot = PTT.API()
    try:
        ptt_bot.login(ptt_id, password, kick_other_login=True)
    except PTT.exceptions.LoginError:
        ptt_bot.log('登入失敗')
        sys.exit()
    except PTT.exceptions.WrongIDorPassword:
        ptt_bot.log('帳號密碼錯誤')
        sys.exit()
    except PTT.exceptions.LoginTooOften:
        ptt_bot.log('請稍等一下再登入')
        sys.exit()
    ptt_bot.log('登入成功')


ptt_login()
