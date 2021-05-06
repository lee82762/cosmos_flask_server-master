import errno
import os

from flask import Flask, jsonify
from flask import request
from xml.etree.ElementTree import Element, SubElement, ElementTree

import urllib3
import json
from collections import OrderedDict

answer = ''
jsonString = OrderedDict()
analysis_data = ""


class morpAPI2:
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
    accessKey = "9cf5e5b7-55b3-4369-9921-726d59b3b6e5"
    analysisCode = "morp"  # 개체명 분석 코드
    text = "기본"  # 분석할 대상
    data = ""  # api를 통해서 받은 분석결과 json
    result = ""  # data를 리스트로 변환한 분석결과변수-변수이름 고치기
    k = 0


    def __init__(self, userFile):

        self.text = self.setText(userFile)
        print(type(self.text))
        print("현재분석코드 " + self.analysisCode)
        print("현재분석문장 " + self.text)
        self.data = self.setData()
        self.result = self.result(self.data)

    '''
    사용자가 분석할 텍스트 파일 저장
    '''

    def setText(self, userFile):

        '''
        myFile = open(userFile, "r", encoding="utf-8")
        self.text = myFile.read()
        return self.text
        '''
        # '''
        self.text = userFile
        return self.text
        # '''

    '''
    api로부터 json 값을 가져오기
    '''

    def setData(self):
        requestJson = {
            "access_key": self.accessKey,
            "argument": {
                "text": self.text,
                "analysis_code": self.analysisCode
            }
        }

        http = urllib3.PoolManager()

        response = http.request(
            "POST",
            self.openApiURL,
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps(requestJson)  # json파일로 api를 받음
        )

        self.data = str(response.data, "utf-8")
        return self.data

    '''
    josn데이터에서 필요한 데이터값 가져오기
    '''

    def result(self, data):
        test = json.loads(data)
        self.result = test['return_object']['sentence']
        return self.result

    '''
    형태소 분석부분
    '''

    def showMorp2(self, analysis_data=dict()):
        test = ''
        print("형태소분석결과 ")
        strnum = len(self.result)  # 총문장갯수
        print(strnum)
        morpnum = len(self.result[0]['morp'])  # 하나의 문장당 형태소 갯수
        print(morpnum)

        wordnum = len(self.result[0]['word'])  # 하나의 문장단 단어 갯수
        print(wordnum)

        analysis_data['key'] = list()
        analysis_data['value'] = list()

        with open('morpAPI.txt', 'w', encoding="utf-8") as make_file:
            for i in range(strnum):
                for j in range(morpnum - 1):
                    str = ''

                    # str = self.result[i]['morp'][j]['lemma'] + ":" + self.result[i]['morp'][j]['type']

                    analysis_data['key'].append(self.result[i]['morp'][j]['lemma'])
                    analysis_data['value'].append(self.result[i]['morp'][j]['type'])
                    jsonString = json.dumps(analysis_data, ensure_ascii=False, indent=4)

                    if self.result[i]['morp'][j]['position'] - self.result[i]['morp'][j - 1]['position'] == 4:

                        print("  ", end="")
                        # answer += "  "
                        print(str, end="")
                        # answer += str

                    else:
                        # str=str.replace("\"\"",)
                        print(str, end="")
                        # answer += str

                    json.dump(str, make_file, ensure_ascii=False, indent=4)

        myFile = open("C:/Users/이재범/PycharmProjects/cosmos_flask_server - master/cosmos_flask_server - master/형태소분석/morpAPI.txt", "r", encoding="utf-8")
        # myFile = open("C:\\Users\\User\\PycharmProjects\\Cosmos\\형태소분석\\morpAPI.txt", "r", encoding="utf-8")

        text = myFile.readline()
        print("\n")
        print(type(test))
        print("\n")
        print(test)
        '''
        if self.text==" + ":
            self.text=self.text.replace("  + "," aa")
        else :
            self.text=self.text.replace("\"","")
            print(self.text)

       # print(self.text)
        self.text=self.text.replace("\"","")
        self.setOutput(self.text)

        '''
        text = text.replace("\"\"", " / ")

        text = text.replace("\"\"", " /")
        text = text.replace("\"", "")

        print("\n")
        print(type(text))
        print(text)
        print("\n")

        # print(text)
        self.setOutput(text)

        # print(answer)
        # return answer

        return jsonString

        # return jsonString

    def setOutput(self, str):
        with open('morpAPI.txt', 'w', encoding="utf-8") as make_file:
            json.dump(str, make_file, ensure_ascii=False, indent=4)


class morpAPI:
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
    accessKey = "9cf5e5b7-55b3-4369-9921-726d59b3b6e5"
    analysisCode = "morp"  # 개체명 분석 코드
    text = "기본"  # 분석할 대상
    data = ""  # api를 통해서 받은 분석결과 json
    result = ""  # data를 리스트로 변환한 분석결과변수-변수이름 고치기
    k = 0

    def __init__(self, userFile):

        self.text = self.setText(userFile)
        print(type(self.text))
        print("현재분석코드 " + self.analysisCode)
        print("현재분석문장 " + self.text)
        self.data = self.setData()
        self.result = self.result(self.data)

    '''
    사용자가 분석할 텍스트 파일 저장
    '''

    def setText(self, userFile):

        '''
        myFile = open(userFile, "r", encoding="utf-8")
        self.text = myFile.read()
        return self.text
        '''
        # '''
        self.text = userFile
        return self.text
        # '''

    '''
    api로부터 json 값을 가져오기
    '''

    def setData(self):
        requestJson = {
            "access_key": self.accessKey,
            "argument": {
                "text": self.text,
                "analysis_code": self.analysisCode
            }
        }

        http = urllib3.PoolManager()

        response = http.request(
            "POST",
            self.openApiURL,
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps(requestJson)  # json파일로 api를 받음
        )

        self.data = str(response.data, "utf-8")
        return self.data

    '''
    josn데이터에서 필요한 데이터값 가져오기
    '''

    def result(self, data):
        test = json.loads(data)
        print(test)
        self.result = test['return_object']['sentence']
        return self.result

    '''
    형태소 분석부분
    '''

    def showMorp(self, answer=""):  # analysis_data = dict()):
        test = ''
        print("형태소분석결과 ")
        strnum = len(self.result)  # 총문장갯수
        print(strnum)
        morpnum = len(self.result[0]['morp'])  # 하나의 문장당 형태소 갯수
        print(morpnum)

        wordnum = len(self.result[0]['word'])  # 하나의 문장단 단어 갯수
        print(wordnum)

        # analysis_data['key'] = list()
        # analysis_data['value'] = list()

        with open('morpAPI.txt', 'w', encoding="utf-8") as make_file:
            for i in range(strnum):
                for j in range(morpnum - 1):
                    str = ''

                    str = self.result[i]['morp'][j]['lemma'] + ":" + self.result[i]['morp'][j]['type']

                    # analysis_data['key'].append(self.result[i]['morp'][j]['lemma'])
                    # analysis_data['value'].append(self.result[i]['morp'][j]['type'])
                    # jsonString = json.dumps(analysis_data, ensure_ascii=False, indent=4)

                    if self.result[i]['morp'][j]['position'] - self.result[i]['morp'][j - 1]['position'] == 4:

                        print("  ", end="")
                        answer += "  "
                        print(str, end="")
                        answer += str

                    else:
                        # str=str.replace("\"\"",)
                        print(str, end="")
                        answer += str

                    json.dump(str, make_file, ensure_ascii=False, indent=4)

        # myFile = open("C:\\Users\\User\\PycharmProjects\\Cosmos\\morpAPI.txt", "r", encoding="utf-8")
        myFile = open("C:/Users/이재범/PycharmProjects/cosmos_flask_server-master/cosmos_flask_server-master/morpAPI.txt", "r", encoding="utf-8")


        text = myFile.readline()
        print("\n")
        print(type(test))
        print("\n")
        print(test)
        '''
        if self.text==" + ":
            self.text=self.text.replace("  + "," aa")
        else :
            self.text=self.text.replace("\"","")
            print(self.text)

       # print(self.text)
        self.text=self.text.replace("\"","")
        self.setOutput(self.text)

        '''
        text = text.replace("\"\"", " / ")

        text = text.replace("\"\"", " /")
        text = text.replace("\"", "")

        print("\n")
        print(type(text))
        print(text)
        print("\n")

        # print(text)
        self.setOutput(text)

        print(answer)
        return answer

        # return jsonString

    def setOutput(self, str):
        with open('morpAPI.txt', 'w', encoding="utf-8") as make_file:
            json.dump(str, make_file, ensure_ascii=False, indent=4)


# if __name__ == "__main__":
#     hi = morpAPI("C:\\Users\\User\\PycharmProjects\\Cosmos\\text1.txt")
#     hi.showMorp()

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     hi = morpAPI("C:\\Users\\User\\PycharmProjects\\Cosmos\\text1.txt")
#     morpResult = hi.showMorp()
#
#     return morpResult

@app.route('/')
def hello_world():
    hi = morpAPI(
        "엑소브레인은 내 몸 바깥에 있는 인공 두뇌라는 뜻으로, 세계 최고인공지능 기술 선도라는 비전을 달성하기 위한 과학기술정보통신부 소프트웨어 분야의 국가 혁신기술 개발형 연구개발 과제이다.")
    morpResult = hi.showMorp()

    return morpResult

class AnalysisAPI():
    morp = ""
    code = ""


@app.route("/cosmos/KStars/morp")
def cosmos_morp():
    data = request.json
    print(data)
    hi = morpAPI2(data['text'])
    moreResult = hi.showMorp2()

    data['analysisResult'] = moreResult
    print(type(data['analysisResult']))
    print(data['analysisResult'])
    return jsonify(data)

@app.route("/cosmos/KStars/morpList", methods=['POST'])
def cosmos_morp_board():
    data = request.json
    for i in range(len(data)):
        analysis = morpAPI2(data[i]['text'])
        resultList = analysis.showMorp2()
        data[i]['analysisResult'] = resultList

    return jsonify(data)


@app.route("/test", methods=['POST'])
def test():
    data = request.json
    # print(data)
    hi = morpAPI(data['text'])
    moreResult = hi.showMorp()

    # print(moreResult)
    data['analysisResult'] = moreResult

    return jsonify(data)

@app.route('/cosmos/KStars/create/kst', methods=['POST'])
def cosmos_create_file():
    # request.josn = 스프링에서 restTemplate로 보낸 json데이터를 담는다.
    data = request.json

    print("sdsdsddsds")


    # 기억이 안남
    def indent(node, level=0):
        i = "\n" + level * " " * 4
        if len(node):
            if not node.text or not node.text.strip():
                node.text = i + " " * 4
            if not node.tail or not node.tail.strip():
                node.tail = i
            for node in node:
                indent(node, level + 1)
            if not node.tail or not node.tail.strip():
                node.tail = i
        else:
            if level and (not node.tail or not node.tail.strip()):
                node.tail = i

    # BeautifulSoup 라이브러리를 사용해서 kst 파일 생성.
    # Root = KStars
    root = Element('KStars')

    # <Version>
    SubElement(root, 'Version').text = data['version']

    # <Option>
    Option = SubElement(root, 'Option')
    # <Option> => <SpeakerList>
    for i in range(len(data['m_Option']["speakerList"])):
        SubElement(Option, "SpeakerList").text = data['m_Option']["speakerList"][i]
    # <Option> => <StringOption>
    SubElement(Option, "StringOption").text = data['m_Option']["stringOption"]

    # <Header>
    Header = SubElement(root, 'Header')
    # <Header> => <SpeechType>
    SubElement(Header, "SpeechType").text = data['m_header']['speechType']
    # <Header> => <Participants>
    for i in range(len(data['m_header']['arrParticipants'])):
        SubElement(Header, "Participants").text = data['m_header']['arrParticipants'][i]
    # <Header> => <BirthPlaceofCHI>
    SubElement(Header, "BirthPlaceOfCHI").text = data['m_header']['birthPlaceOfCHI']
    # <Header> => <Location>
    SubElement(Header, "Location").text = data['m_header']['location']
    # <Header> => <Situation>
    SubElement(Header, "Situation").text = data['m_header']['situation']
    # <Header> => <Recording>
    SubElement(Header, "Recording").text = data['m_header']['recording']
    # <Header> => <Transcriber>
    SubElement(Header, "Transcriber").text = data['m_header']['transcriber']
    # <Header> => <Reviewer>
    SubElement(Header, "Reviewer").text = data['m_header']['reviewer']
    # <Header> => <Comment>
    SubElement(Header, "Comment").text = data['m_header']['comment']

    # <Header> => <ID>
    for i in range(len(data['m_header']['arrID'])):
        UserID = SubElement(Header, "ID")
        # <Header> => <ID> => <IDCorpus>
        SubElement(UserID, "IDCorpus").text = data['m_header']['arrID'][i]['corpus']
        # <Header> => <ID> => <IDCode>
        SubElement(UserID, "IDCode").text = data['m_header']['arrID'][i]['code']
        # <Header> => <ID> => <IDDateOfBirth>
        SubElement(UserID, "IDDateOfBirth").text = data['m_header']['arrID'][i]['dateOfBirth']
        # <Header> => <ID> => <IDAge>
        SubElement(UserID, "IDAge").text = data['m_header']['arrID'][i]['age']
        # <Header> => <ID> => <IDSex>
        SubElement(UserID, "IDSex").text = data['m_header']['arrID'][i]['sex']
        # <Header> => <ID> => <IDGroup>
        SubElement(UserID, "IDGroup").text = data['m_header']['arrID'][i]['group']
        # <Header> => <ID> => <IDRegion>
        SubElement(UserID, "IDRegion").text = data['m_header']['arrID'][i]['region']
        # <Header> => <ID> => <IDSES>
        SubElement(UserID, "IDSES").text = data['m_header']['arrID'][i]['ses']
        # <Header> => <ID> => <IDEdu>
        SubElement(UserID, "IDEdu").text = data['m_header']['arrID'][i]['edu']
        # <Header> => <ID> => <IDRole>
        SubElement(UserID, "IDRole").text = data['m_header']['arrID'][i]['role']

    # <Tier type = "KUtterance">
    KUtterance = SubElement(root, "Tier")
    KUtterance.attrib['type'] = data['m_KTierVer2']['dataType']
    # <Tier type = "KUtterance"> => <Data>
    for i in range(len(data['m_KTierVer2']['datas'])):
        DataUtter = SubElement(KUtterance, "Data")
        # <Tier type = "KUtterance"> => <Data uid = "?">
        DataUtter.attrib['uid'] = data['m_KTierVer2']['datas'][i]['uid']
        # <Tier type = "KUtterance"> => <Data uid = "?"> => <Speaker>
        SubElement(DataUtter, 'Speaker').text = data['m_KTierVer2']['datas'][i]['speaker']
        # <Tier type = "KUtterance"> => <Data uid = "?"> => <Text>
        SubElement(DataUtter, 'Text').text = data['m_KTierVer2']['datas'][i]['text']
        # <Tier type = "KUtterance"> => <Data uid = "?"> => <Time>
        SubElement(DataUtter, 'Time').text = data['m_KTierVer2']['datas'][i]['time']

    KMorpheme = SubElement(root, "Tier")
    KMorpheme.attrib['type'] = data['m_KTierMorpVer2']['dataType']
    for i in range(len(data['m_KTierMorpVer2']['datas'])):
        DataMorp = SubElement(KMorpheme, "Data")
        DataMorp.attrib['uid'] = data['m_KTierMorpVer2']['datas'][i]['uid']
        SubElement(DataMorp, 'Speaker').text = data['m_KTierMorpVer2']['datas'][i]['speaker']
        SubElement(DataMorp, 'MEtri').text = data['m_KTierMorpVer2']['datas'][i]['morp']
        SubElement(DataMorp, 'MUser').text = data['m_KTierMorpVer2']['datas'][i]['user']

    Audio = SubElement(root, "Audio")
    for i in range(len(data['m_Audio']['audioPath'])):
        SubElement(Audio, 'AudioPath').text = data['m_Audio']['audioPath'][i]
    SubElement(Audio, 'AudioFileIndex').text = data['m_Audio']['audioFileIndex']
    SubElement(Audio, 'AudioCurrentPosition').text = data['m_Audio']['audioCurrentPosition']
    indent(root)

    print(root)

    tree = ElementTree(root)

    localPath = os.path.abspath("C:/emp")
    print(data['userDto']['user'])



    if data['userDto']['user'] == "guest":
        tree.write(localPath + "\\guest\\temp\\" + data['userDto']['fileName'] + ".kst", encoding="utf-8")
    elif data['userDto']['user'] == "user":
        try:
            if not (os.path.isdir(localPath + "\\user\\" + data['userDto']['id'])):
                os.makedirs(os.path.join(localPath + "\\user\\" + data['userDto']['id']))
                tree.write(localPath + "\\user\\" + data['userDto']['id'] + "\\" + data['userDto']['fileName'] + ".kst",
                           encoding="utf-8")
            if os.path.isdir(localPath + "\\user\\" + data['userDto']['id']):
                tree.write(localPath + "\\user\\" + data['userDto']['id'] + "\\" + data['userDto']['fileName'] + ".kst",
                           encoding="utf-8")
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Failed to create directory!!!!!")
                raise



    return jsonify(data)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
