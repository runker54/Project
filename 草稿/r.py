import tkinter
import random
import requests
import request
import urllib
from urllib import request, parse
import time, json, random, hashlib

win = tkinter.Tk()


def pachong():
    try:
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        data = {}

        u = 'fanyideskweb'
        d = content
        f = str(int(time.time() * 1000) + random.randint(1, 10))
        c = 'rY0D^0\'nM0}g5Mm1z%1G4'

        sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

        data['i'] = content  # 需要翻译的内容
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = f
        data['sign'] = sign
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CL1CKBUTTON'
        data['typoResult'] = 'true'
        data = parse.urlencode(data).encode('utf-8')
        req = request.Request(url, data=data)
        response = request.urlopen(req)

        res = response.read().decode('utf-8')
        res = json.loads(res)
        res = res["translateResult"]
        return res[0][0]['tgt']
    except:
        print("cuowu")


def eBtn(event):
    global content
    content = entry_w.get()
    entry_r.config(entry_r, text=content)
    entry_r.delete(0, 80)
    entry_r.insert(0, str(pachong()))
    # pachong()


if __name__ == "__main__":
    label_val_q = tkinter.Label(win, width="80")
    label_val_q.pack(side="top")
    label_val_q.config(label_val_q, text="请输入要翻译的文本")
    entry_w = tkinter.Entry(win, width="80")
    entry_w.pack(side="top")
    btn = tkinter.Button(win, text="翻译")
    btn.pack(side="top")
    btn.bind('<Button-1>', eBtn)

    label_val_q = tkinter.Label(win, width="80")
    label_val_q.pack(side="top")
    label_val_q.config(label_val_q, text="翻译为:")
    entry_r = tkinter.Entry(win, width="80")
    entry_r.pack(side="top")
    entry_r.bind('<Return>', eBtn)
    win.mainloop()
