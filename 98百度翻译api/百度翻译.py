#conding=utf-8

from tkinter import *
from tkinter import ttk
import requests
import random

def generat_MD5(str):
    import hashlib
    h1 = hashlib.md5()
    h1.update(str.encode(encoding='utf-8'))
    return h1.hexdigest()

def translate(in_str,country1='自动检测', country2='中文'):
    reference_dict = {'中文': 'zh', '英语': 'en', '粤语': 'yue', '文言文': 'wyw', '日语': 'jp',
                      '韩语': 'kor', '法语': 'fra', '西班牙语': 'spa', '泰语': 'th', '阿拉伯语': 'ara',
                      '俄语': 'ru', '葡萄牙语': 'pt', '德语': 'de', '意大利语': 'it', '希腊语': 'el',
                      '荷兰语': 'nl', '波兰语': 'pl', '保加利亚语': 'bul', '爱沙尼亚语': 'est', '丹麦语': 'dan',
                      '芬兰语':'fin', '捷克语': 'cs', '罗马尼亚语': 'rom', '斯洛文尼亚语': 'slo', '瑞典语': 'swe', '匈牙利语': 'hu',
                      '繁体中文': 'cht', '越南语': 'vie', '自动检测': 'auto'}
    error_dict ={'52000': {'meaning': '成功', 'solution': ' '}, '52001':{'meaning': '请求超时', 'solution': '重试'}, '52002':{'meaning': '系统错误', 'solution': '重试'}
        , '52003': {'meaning': '未授权用户', 'solution': '检查您的 appid 是否正确，或者服务是否开通'}, '54000':{'meaning': '必填参数为空', 'solution': '检查是否少传参数'}, '54001':{'meaning': '签名错误', 'solution': '请检查您的签名生成方法'}
        , '54003': {'meaning': '访问频率受限', 'solution': '请降低您的调用频率'}, '54004':{'meaning': '账户余额不足', 'solution': '请前往管理控制平台为账户充值'}, '54005':{'meaning': '长query请求频繁', 'solution': '请降低长query的发送频率，3s后再试'}
        , '58000': {'meaning': '客户端IP非法', 'solution': '检查个人资料里填写的 IP地址 是否正确，可前往管理控制平台修改，IP限制，IP可留空'}, '58001':{'meaning': '译文语言方向不支持', 'solution': '检查译文语言是否在语言列表里'}}
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    q = in_str
    from_ = reference_dict[country1]
    to = reference_dict[country2]
    appid = str(20180312000134378)
    salt = random.randint(32768, 65536)
    s_key = 'htvikWKgtRfKNkrct038'
    try:
        sign = generat_MD5(appid + q + str(salt) + s_key)
        data = {'q': q, 'from': from_, 'to': to, 'appid': appid, 'salt': salt, 'sign': sign}
        response = requests.get(url, params=data)
        result = response.json()
        assert 'trans_result' in result.keys(), {result['error_code']:error_dict[result['error_code']]['meaning']}
    except requests.ConnectionError:
        result = 'error3(连接错误)'
    except AssertionError as a:
        result = a
    return result

root = Tk()
root.title('翻译')

from_test = StringVar()
to_test = StringVar()

Label(root, text='输入词汇', font=("Helvetica", 12, "normal")).grid(row=0, column=0)
Label(root, text='翻译词汇', font=("Helvetica", 12, "normal")).grid(row=1, column=0)

l1 = Label(root, textvariable=from_test, width=3, font=("Helvetica", 12, "normal"))     #创建标签
l1.grid(row=0, column=3)
from_test.set('en')

l2 = Label(root, textvariable=to_test, width=3, font=("Helvetica", 12, "normal"))
l2.grid(row=1, column=3)
to_test.set('zh')

source_text = StringVar()                        #创建输入框
source = Entry(root, textvariable=source_text, width=30, font=("Helvetica", 12, "normal"))
source_text.set(' ')
source.grid(row=0, column=1)

result_text = StringVar()                       #创建翻译窗口
result = Entry(root, textvariable=result_text, width=30, font=("Helvetica", 12, "normal"))
result.grid(row=1, column=1)
result['state'] = 'readonly'

chosen_text1 = StringVar()
chosen1 = ttk.Combobox(root, width=8, textvariable=chosen_text1, font=("Helvetica", 12, "normal"))
chosen1['values'] = ('自动检测', '中文', '英语', '粤语', '文言文', '日语', '韩语', '俄语', '德语', '繁体中文')
chosen1.grid(row=0, column=2)
chosen1.current(0)

chosen_text2 = StringVar()
chosen2 = ttk.Combobox(root, width=8, textvariable=chosen_text2, font=("Helvetica", 12, "normal"))
chosen2['values'] = ('中文', '英语', '粤语', '文言文', '日语', '韩语', '俄语', '德语', '繁体中文')
chosen2.grid(row=1, column=2)
chosen2.current(0)

def on_click():
    # global from_test
    # global to_test

    ss = source_text.get()
    count1 = chosen_text1.get()
    count2 = chosen_text2.get()
    t_result = translate(ss, country1=count1, country2=count2)
    try:
        assert type(t_result) == dict
        from_test.set(t_result['from'])
        to_test.set(t_result['to'])
        result_text.set(t_result['trans_result'][0]['dst'])
    except AssertionError:
        result_text.set(t_result)



Button(root, text="翻译", command=on_click, width=15, font=("Helvetica", 12, "normal")).grid(row=2, column=1)   #创建按钮

root.mainloop()


