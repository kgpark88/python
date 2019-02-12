names = ['Minho', 'Seoyun', 'Dongsu']
scores = [95, 85, 75]
for i in range(len(names)):
    name = names[i]
    score = scores[i]
    if score >= 90:
        level = 'A학점'
    elif 80 <= score < 90:
        level = 'B학점'
    else:
        level = 'C학점'
    print(name, score, level)
