'''
    result_code : 성공 여부 (성공 : success, 에러 : error)
    query : 분석을 위한 텍스트 값
    type : 분석 종류
    score: 결과에 대한 스코어 0.0~1.0(1.0에 가까울수록 신뢰도 높음)
    label: 감성 종류 : [부정, 중립, 긍정] , 감정 종류 : [기쁨, 신뢰, 공포, 기대, 놀라움, 슬픔, 혐오, 분노]
    error_code: 에러 코드 (에러시 표시)
    error_msg: 에러 사유 (에러시 표시)
'''

result1 = {
    "request_id": "0",
    "return_type": "omAnalysis",
    "result": 0,
    "reason": "",
    "return_object": {
        "query": "코로나 무증상 증상 넘 무서워요.",
        "type": "감성분석",
        "score": 0.9489038586616516,
        "label": "부정"
    },
    "result_code": "success"
}

result2 = {
    "request_id": "0",
    "return_type": "omAnalysis",
    "result": 0,
    "reason": "",
    "return_object": {
        "query": "코로나 무증상 증상 넘 무서워요.",
        "type": "감정분석",
        "Result": [
            [
            0.8162028789520264,
            "공포"
            ]
        ]
    },
    "result_code": "success"
} 

""" print(result1["return_object"])

for item in result1["return_object"] :
    print(result1["return_object"][item])

dt = result1["return_object"]
print(f'{dt["query"]} : {dt["type"]}-{dt["label"]}({dt["score"]*100:0.2f}%)')
print(type(dt["query"]))
print(type(dt["score"]))

lt=list()
print("lt", type(lt))

dt=dict()
print("dt", type(dt)) """

dt= result2["return_object"]
dt2= dt['Result'][0]
print(dt2[-1]) #뒤에서 첫번째 인덱스(마지막 인덱스) -1
print(f'{dt2[-1]} : {dt2[0]*100:0.2f}%')
