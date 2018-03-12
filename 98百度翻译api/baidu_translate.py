import requests
import random

def generat_MD5(str):
    import hashlib
    h1 = hashlib.md5()
    h1.update(str.encode(encoding='utf-8'))
    return h1.hexdigest()


reference_dict = {'中文': 'zh', '英语': 'en', '粤语': 'yue', '文言文': 'wyw', '日语': 'jp',
                      '韩语': 'kor', '法语': 'fra', '西班牙语': 'spa', '泰语': 'th', '阿拉伯语': 'ara',
                      '俄语': 'ru', '葡萄牙语': 'pt', '德语': 'de', '意大利语': 'it', '希腊语': 'el',
                      '荷兰语': 'nl', '波兰语': 'pl', '保加利亚语': 'bul', '爱沙尼亚语': 'est', '丹麦语': 'dan',
                      '芬兰语':'fin', '捷克语': 'cs', '罗马尼亚语': 'rom', '斯洛文尼亚语': 'slo', '瑞典语': 'swe', '匈牙利语': 'hu',
                      '繁体中文': 'cht', '越南语': 'vie', '自动检测': 'auto'}
url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
q = 'apple'
from_ = reference_dict['自动检测']
to = reference_dict['中文']
appid = str(20180312000134378)
salt = random.randint(32768, 65536)
s_key = 'htvikWKgtRfKNkrct038'
try:
    sign = generat_MD5(appid + q + str(salt) + s_key)
    data = {'q': q, 'from': from_, 'to': to, 'appid': appid, 'salt': salt, 'sign': sign}
    response = requests.get(url, params=data)
    result = response.json()
    assert 'trans_result' in result.keys(), result['error_msg']
except requests.ConnectionError as e:
    result = e
except AssertionError as f:
    result = f

