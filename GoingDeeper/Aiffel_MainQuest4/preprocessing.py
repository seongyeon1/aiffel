import re
import pandas as pd
import numpy as np
def preprocessing(train, col='document'):
    train[col] = train[col].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣0-9♥♡乃ㄳㅄ ]", "")  # 정규 표현식 수행
    train[col] = train[col].str.replace('^ +', "")  # 공백은 empty 값으로 변경
    train[col].replace('', np.nan, inplace=True)  # 공백은 Null 값으로 변경
    train.dropna(how='any', inplace=True)

    train[col] = train[col].apply(lambda x: re.sub(r'(ㅋ|ㅎ|ㅜ|ㅠ){2,}', lambda m: m.group(1) * 2, x))  # 반복되는 2자리 문자 처리

    train[col] = train[col].str.replace(r'♡', '♥')
    train[col] = train[col].apply(lambda x: re.sub(r'♥+', '♥', x))
    train[col] = train[col].apply(lambda x: re.sub(r'\b(\S+)( \1)+', r'\1', x))
    train[col] = train[col].apply(lambda x: ' '.join(x.split()))
    return train