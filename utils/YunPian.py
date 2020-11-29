import requests
import json


def single_send_sms(apiKey, code, mobile):
    url = 'https://sms.yunpian.com/v2/sms/single_send.json'
    text = '【陈湉test】您的验证码是{}。如非本人操作，请忽略本短信'.format(code)
    res = requests.post(url, data={
        'apikey': apiKey,
        'code': code,
        'mobile': mobile,
        'text': text
    })
    return json.loads(res.text)


if __name__ == '__main__':
    res = single_send_sms('6624878a09526a06579ad51e44ac7986', '877666', '15827196096')
    print(res)
    code = res['code']
    msg = res['msg']
    if code == 0:
        print('发送成功')
    else:
        print('发送失败')
