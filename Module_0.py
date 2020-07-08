#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
def binary_search(number):
    '''Между альтернативой усложнить цикл вложенными ветками, 
    которые делили бы массив на части и проверяли отдельно каждую, 
    выбрала все-таки бинарный поиск, ибо со сложным циклом код слишком длинный. 
    '''
    count = 0
    minimum = 0      # Мин. граница поиска
    maximum = 100  # Макс.  граница поиска
    while (maximum - minimum) > 1:  # Пока максималная граница больше минимальной и их разница больше 1
        middle = int((minimum + maximum) / 2) # вычисляем среднее между макисмальной и минимальной границами
        if (middle >= number): # Если угадываемое число равняется среднему или находится между средним и максимальной границей
            maximum = middle  # В таком случае целесообразно, чтобы максимум принял значение среднего как верхней границы
        else:
            minimum = middle  # В таком случае целесообразно, чтобы минимум принял значение среднего как верхней границы
        count += 1
    return(count)  # выход из цикла, если цисло угадано
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать,
        как быстро игра угадывает число'''
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(binary_search)


# In[ ]:




