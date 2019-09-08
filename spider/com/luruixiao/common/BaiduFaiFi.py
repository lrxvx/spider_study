# encoding=utf-8
import requests
import json

url = "https://fanyi.baidu.com/basetrans"
url_lang = "https://fanyi.baidu.com/langdetect"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36",
    "Cookie": "BAIDUID=A97797477EBA769323882BB4D6D1F9FE:FG=1; BIDUPSID=A97797477EBA769323882BB4D6D1F9FE; PSTM=1552130646; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=2pXMXN3UmhYTU4yT3Y5ckw5a0c1RDY4OFVMZ2pQdjVjN0xtWmN6NGZoYWticjVjQVFBQUFBJCQAAAAAAAAAAAEAAACX2q-jAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKThllyk4ZZcU; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; APPGUIDE_8_0_0=1; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; H_PS_PSSID=1446_21101_29523_29521_29721_29567_29221_26350_29459; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1565425239,1566702826,1567862111,1567905877; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1567862462,1567905898; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1567905898; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1567905898; yjs_js_security_passport=f382b735d048142a739062ebc986d0b19c3e126e_1567905900_js; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=6"
}
# 这两个比较关键
# "token": "ab91302ce8f1341b7c1855742511fa0d",
# "sign":  849138.530371
p_data = {
    "query": "人生孤单，及时行乐",
    "from": "zh",
    "to": "en",
    "token": "ab91302ce8f1341b7c1855742511fa0d",
    "sign":  849138.530371
}
lang_data = {
    "query": "人生孤单"
}


response = requests.post(url, headers=headers, data=p_data)
print(response.content.decode())

# response_lang = requests.post(url_lang, headers=headers, data=lang_data)
# content = json.loads(response_lang.content.decode())
# print(content["lan"])
# print(response_lang.content.decode())