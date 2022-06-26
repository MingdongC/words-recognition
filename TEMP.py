from aip import AipOcr
import base64
import requests

def shibie(ImgName):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=QXmsQXjmyaCaAap09hKaZOGS&client_secret=HWROy2A05Gkjq29N5w4phNGxbHerTjPS'
    response = requests.get(host)
    if response:
        print(response.json())

    app_id = '23614408'
    api_key = 'QXmsQXjmyaCaAap09hKaZOGS'
    secret_key = 'HWROy2A05Gkjq29N5w4phNGxbHerTjPS'
    # client = AipOcr(app_id,api_key,secret_key)

    request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage'
    filePath = 'E:\\PycharmProjects\\wenzishibie\\' + ImgName

    def getImage(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = base64.b64encode(getImage(filePath))

    params = {'image':image}
    access_token = '24.8458397cb28788d88c80f7cc4ffc7fe9.2592000.1614577513.282335-23614408'

    request_url = request_url + '?access_token=' + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    #图片处理部分，不用可注释掉
    tempText = response.text
    tempText = tempText.replace('"words":', '\n')
    tempText = tempText.replace('[{', '')
    tempText = tempText.replace('},', '')
    tempText = tempText.replace('{', '')
    tempText = tempText.replace('"', '')
    tempText = tempText.replace(']', '')
    tempText = tempText.replace('}', '')
    tempText = tempText.replace(' ', '')
    return tempText

with open('新建文本文档.txt', 'w') as f:
    ImgName = ' '
    while(ImgName != '结束.png'):
        ImgName = input('请输入图片文件的名字：') + '.png'
        if ImgName != '结束.png':
            tempText = shibie(ImgName)
            f.write(tempText)
            f.write('\n')
            f.write('=================================================================')
            print(ImgName, '的写入结束啦！')
    f.close()

# if response:
#     print (response.json())

if __name__ == '__main__':
    print()


