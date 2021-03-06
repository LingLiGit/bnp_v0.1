import smtplib
from email.mime.text import MIMEText

from bnp.settings import cfg


def pack_info(msg):
    info = f"{msg['date']}\n\n"
    if len(msg['stocks']) == 0:
        info += f"๐ถ๐ถ๐ถ [{msg['algo']}]\n"
    else:
        info += f"๐๐๐ [{msg['algo']}]\n"
        for stock in msg['stocks']:
            if 'algo' in stock:
                info += f"\n{stock['algo']}"
                info += f"\n{stock['ts_code']} {stock['name']} {stock['industry']} {stock['market']}"
                info += "\n"
            else:
                info += f"\n{stock['ts_code']} {stock['name']} {stock['industry']} {stock['market']}"
    # print(info)
    return info


def _send_mail(CONTENT):
    message = MIMEText(CONTENT, 'plain', 'utf-8')
    message['From'] = cfg.MAIL.FROM
    message['To'] = cfg.MAIL.TO
    message['Subject'] = cfg.MAIL.SUBJECT

    try:
        # smtp_obj = smtplib.SMTP()
        # smtp_obj.connect(cfg.MAIL.HOST, 25)

        smtp_obj = smtplib.SMTP_SSL(f'{cfg.MAIL.HOST}:{cfg.MAIL.PORT}')

        smtp_obj.login(cfg.MAIL.USER, cfg.MAIL.PASS)
        smtp_obj.sendmail(cfg.MAIL.SENDER, cfg.MAIL.RECEIVERS, message.as_string())
        smtp_obj.quit()
        print("้ฎไปถๅ้ๆๅ.")
    except smtplib.SMTPException as e:
        print(e)
        print("Error: ๆ ๆณๅ้้ฎไปถ.")


def send_mail(msg):
    CONTENT = pack_info(msg)
    _send_mail(CONTENT)


if __name__ == '__main__':
    # send_mail("ไปๆฅไปฃ็ ")
    msg = {'date': today_str(), 'stocks': [], 'algo': '็ฎๆณ8#A3974'}
    pack_info(msg)
