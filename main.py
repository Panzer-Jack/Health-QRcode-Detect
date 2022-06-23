from pyzbar import pyzbar
import requests
import cv2
import ast

cap = cv2.VideoCapture(0)
isOpened = cap.isOpened()

while isOpened:
    try:
        flag, frame = cap.read()
        bacodes = pyzbar.decode(frame, symbols=[pyzbar.ZBarSymbol.QRCODE])
        for bacode in bacodes:
            url = bacode.data.decode("UTF-8")

            uid = url[str(url).find(".cn/") + 4:]
            tar_url = f"https://suishenmafront1.sh.gov.cn/smzy/yqfkewm/ssm/ewmcheck?uid={uid}"

            tar_req = requests.get(tar_url, 'lxml')
            tar_req.encoding = 'utf-8'
            tar_json = ast.literal_eval(tar_req.json()["data"])["type"]
            # print(tar_url)
            # print(url)
            if tar_json == "00":
                print("绿码 通行。")
            else:
                print("健康码 有风险 请等待工作人员核查！")
    except TypeError:
        print("TypeError !!")
        pass

    if cv2.waitKey(1) == ord("q"):
        break

