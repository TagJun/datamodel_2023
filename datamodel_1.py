import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
# 데이터 설정
categories = ['9월', '10월', '11월','12월','1월','2월']
values = [5280000, 5501000, 5469000, 5480000, 5533000, 5554000]

# 막대 그래프 그리기
colors=['blue','red','blue','blue','red','red']
plt.bar(categories, values, color=colors)

# 그래프 제목 및 축 레이블 설정
plt.title('월별 총매출')
plt.xlabel('월')
plt.ylabel('총매출')

# 그래프 표시
plt.show()
