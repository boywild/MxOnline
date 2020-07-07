import requests


def single_send_sms(apiKey, code, mobile):
    url = 'https://sms.yunpian.com/v2/sms/single_send.json'
    text = '【陈湉test】您的验证码是{}。如非本人操作，请忽略本短信'.format(code)
    res = requests.post(url, data={
        'apikey': apiKey,
        'code': code,
        'mobile': mobile,
        'text': text
    })
    return res


if __name__ == '__main__':
    res = single_send_sms('6624878a09526a06579ad51e44ac7986', '123456', '15827196096')
    import json

    res_json = json.loads(res.text)
    code = res_json['code']
    msg = res_json['msg']
    if code == 0:
        print('发送成功')
    else:
        print('发送失败')
    print(res.text)
