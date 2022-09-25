
file = open(r"q4_urls.txt",'rb')

data = file.readlines() 

a  = 0                                          # позиция в списке
lines = len(data)
max_replay = 0                                  # максимальное количество повторов

for i in data:
    replay = 0
    if data[a][0] !='повтор':                   # условия игнора повторений
        for b in range(a+1,lines):              # провека повторов в непроверенном списке
            if i == data[b]:                    # условие поиска повторов
                replay = replay + 1             # счетчик повторов
                data[b] = ['повтор', data[b]]    # отмечат повтор, для игнора               
        data[a] = [replay,data[a]]                  # вносит в список количество повторов у строки
        print(data[a][1],i)
    if replay > max_replay: max_replay = replay # поиск максимального значения повторов
    a = a + 1


file1 = open('строкожор.txt','a')       # создает фаил

number = 0
for i in range(max_replay ,-1 ,-1):         # цикл сортировки от Мах количества повторов к мин
    for j in range(0,lines):                
        if i == data[j][0]:                 # поиск в списке по кол-ву повторов
            file1.writelines(f"№{number} (повтов {data[j][0]}) {data[j][1].strip()}\n")
            number = number + 1
file1.close()

print('готово',data[0][1])








