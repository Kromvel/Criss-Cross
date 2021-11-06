
"""
Добрый день!
Это игра обратные крестики-нолики.
Проигрывает тот, кто первым составит ряд из 5 своих знаков

"""

from tkinter import *
from tkinter import messagebox
import random
import re
import numpy as np
import tkinter.font as font
# это переменная нужна для отсчета ходов
count = 0
# здесь получаем массив из поля для игры (100 элементов)
array_board = np.arange(1,101).reshape(10, 10)
# функция для проверки есть ли победитель. Запускается каждый ход
def checkifwon(): 
    global winner_1, winner_2
    winner_1 = False
    winner_2 = False
    cells_for_cross_choose_list, cells_for_zero_choose_list
    def find_horizontal_row_of_5(lst_var):
        numbers_list = []
        for i in lst_var:
            s = re.findall(r'\d+', i)
            numbers_list.append(int(s[0]))
        sorted_numbers_lst = sorted(numbers_list)
        for m in range(len(array_board)):
            row_list = array_board[[m],:]
            lst_result = []
            lst_result_set = set()
            for i in row_list:
                for n in i:
                    for k in sorted_numbers_lst:
                        if n == k:
                            lst_result.append(k)
            for n in range(len(lst_result)-1):
                if  lst_result[n] + 1 == lst_result[n+1]:
                    lst_result_set.add(lst_result[n])
                    lst_result_set.add(lst_result[n+1])
            if len(lst_result_set) >= 5:
                final_list = sorted(lst_result_set)
                if final_list[-5] + 4 == final_list[-4] + 3 == final_list[-3] + 2 == final_list[-2] + 1 == final_list[-1]:
                        winner = True
                        change_color_of_defeat_row(final_list[-5:])
                        return winner
                elif final_list[0] + 4 == final_list[1] + 3 == final_list[2] + 2 == final_list[3] + 1  == final_list[4]:
                        winner = True
                        change_color_of_defeat_row(final_list[:5])
                        return winner
    def find_vertical_column_of_5(lst_var):
        numbers_list = []
        for i in lst_var:
            s = re.findall(r'\d+', i)
            numbers_list.append(int(s[0]))
        sorted_numbers_lst = sorted(numbers_list)
        for m in range(len(array_board)):
            column_list = array_board[:, [m]]
            lst_result = []
            lst_result_set = set()
            for i in column_list:
                for n in i:
                    for k in sorted_numbers_lst:
                        if n == k:
                            lst_result.append(k)
            for n in range(len(lst_result)-1):
                if  (lst_result[n] + 10 == lst_result[n+1]):
                    lst_result_set.add(lst_result[n])
                    lst_result_set.add(lst_result[n+1])
            if len(lst_result_set) >= 5:
                final_list = sorted(lst_result_set)
                if final_list[-5] + 40 == final_list[-4] + 30 == final_list[-3] + 20 == final_list[-2] + 10 == final_list[-1]:
                        winner = True
                        change_color_of_defeat_row(final_list[-5:])
                        return winner
                        break;
                elif final_list[0] + 40 == final_list[1] + 30 == final_list[2] + 20 == final_list[3] + 10  == final_list[4]:
                        winner = True
                        change_color_of_defeat_row(final_list[:5])
                        return winner
                        break;   
    def find_diagonal_up_row_of_5(lst_var):
        numbers_list = []
        for i in lst_var:
            s = re.findall(r'\d+', i)
            numbers_list.append(int(s[0]))
        sorted_numbers_lst = sorted(numbers_list)
        for m in range(len(array_board)):
            diagonal_list_up = np.diag(array_board, k=m)
            lst_result = []
            lst_result_set = set()
            for i in diagonal_list_up:
                for k in sorted_numbers_lst:
                    if i == k:
                        lst_result.append(k)
            for n in range(len(lst_result)-1):
                if  lst_result[n] + 11 == lst_result[n+1]:
                    lst_result_set.add(lst_result[n])
                    lst_result_set.add(lst_result[n+1])
            if len(lst_result_set) >= 5:
                final_list = sorted(lst_result_set)
                if final_list[-5] + 44 == final_list[-4] + 33 == final_list[-3] + 22 == final_list[-2] + 11 == final_list[-1]:
                        winner = True
                        change_color_of_defeat_row(final_list[-5:])
                        return winner
                elif final_list[0] + 44 == final_list[1] + 33 == final_list[2] + 22 == final_list[3] + 11  == final_list[4]:
                        winner = True
                        change_color_of_defeat_row(final_list[:5])
                        return winner
    def find_diagonal_down_row_of_5(lst_var):
        numbers_list = []
        for i in lst_var:
            s = re.findall(r'\d+', i)
            numbers_list.append(int(s[0]))
        sorted_numbers_lst = sorted(numbers_list)
        for m in range(len(array_board)):
            diagonal_list_down = np.diag(array_board, k=-m)
            lst_result = []
            lst_result_set = set()
            for i in diagonal_list_down:
                for k in sorted_numbers_lst:
                    if i == k:
                        lst_result.append(k)
            for n in range(len(lst_result)-1):
                if  lst_result[n] + 11 == lst_result[n+1]:
                    lst_result_set.add(lst_result[n])
                    lst_result_set.add(lst_result[n+1])
            if len(lst_result_set) >= 5:
                final_list = sorted(lst_result_set)
                if final_list[-5] + 44 == final_list[-4] + 33 == final_list[-3] + 22 == final_list[-2] + 11 == final_list[-1]:
                        winner = True
                        change_color_of_defeat_row(final_list[-5:])
                        return winner
                elif final_list[0] + 44 == final_list[1] + 33 == final_list[2] + 22 == final_list[3] + 11  == final_list[4]:
                        winner = True
                        change_color_of_defeat_row(final_list[:5])
                        return winner
    def find_reverse_diagonal_up_of_5(lst_var):
        numbers_list = []
        for i in lst_var:
            s = re.findall(r'\d+', i)
            numbers_list.append(int(s[0]))
        sorted_numbers_lst = sorted(numbers_list)
        for m in range(len(array_board)):
            reverse_diagonal_list_up = np.fliplr(array_board).diagonal(m)
            lst_result = []
            lst_result_set = set()
            for i in reverse_diagonal_list_up:
                for k in sorted_numbers_lst:
                    if i == k:
                        lst_result.append(k)
            for n in range(len(lst_result)-1):
                if  lst_result[n] + 9 == lst_result[n+1]:
                    lst_result_set.add(lst_result[n])
                    lst_result_set.add(lst_result[n+1])
            if len(lst_result_set) >= 5:
                final_list = sorted(lst_result_set)
                if final_list[-5] + 36 == final_list[-4] + 27 == final_list[-3] + 18 == final_list[-2] + 9 == final_list[-1]:
                        winner = True
                        change_color_of_defeat_row(final_list[-5:])
                        return winner
                elif final_list[0] + 36 == final_list[1] + 27 == final_list[2] + 18 == final_list[3] + 9  == final_list[4]:
                        winner = True
                        change_color_of_defeat_row(final_list[:5])
                        return winner
    def find_reverse_diagonal_down_of_5(lst_var):
        numbers_list = []
        for i in lst_var:
            s = re.findall(r'\d+', i)
            numbers_list.append(int(s[0]))
        sorted_numbers_lst = sorted(numbers_list)
        for m in range(len(array_board)):
            reverse_diagonal_list_down = np.fliplr(array_board).diagonal(-m)
            lst_result = []
            lst_result_set = set()
            for i in reverse_diagonal_list_down:
                for k in sorted_numbers_lst:
                    if i == k:
                        lst_result.append(k)
            for n in range(len(lst_result)-1):
                if  lst_result[n] + 9 == lst_result[n+1]:
                    lst_result_set.add(lst_result[n])
                    lst_result_set.add(lst_result[n+1])
            if len(lst_result_set) >= 5:
                final_list = sorted(lst_result_set)
                if final_list[-5] + 36 == final_list[-4] + 27 == final_list[-3] + 18 == final_list[-2] + 9 == final_list[-1]:
                        winner = True
                        change_color_of_defeat_row(final_list[-5:])
                        return winner
                elif final_list[0] + 36 == final_list[1] + 27 == final_list[2] + 18 == final_list[3] + 9  == final_list[4]:
                        winner = True
                        change_color_of_defeat_row(final_list[:5])
                        return winner
    if len(cells_for_zero_choose_list) > 0:
        if find_horizontal_row_of_5(cells_for_zero_choose_list) == True or find_vertical_column_of_5(cells_for_zero_choose_list) == True or find_diagonal_up_row_of_5(cells_for_zero_choose_list) == True or find_diagonal_down_row_of_5(cells_for_zero_choose_list) == True or find_reverse_diagonal_up_of_5(cells_for_zero_choose_list) == True or find_reverse_diagonal_down_of_5(cells_for_zero_choose_list) == True:
            winner_1 = True
    if len(cells_for_cross_choose_list) > 0: 
        if find_horizontal_row_of_5(cells_for_cross_choose_list) == True or find_vertical_column_of_5(cells_for_cross_choose_list) == True or find_diagonal_up_row_of_5(cells_for_cross_choose_list) == True or find_diagonal_down_row_of_5(cells_for_cross_choose_list) == True or find_reverse_diagonal_up_of_5(cells_for_cross_choose_list) == True or find_reverse_diagonal_down_of_5(cells_for_cross_choose_list) == True:
            winner_2 = True
    if winner_1 == True:
        disable_all_buttons()
        greetings_for_winner()
    elif winner_2 == True:
        disable_all_buttons()
        greetings_for_winner()
        return True
# Одна из функции для хода компьютера. Нужна, чтобы составить списки с номерами клеток поля с разделением на пустые, заполненные крестиками и ноликами
def lists_for_computer_move():
        global sorted_list_for_choose, numbers_empty_list     
        numbers_empty_list = []
        for i in empty_cells_list:
            s = re.findall(r'\d+', i)
            numbers_empty_list.append(int(s[0]))       
        numbers_zero_list = []
        for i in cells_for_zero_choose_list:
            s = re.findall(r'\d+', i)
            numbers_zero_list.append(int(s[0]))    
        numbers_cross_list = []
        for i in cells_for_cross_choose_list:
            s = re.findall(r'\d+', i)
            numbers_cross_list.append(int(s[0]))
        if computer_side == "X":
            sorted_list_for_choose = sorted(numbers_cross_list)
        elif computer_side == "O":
            sorted_list_for_choose = sorted(numbers_zero_list)
# Одна из функции для хода компьютера. В ней происходит выбор хода, основанный на избегании опасных ходов, позволяющих составить ряд из 5 знаков.
def arr_for_choice():
        global number_of_tries, choose_number
        lst_result = []
        for m in range(len(array_board)):
            row_array = array_board[[m],:]
            column__array = array_board[:, [m]]
            diagonal_up_array = np.diag(array_board, k=m)
            diagonal_down_array = np.diag(array_board, k=-m)
            reverse_diagonal_up_array = np.fliplr(array_board).diagonal(m)
            reverse_diagonal_down_array = np.fliplr(array_board).diagonal(-m)
            lst_before_result = []
            def find_not_enemy_numbers_of_cells(numbers_arr):
                list_var = []
                for i in numbers_arr:
                    for n in i:
                        for k in sorted_list_for_choose:
                            if n == k:
                                list_var.append(k)
                return lst_before_result.append(list_var)
            def find_not_enemy_numbers_of_cells_for_diagonals(numbers_arr):
                list_var = []
                for i in numbers_arr:
                            for k in sorted_list_for_choose:
                                if i == k:
                                    list_var.append(k)
                return lst_before_result.append(list_var)
            find_not_enemy_numbers_of_cells(row_array)          
            find_not_enemy_numbers_of_cells(column__array)
            find_not_enemy_numbers_of_cells_for_diagonals(diagonal_up_array)
            find_not_enemy_numbers_of_cells_for_diagonals(diagonal_down_array)
            find_not_enemy_numbers_of_cells_for_diagonals(reverse_diagonal_up_array)
            find_not_enemy_numbers_of_cells_for_diagonals(reverse_diagonal_down_array)         
            for i in lst_before_result:
                lst_result.append(i)             
        chosen_cell = ""
        choose_number = random.choice(numbers_empty_list)
        sorted_for_len_lst_result = sorted(lst_result, key=len,reverse=True)
        number_of_tries = 0
        list_for_check = []
        def check_for_danger_streak():
            for i in range(len(sorted_for_len_lst_result)):
                if len(sorted_for_len_lst_result[i]) >= 4:
                    list_for_check.append(sorted_for_len_lst_result[i])
        check_for_danger_streak()
        def check_for_lose_streak():
            danger_streak_response = 0    
            if len(list_for_check) > 0:
                for k in range(len(list_for_check)):
                    check_lst = list_for_check[k]
                    check_lst.append(choose_number)
                    try:
                        sorted_check_lst = sorted(check_lst)
                        if len(sorted_check_lst) >= 5:
                            check_row_array_for_danger_streak = []
                            check_column_array_for_danger_streak = []
                            check_diagonal_array_for_danger_streak = []
                            check_reversed_diagonal_array_for_danger_streak = []
                            for i in range(len(sorted_check_lst)):
                                if i + 4 < len(sorted_check_lst):
                                    if (sorted_check_lst[i] + 4 == sorted_check_lst[i+1] + 3 == sorted_check_lst[i+2] + 2 == sorted_check_lst[i+3] + 1  == sorted_check_lst[i+4]) or (sorted_check_lst[-5] + 4 == sorted_check_lst[-4] + 3 == sorted_check_lst[-3] + 2 == sorted_check_lst[-2] + 1  == sorted_check_lst[-1]):
                                        check_row_array_for_danger_streak.append(sorted_check_lst[i])
                                        check_row_array_for_danger_streak.append(sorted_check_lst[i+1])
                                        check_row_array_for_danger_streak.append(sorted_check_lst[i+2])
                                        check_row_array_for_danger_streak.append(sorted_check_lst[i+3])
                                        check_row_array_for_danger_streak.append(sorted_check_lst[i+4])                                 
                                        for m in range(len(array_board)):
                                            row_list = array_board[[m],:]
                                            lst_result_array_row = []
                                            for j in row_list:
                                                for n in j:
                                                    for s in check_row_array_for_danger_streak:
                                                        if n == s:
                                                            lst_result_array_row.append(s)
                                            if (check_row_array_for_danger_streak == lst_result_array_row) and (len(check_row_array_for_danger_streak) >= 5 and len(lst_result_array_row) >= 5 ):
                                                list_for_check[k].pop(-1)
                                                danger_streak_response += 1                                   
                                    elif (sorted_check_lst[i] + 40 == sorted_check_lst[i+1] + 30 == sorted_check_lst[i+2] + 20 == sorted_check_lst[i+3] + 10  == sorted_check_lst[i+4]) or (sorted_check_lst[-5] + 40 == sorted_check_lst[-4] + 30 == sorted_check_lst[-3] + 20 == sorted_check_lst[-2] + 10  == sorted_check_lst[-1]):
                                        check_column_array_for_danger_streak.append(sorted_check_lst[i])
                                        check_column_array_for_danger_streak.append(sorted_check_lst[i+1])
                                        check_column_array_for_danger_streak.append(sorted_check_lst[i+2])
                                        check_column_array_for_danger_streak.append(sorted_check_lst[i+3])
                                        check_column_array_for_danger_streak.append(sorted_check_lst[i+4])                           
                                        for m in range(len(array_board)):
                                            column_list = array_board[:, [m]]
                                            lst_result_array_column = []
                                            for j in column_list:
                                                for n in j:
                                                    for s in check_column_array_for_danger_streak:
                                                        if n == s:
                                                            lst_result_array_column.append(s)
                                            if (check_column_array_for_danger_streak == lst_result_array_column) and (len(check_column_array_for_danger_streak) >= 5 and len(lst_result_array_column) >= 5 ):
                                                list_for_check[k].pop(-1)
                                                danger_streak_response += 1                              
                                    elif (sorted_check_lst[i] + 44 == sorted_check_lst[i+1] + 33 == sorted_check_lst[i+2] + 22 == sorted_check_lst[i+3] + 11  == sorted_check_lst[i+4]) or (sorted_check_lst[-5] + 44 == sorted_check_lst[-4] + 33 == sorted_check_lst[-3] + 22 == sorted_check_lst[-2] + 11  == sorted_check_lst[-1]):
                                        check_diagonal_array_for_danger_streak.append(sorted_check_lst[i])
                                        check_diagonal_array_for_danger_streak.append(sorted_check_lst[i+1])
                                        check_diagonal_array_for_danger_streak.append(sorted_check_lst[i+2])
                                        check_diagonal_array_for_danger_streak.append(sorted_check_lst[i+3])
                                        check_diagonal_array_for_danger_streak.append(sorted_check_lst[i+4])
                                        for m in range(len(array_board)):
                                            diagonal_list_up = np.diag(array_board, k=m)
                                            lst_result_array_diagonal_list_up = []
                                            for i in diagonal_list_up:
                                                for s in check_diagonal_array_for_danger_streak:
                                                    if i == s:
                                                        lst_result_array_diagonal_list_up.append(s)
                                            if (check_diagonal_array_for_danger_streak == lst_result_array_diagonal_list_up) and (len(check_diagonal_array_for_danger_streak) >= 5 and len(lst_result_array_diagonal_list_up) >= 5 ):
                                                list_for_check[k].pop(-1)
                                                danger_streak_response += 1
                                        for m in range(len(array_board)):
                                            diagonal_list_down = np.diag(array_board, k=-m)
                                            lst_result_array_diagonal_list_down = []
                                            for i in diagonal_list_down:
                                                for s in check_diagonal_array_for_danger_streak:
                                                    if i == s:
                                                        lst_result_array_diagonal_list_down.append(s)
                                            if (check_diagonal_array_for_danger_streak == lst_result_array_diagonal_list_down) and (len(check_diagonal_array_for_danger_streak) >= 5 and len(lst_result_array_diagonal_list_down) >= 5 ):
                                                danger_streak_response += 1                            
                                    elif (sorted_check_lst[i] + 36 == sorted_check_lst[i+1] + 27 == sorted_check_lst[i+2] + 18 == sorted_check_lst[i+3] + 9  == sorted_check_lst[i+4]) or (sorted_check_lst[-5] + 36 == sorted_check_lst[-4] + 27 == sorted_check_lst[-3] + 18 == sorted_check_lst[-2] + 9  == sorted_check_lst[-1]):
                                        check_reversed_diagonal_array_for_danger_streak.append(sorted_check_lst[i])
                                        check_reversed_diagonal_array_for_danger_streak.append(sorted_check_lst[i+1])
                                        check_reversed_diagonal_array_for_danger_streak.append(sorted_check_lst[i+2])
                                        check_reversed_diagonal_array_for_danger_streak.append(sorted_check_lst[i+3])
                                        check_reversed_diagonal_array_for_danger_streak.append(sorted_check_lst[i+4])
                                        for m in range(len(array_board)):
                                            reverse_diagonal_list_up = np.fliplr(array_board).diagonal(m)
                                            lst_result_array_reverse_diagonal_list_up = []
                                            for i in reverse_diagonal_list_up:
                                                for s in check_reversed_diagonal_array_for_danger_streak:
                                                    if i == s:
                                                        lst_result_array_reverse_diagonal_list_up.append(s)
                                            if (check_reversed_diagonal_array_for_danger_streak == lst_result_array_reverse_diagonal_list_up) and (len(check_reversed_diagonal_array_for_danger_streak) >= 5 and len(lst_result_array_reverse_diagonal_list_up) >= 5 ):
                                                list_for_check[k].pop(-1)
                                                danger_streak_response += 1                                
                                        for m in range(len(array_board)):
                                            reverse_diagonal_list_down = np.fliplr(array_board).diagonal(-m)
                                            lst_result_array_array_for_danger_streak_down = []
                                            for i in reverse_diagonal_list_down:
                                                for s in check_reversed_diagonal_array_for_danger_streak:
                                                    if i == s:
                                                        lst_result_array_array_for_danger_streak_down.append(s)
                                            if (check_reversed_diagonal_array_for_danger_streak == lst_result_array_array_for_danger_streak_down) and (len(check_reversed_diagonal_array_for_danger_streak) >= 5 and len(lst_result_array_array_for_danger_streak_down) >= 5 ):
                                                danger_streak_response += 1                                    
                            if len(check_row_array_for_danger_streak) >= 5 or len(check_column_array_for_danger_streak) >= 5 or len(check_diagonal_array_for_danger_streak) >= 5 or len(check_reversed_diagonal_array_for_danger_streak) >= 5:
                                    danger_streak_response += 1                 
                            else:
                                list_for_check[k].pop(-1)
                              
                    except TypeError as e:
                        print(e)
            return danger_streak_response
        used_numbers = (set([]))
        
        check_for_lose_streak()
        def check_response():
            global number_of_tries, choose_number
            while True:
                lose_streaks_count = check_for_lose_streak()
                if lose_streaks_count > 0 and number_of_tries < 10:
                    used_numbers.add(choose_number)
                    set_numbers_empty_list = set(numbers_empty_list)
                    set_numbers_empty_list.difference_update(used_numbers)
                    numbers_empty_list_without_used_numbers = list(set_numbers_empty_list)
                    if len(numbers_empty_list_without_used_numbers) > 0 and len(set_numbers_empty_list) > 0:
                        choose_number = random.choice(numbers_empty_list_without_used_numbers)
                        check_for_lose_streak()
                    elif len(numbers_empty_list_without_used_numbers) == 0 and len(set_numbers_empty_list) > 0:
                        choose_number = random.choice(numbers_empty_list)
                    if choose_number not in used_numbers:
                        number_of_tries += 1   
                        check_for_lose_streak()
                        check_response()
                        
                    elif choose_number in used_numbers:
                        used_numbers.add(choose_number)
                        choose_number = random.choice(numbers_empty_list)
                        number_of_tries += 1
                        check_for_lose_streak()
                        check_response()
                        
                elif lose_streaks_count == 0 and number_of_tries < 10:
                    number_of_tries = 0
                    check_for_lose_streak()
                    for i in empty_cells_list:
                        str_choose_number = "cell_" +str(choose_number)
                        if re.findall(str_choose_number +'$', i):
                            chosen_cell = i
                            return chosen_cell
                    break;
                elif  number_of_tries == 10:
                    for i in empty_cells_list:
                        str_choose_number = "cell_" +str(choose_number)
                        if re.findall(str_choose_number +'$', i):
                            chosen_cell = i
                            return chosen_cell
                    break;
                else:
                    pass
                    break;
        return check_response()
# Функция, отключающая все кнопки на главном экране. Нужна для модульных окон с сообщениями.
def disable_all_buttons():
    for i in buttons:
        i.config(state=DISABLED)
        if i['bg'] == "#ac1818":
            i['disabledforeground'] ="white"
    my_menu.entryconfig("Опции", state="disabled")
# Функция, включающая все кнопки на главном экране. Нужна для возврата в игру после нажатия кнопки в модульном окне
def enable_all_buttons():
    for i in buttons:
        i.config(state=NORMAL)
    my_menu.entryconfig("Опции", state=NORMAL)
# Функция, меняющая цвет фона и шрифта ячеек, в которых был найден ряд из 5 одинаковых знаков
def change_color_of_defeat_row(var):
    for i in var:
        lst_buttons_variables_names['cell_'+str(i)].config(bg="#ac1818", fg='white')
# Функция с поздравлениями о победе и предложением сыграть снова
def greetings_for_winner():
    if winner_1 == True:
        greetings_msg = '''В этой партии победил игрок X ! \n Сыграете еще раз?'''
    elif winner_2 == True:
        greetings_msg = '''В этой партии победил игрок O ! \n Сыграете еще раз?'''
    greetings_window = Toplevel()
    greetings_window.geometry('350x250')
    greetings_window.title('Обратные крестики-нолики')
    greetings_window.columnconfigure(0, weight=1)
    greetings_window.columnconfigure(1, weight=1)
    windowWidth = greetings_window.winfo_reqwidth()
    windowHeight = greetings_window.winfo_reqheight()
    positionRight = int(greetings_window.winfo_screenwidth()/1.61 - windowWidth/2)
    positionDown = int(greetings_window.winfo_screenheight()/2 - windowHeight/2)
    greetings_window.geometry("+{}+{}".format(positionRight, positionDown))
    buttonFont = font.Font(size=16)
    button_no = Button(greetings_window, text="Нет", bg ="red", fg="white", command=lambda:[greetings_window.destroy(), root.destroy()], width=10, height=1)
    button_yes = Button(greetings_window, text="Да", bg ="green", fg="white", command=lambda:[greetings_window.destroy(), reset()], width=10, height=1)
    button_no['font'] = button_yes['font'] = buttonFont
    message = Label(greetings_window, text = greetings_msg, font='size, 14')
    message.grid(row=1, column=0,columnspan=2)
    button_yes.grid(row=3, column=0, pady=20)
    button_no.grid(row=3, column=1, pady=20)
    my_menu.entryconfig("Опции", state="normal")
    greetings_window.lift()
    greetings_window.attributes('-topmost',1)
    greetings_window.focus()
    greetings_window.mainloop()
# Функция, обрабатывающая ход игрока, в которой также запускается проверка победы и ход компьютера
def b_click(b):
    global clicked, count, computer_side, cells_for_zero_choose_list, cells_for_cross_choose_list, empty_cells_list
    cells_for_zero_choose_list = []
    cells_for_cross_choose_list = []
    empty_cells_list = []
    if selected_player == 1:
        computer_side = "O"
    elif selected_player == 2:
        computer_side = "X"
    if b["text"] == " "  and selected_player == 1:
        b["text"] = "X"       
        count += 1 
        checkifwon()
        computer_move()
    elif b["text"] == " "  and selected_player == 2:
        b["text"] = "O"
        count += 1 
        checkifwon()
        computer_move()
    else:
        disable_all_buttons()
        messagebox.showerror("Обратные крестики-нолики", "Это поле уже было выбрано \n Выберите другую ячейку", parent = root)
        enable_all_buttons()
# Одна из функции для хода компьютера. Она запускает сам ход.
def computer_move():
    global clicked, count
    for key, value in lst_buttons_variables_names.items():
        if value['text'] == "O":
            cells_for_zero_choose_list.append(key)
        elif value['text'] == "X":
            cells_for_cross_choose_list.append(key)
        elif value['text'] != "X" or value['text'] != "O":
            empty_cells_list.append(key)
    if computer_side == "O":
        lists_for_computer_move()
        choose_cell = arr_for_choice()
        globals()[choose_cell]["text"] = "O"
        cells_for_zero_choose_list.append(choose_cell)
        checkifwon()
        count += 1 
    elif computer_side == "X":
        lists_for_computer_move()
        choose_cell = arr_for_choice()
        globals()[choose_cell]["text"] = "X"
        cells_for_cross_choose_list.append(choose_cell)
        checkifwon()
        
        count += 1
    else:
        pass
# Основное окно
def set_board():
    global root, computer_side, my_menu, options_menu, lst_buttons_variables_names, buttons
    root = Tk()
    root.title('Обратные крестики-нолики')
    root_width = 500
    root_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (root_width / 2)
    y = (screen_height / 2) - (root_height / 2)
    root.geometry(f'{root_width}x{root_height}+{int(x)}+{int(y)}')
    my_menu = Menu(root)
    root.config(menu=my_menu)
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Опции", menu=options_menu)
    options_menu.add_command(label="Перезапустить игру", command=reset)
    buttons = []
    lst_buttons_variables_names = {}
    computer_side = ["O", "X"]
    for i in range(1,101):
        name = "cell_%s" %i
        lst_buttons_variables_names[name] = Button(root, text=" ", font=("Helvetica",20),heigh=1,width=2,bg="#a5a8a6", command=lambda:b_click(lst_buttons_variables_names[name]))
    count_row = 0
    count_column = 0
    def change_command(var):
        var.config(command = lambda:b_click(var))
    for key, value in lst_buttons_variables_names.items():
        new_var_button = globals()[key] = value
        change_command(new_var_button)
        if count_column == 0:
           new_var_button.grid(row=count_row, column=count_column, padx=(38,0))
        else:
            new_var_button.grid(row=count_row, column=count_column)
        if count_column < 9:
            count_column += 1
        elif count_column == 9 and count_row < 11:
            count_column = 0
            count_row += 1
        elif count_row == 11:
            count_row = 0
        buttons.append(new_var_button)
    root.lift()
    root.attributes('-topmost',0)
    root.mainloop()
# Функция перезагрузки игры
def reset():
    root.withdraw()
    popup_window()
# Окно с выбором игрока стороны для игры.
def popup_window():
    Tk().withdraw()
    window = Toplevel()
    window.title('Choose player')
    window_width = 450
    window_height = 250
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    buttonFont = font.Font(size=16)
    window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
    newlabel = Label(window, text = "Выберите X или O:", font='size, 14')
    newlabel.grid(row=0, column=1,sticky=S, rowspan=3, pady=(40, 10))
    var = IntVar()
    var.set(0)
    global which_button_is_selected,  computer_side
    def choose():
        which_button_is_selected = var.get()
        if(which_button_is_selected == 1) or (which_button_is_selected == 2):
            button_close.config(state=NORMAL)       
        else:
            messagebox.showinfo("Criss Cross", "Сделайте выбор")
    def callback():
        global selected_player
        selected_player = var.get()
        return selected_player
    cross = Radiobutton(window,text="X", variable=var, value=1, command=choose, width=10, height=1)
    zero = Radiobutton(window,text="O", variable=var, value=2, command=choose, width=10, height=1)
    button_close = Button(window, text="Выбрать", command=lambda:[callback(), window.destroy(), set_board()], state=DISABLED, width=10, height=1)
    button_close['font'] = cross['font'] = zero ['font'] =buttonFont
    cross.grid(row=4, column=1)
    zero.grid(row=5, column=1)
    button_close.grid(row=6, column=1)
    window.mainloop()
popup_window()
