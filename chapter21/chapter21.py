import pandas as pd

df = pd.DataFrame({

    "name": ["민수", "지영", "서준"],
    "score": [85, 92, 78],

})

a = df["score"]

b = df[["name", "score"]]

print(type(a))
print(a)

print(type(b))
print(b)

# Series는 컬럼이 1개 (컬럼 2개가 될 수 없음)
# DataFrame은 컬럼이 여러개가 될 수 있음




# data/chapter21/store_sales.csv
# https://github.com/GilbertMoon/ai-python-basics-reader-resources/blob/main/data/chapter21/store_sales.csv

import pandas as pd
df_sales = pd.read_csv("data/chapter21/store_sales.csv")
print(df_sales)
# df 같은걸로만 쓰면 위에 내용 덮어씌워져서 날라갈 수 있으니 이름 바꿔주기.

# info() / head() / tail() / describe()