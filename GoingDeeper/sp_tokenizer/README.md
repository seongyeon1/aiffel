🔑 **PRT(Peer Review Template)**

- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
      ![image](https://github.com/seongyeon1/aiffel/assets/58682424/6da3b115-4c9f-4367-b1f9-64e0d52c9b8e)
      
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 퀘스트 문제 요구조건 등을 지칭
        - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부

         1. EDA ( 훈련 데이터 라벨링 값 비율 확인/ train, test data의 문장 길이 확인)
        ![image](https://github.com/seongyeon1/aiffel/assets/58682424/71c73b9b-828c-4284-911b-e0d6319f1c39)
        ![image](https://github.com/seongyeon1/aiffel/assets/58682424/5589a992-3e0e-4574-9dff-461d1cbce08b)

         2. 전처리( 반복되는 문자 처리 추가 /불용어 )
            ![image](https://github.com/seongyeon1/aiffel/assets/58682424/ce3bc99e-068b-4c50-9d26-7294b8c9a99c)
            ![image](https://github.com/seongyeon1/aiffel/assets/58682424/5f7169f3-2ce9-4842-9d1c-8be4617c3c18)

         4. 모델 학습 ( SentencePiece를 적용시킨 모델 학습하기)
           ![image](https://github.com/seongyeon1/aiffel/assets/58682424/997f1753-0800-4e9a-ba11-ccb1be617bd3)
           ![image](https://github.com/seongyeon1/aiffel/assets/58682424/6f63e92f-827c-413b-bf30-813731b6fd78)


- [O]  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
    - [O]  모델 선정 이유
    - - ![image](https://github.com/seongyeon1/aiffel/assets/58682424/5968f546-3586-485b-9c6a-4ec5bb3ff791)
    - [O]  Metrics 선정 이유 
    - [O]  Loss 선정 이유


    - ![image](https://github.com/seongyeon1/aiffel/assets/58682424/7810ea04-d77e-499f-a226-fc889769ea5a)

- [O]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
    - [O]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
    - ![image](https://github.com/seongyeon1/aiffel/assets/58682424/e4444b52-d69a-41f9-92f0-588fcb5ea3f2)

    - [O]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
    - [O]  각 실험을 시각화하여 비교하였나요?
    - ![image](https://github.com/seongyeon1/aiffel/assets/58682424/e79433b0-20d4-4d47-8bb6-1c4c95543c82)

    - [O]  모든 실험 결과가 기록되었나요?
      ![image](https://github.com/seongyeon1/aiffel/assets/58682424/09b26e09-2571-4f0a-8702-5b2aaaaf60f2)
      ![image](https://github.com/seongyeon1/aiffel/assets/58682424/d8ea64f6-d433-4a48-a832-158167024ac1)
      ![image](https://github.com/seongyeon1/aiffel/assets/58682424/a941f3f5-436f-4f69-9cd5-d8d07f484c6c)


- [[O]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
    - [O]  배운 점
    - [O]  아쉬운 점
    - [O]  느낀 점
    - [O]  어려웠던 점
 
    - ![image](https://github.com/seongyeon1/aiffel/assets/58682424/b43362c3-de7a-4c9a-9404-b65a09b3c2b2)



## 리뷰
 토크나이저 별로 형태소 분석기별 성능을 확인하는 내용이 좋았습니다. ROC 커브도 그리시고 완벽하네요!!!!!!!!!
