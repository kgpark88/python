exam_score = {'Minho': 95, 'Seoyun': 85, 'Dongsu': 75}
exam_score['Minho']
exam_score['Seoyun']
exam_score['Dongsu'] = 90
exam_score['Dongsu']
exam_score
exam_score['Yunsu'] = 100
exam_score
del exam_score['Yunsu']
exam_score


fruits = {'apple': '사과', 'banana': '바나나', 'orange': '오렌지'}
fruits
len(fruits)
del fruits['apple']
fruits
'banana' in fruits
'apple' not in fruits
fruits['apple'] = '사과'
fruits.keys()
fruits.values()
fruits.items()
fruits.clear()


dict1 = {1: 'one', 2: 'two', 3: 'three'}
dict2 = {v: k for k, v in dict1.items()}

print(dict1)
print(dict2)




