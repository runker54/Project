#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-12-10
# Author:Runker54
# ----------------------
import smtplib
import requests
from qcloudsms_py import SmsSingleSender
import time
import datetime
import ssl
import pymongo
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtpserver = 'smtp.163.com'
username = '邮箱@163.com'
password = '密码'
email_sender = '邮箱@163.com'
addressee = '邮箱@qq.com'
exit_count = 5

ssl._create_default_https_context = ssl._create_unverified_context

# 短信应用 SDK AppID
app_id = 'app_id'  # SDK AppID 以1400开头

# 短信应用 SDK AppKey
app_key = "app_key"

sms_type = 0  # Enum{0: 普通短信, 1: 营销短信}
sender = SmsSingleSender(app_id, app_key)
# 签名
sms_sign = "签名"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请

my_client = pymongo.MongoClient("mongodb://127.0.0.1:28017/")
my_db = my_client["btc_db"]
my_col = my_db["btc"]


def sendEmail(msg):
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(email_sender, addressee, msg)
    smtp.quit()


def setMsg(msgs):
    msg = MIMEMultipart('mixed')
    msg['Subject'] = '韭菜分报'
    msg['From'] = '邮箱@163.com <邮箱@163.com>'
    msg['To'] = addressee
    text_plain = MIMEText(msgs, 'plain', 'utf-8')
    msg.attach(text_plain)
    return msg.as_string()


while True:
    url = 'https://www.huobi.co/-/x/pro/market/overview5?r=ny2seo'
    data = requests.get(url)
    detail = data.json()
    lowest_money = detail['data'][2]['close']
    lowest_money = float(lowest_money)
    loss_money = round(8000 - lowest_money, 2)
    loss_money = str(loss_money)
    my_dict = {"price": lowest_money, "loss": loss_money, "create_date": datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S")}
    my_col.insert_one(my_dict)
    if lowest_money < 7000 or lowest_money > 8500:
        lowest_money = str(lowest_money)
        params = ['', lowest_money, loss_money, '赶紧抛售！']
        sender.send_with_param(86, 手机号, 346801, params, sign=sms_sign, extend="", ext="")
        msgs = '您现在的韭菜价格为' + lowest_money + ',亏损价格为' + loss_money + ',请及时收割韭菜，建议赶紧抛售'
        sendEmail(setMsg(msgs))
        print(msgs)
    else:
        lowest_money = str(lowest_money)
        msgs = '您现在的韭菜价格为' + lowest_money + ',亏损价格为' + loss_money + ',请及时收割韭菜，建议持续观望'
        sendEmail(setMsg(msgs))
        print(msgs)
    time.sleep(60)