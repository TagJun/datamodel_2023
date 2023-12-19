import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
# 데이터 설정
sizes = [
    [1056000, 0],
    [950400,105600],
    [739200,316800],
    [528000,528000],
    [316800,739200],
    [316800,739200],
]

labels = [
    ['광고','소셜네트워크'],
    ['광고','소셜네트워크'],
    ['광고','소셜네트워크'],
    ['광고','소셜네트워크'],
    ['광고','소셜네트워크'],
    ['광고','소셜네트워크'],
]

section_names = [
    '9월',
    '10월',
    '11월',
    '12월',
    '1월',
    '2월',
]

# 원형 그래프 그리기
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))  # 2x3 그리드

for i in range(2):
    for j in range(3):
        index = i * 3 + j
        if index < len(sizes):
            axes[i, j].pie(sizes[index], labels=labels[index], autopct='%1.1f%%', startangle=90)
            axes[i, j].set_title(f'원형 그래프 {index + 1}\n({section_names[index]})')

# 그래프 표시
plt.show()
