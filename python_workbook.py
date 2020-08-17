import math
import string
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import heapq
import os
import sys
from datetime import datetime, timedelta
from matplotlib.table import Table
from statistics import mean
from iteration_utilities import duplicates
import re
import pygame


def exercise4(length, width):
    return length * width / 43560


def exercise5(small_cont, big_cont):
    print("Your refund is %.2f" % (small_cont * 0.10 + big_cont * 0.25))


def exercise12(longitude_rad, latitude_rad):
    longitude = [math.radians(lo) for lo in longitude_rad]
    latitude = [math.radians(la) for la in latitude_rad]
    return 6371.01 * math.acos(math.sin(longitude[0]) * math.sin(latitude[0]) + math.cos(longitude[0]) *
                               math.cos(latitude[0]) * math.cos(longitude[1] - latitude[1]))


def exercise17(mass, temp_change):
    energy = mass * temp_change * 4.186
    cost = 2.777e-7 * energy * 8.9
    return cost


def exercise26():
    today = time.asctime()
    today_list = today.split()
    print('Today is %s %s-%s-%s and the current time is %s' % (
        today_list[0], today_list[2], today_list[1], today_list[-1], today_list[-2]))


def exercise31(number):
    num = str(number)
    add = 0
    for i in num:
        add += int(i)
    return add


def exercise36(letter):
    vowel = ['a', 'e', 'u', 'i', 'o']
    c = ['vowel', 'consonant']
    if letter in vowel:
        return 'Vowel'
    elif letter == 'y':
        return random.choice(c)
    else:
        return 'Consonant'


def exercise38(month):
    month_dict = {'jan': 31, 'feb': 28 if int(time.asctime().split()[-1]) % 4 else 29, 'mar': 31, 'apr': 30, 'may': 31,
                  'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30, 'oct': 31, 'nov': 30, 'dec': 31
                  }
    for key in month_dict:
        if key in month.lower():
            return month_dict[key]


def exercise41(note_name):
    note_dict = {'C4': 261.63,
                 'D4': 293.66,
                 'E4': 329.63,
                 'F4': 349.23,
                 'G4': 392.00,
                 'A4': 440.00,
                 'B4': 493.88}
    if note_name in note_dict:
        return note_dict[note_name]
    for key in note_dict.keys():
        if note_name[0] is key[0]:
            freq = note_dict[key]
            return freq / pow(2, (4 - int(note_name[1])))


def exercise42(freq):
    note_dict = {'C4': 261.63,
                 'D4': 293.66,
                 'E4': 329.63,
                 'F4': 349.23,
                 'G4': 392.00,
                 'A4': 440.00,
                 'B4': 493.88}
    for note_name, frequency in note_dict.items():
        if frequency == freq:
            return note_name


def exercise45(p1, p2):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ind = 0
    for i, letter in enumerate(letters):
        if p2 is letter:
            ind = i

    pygame.init()
    clock = pygame.time.Clock()
    # set color with rgb
    white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)
    # set display
    game_display = pygame.display.set_mode((800, 600))
    # caption
    pygame.display.set_caption("ChessBoard")
    # Size of squares
    size = 60
    # board length, must be even
    board_length = 8
    game_display.fill(white)
    # beginning of logic
    game_exit = False

    cnt = 0
    for i in range(1, board_length + 1):
        for z in range(1, board_length + 1):
            # check if current loop value is even
            if cnt % 2 == 0:
                this_rect = pygame.draw.rect(game_display, white, [size * z, size * i, size, size])
                if abs(8 - p1) + 1 == i and ind + 1 == z:
                    pygame.draw.circle(game_display, (255, 0, 0), this_rect.center, 20)
                    print(i, z)
            else:
                this_rect = pygame.draw.rect(game_display, black, [size * z, size * i, size, size])
                if abs(8 - p1) + 1 == i and ind + 1 == z:
                    pygame.draw.circle(game_display, (255, 0, 0), this_rect.center, 20)
                    print(i, z)
            cnt += 1
        # since there's even number of squares go back one value
        cnt -= 1
    # Add a nice boarder
    pygame.draw.rect(game_display, black, [size, size, board_length * size, board_length * size], 1)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


def exercise46(month, day):
    months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
              'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
    month = month.lower() if len(month) <= 3 else month.lower()[0:3]
    month_index = months[month]

    if month_index is 4 or month is 5 or (month_index is 3 and day >= 20) or (month_index is 6 and day < 21):
        return 'spring'
    elif month_index is 7 or month_index is 8 or (month_index is 6 and day >= 21) or (month_index is 9 and day < 22):
        return 'summer'
    elif month_index is 10 or month_index is 11 or (month_index is 9 and day >= 22) or (month_index is 12 and day < 21):
        return 'fall'
    elif month_index is 1 or month_index is 2 or (month_index is 12 and day >= 21) or (month_index is 3 and day < 20):
        return 'winter'
    return 'Invalid month and day!'


def exercise48():
    year = input('please enter your birth year and I will tell your Chinese zodiac: ')
    zodiac_dict = {0: 'Monkey', 1: 'Rooster', 2: 'Dog',
                   3: 'Pig', 4: 'Rat', 5: 'Ox',
                   6: 'Tiger', 7: 'Hare', 8: 'Dragon',
                   9: 'Snake', 10: 'Horse', 11: 'Sheep'}  # ne lazimsa onu value yap
    return zodiac_dict[int(year) % 12]


def exercise51(letter_grade):
    letter_grade_dict = {'a+': 4.0, 'a': 4.0, 'a-': 3.7,
                         'b+': 3.3, 'b': 3.0, 'b-': 2.7,
                         'c+': 2.3, 'c': 2.0, 'c-': 1.7,
                         'd': 1.0, 'f': 0}
    if letter_grade.lower() in letter_grade_dict:
        return letter_grade_dict.get(letter_grade.lower())
    return -1


def exercise54(wavelength):
    if 380 <= wavelength < 450:
        plt.plot(np.linspace(380.0, 450.0), 'violet')
        plt.show()
    elif 450 <= wavelength < 495:
        plt.plot(np.linspace(450.0, 495.0), 'blue')
        plt.show()
    elif 495 <= wavelength < 570:
        plt.plot(np.linspace(495.0, 570.0), 'green')
        plt.show()
    elif 570 <= wavelength < 590:
        plt.plot(np.linspace(570.0, 590.0), 'yellow')
        plt.show()
    elif 590 <= wavelength < 620:
        plt.plot(np.linspace(590.0, 620.0), 'orange')
        plt.show()
    elif 620 <= wavelength < 750:
        plt.plot(np.linspace(620.0, 750.0), 'red')
        plt.show()
    else:
        print('Unknown wavelength')


def exercise58(your_date):
    the_date = re.split('. |/ |-', your_date)
    today = datetime(int(the_date[0]), int(the_date[1]), int(the_date[2]))
    tomorrow = today + timedelta(1)
    return tomorrow


def exercise59(license_plate):
    if len(license_plate) == 6 and 'A' <= license_plate[0:3] <= 'Z' and license_plate[3:].isdigit():
        print('Older style licence plate')
    elif len(license_plate) == 7 and 'A' <= license_plate[4:7] <= 'Z' and license_plate[0:4].isdigit():
        print('New style licence plate')
    else:
        print('The plate is not valid')


def exercise60():
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    all = [0, 00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
           20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    num = random.choice(all)

    print('The spin resulted in %d ...' % num)
    print('Pay %d' % num)
    if num % 2 is 0 and num != (0 or 00):
        print('Pay Even')
    elif num % 2 is 1:
        print('Pay Odd')
    else:
        print('Pay %d' % num)
    if num in black:
        print('Pay Black')
    elif num in red:
        print('Pay Red')
    if 1 <= num <= 18:
        print('Pay 1 to 18')
    elif 18 < num <= 36:
        print('Pay 19 to 36')


def exercise66():
    your_input = input("Enter the letter grade, enter space to quit: ")
    sum_grades = 0
    count = 0
    while your_input != " ":
        if exercise51(your_input) == -1:
            print('Your input is not a valid letter grade, enter a valid letter grade')
            your_input = input("Enter the letter grade, enter space to quit: ")
        sum_grades += exercise51(your_input)
        your_input = input("Enter the letter grade, enter space to quit: ")
        count += 1
    print(sum_grades, count)
    return sum_grades / count


def exercise67():
    total_price = 0
    ages = [int(i) for i in input('Enter the ages of the guests: ').split()]
    for num in ages:
        if num <= 2:
            total_price += 0
        elif 3 <= num <= 12:
            total_price += 14
        elif num >= 65:
            total_price += 18
        else:
            total_price += 23

    print('Total admission price for the group of %d people is %.2f' % (len(ages), total_price))


def exercise68(your_string):
    if len(your_string) != 8:
        return
    for b in your_string:
        if b != 0 or b != 1:
            return
    if your_string.count('1') % 2 == 0:
        return '0'
    else:
        return '1'


def exercise69():
    # Nilakantha Series
    pi_list = []
    pi_list.append(3)
    k, p, s = 2, 3, 0
    for _ in range(15):
        s += 1
        if s % 2 == 1:
            p += 4.0 / (k * (k + 1) * (k + 2))
        else:
            p -= 4.0 / (k * (k + 1) * (k + 2))
        k += 2
        pi_list.append(p)
    return pi_list


def exercise70_encrypt(your_message):
    encrypted_message = ""
    for i in your_message.lower():
        if not i.isalpha():
            encrypted_message += i
        if chr(ord(i) + 3).isalpha():
            encrypted_message += chr(ord(i) + 3)
        elif i == 'z':
            encrypted_message += 'c'
        elif i == 'y':
            encrypted_message += 'b'
        elif i == 'x':
            encrypted_message += 'a'
    return encrypted_message


def exercise70_decrypt(your_message):
    encrypted_message = []
    for i in your_message.lower():
        if not i.isalpha():
            encrypted_message.append(i)
        if chr(ord(i) - 3).isalpha():
            encrypted_message.append(chr(ord(i) - 3))
        elif i == 'c':
            encrypted_message.append('z')
        elif i == 'b':
            encrypted_message.append('y')
        elif i == 'a':
            encrypted_message.append('x')
    str_message = ""
    return str_message.join(encrypted_message)


def exercise71(x):
    guess = x / 2
    while abs(guess * guess - x) >= 1e-12:
        guess = (guess + x / guess) / 2

    return guess


def exercise72(your_str):
    your_str = your_str.lower().replace(" ", "")
    for s in string.punctuation:
        if s in your_str:
            your_str = your_str.replace(s, "")
    print(your_str)
    is_palindrome = True
    for i in range(len(your_str) // 2):
        if your_str[i] != your_str[len(your_str) - i - 1]:
            is_palindrome = False

    return is_palindrome


def exercise74():
    fig, ax = plt.subplots()
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1])

    nrows, ncols = 10, 10
    width, height = 1.0 / ncols, 1.0 / nrows

    # Add cells
    for i in range(1, 11):
        for j in range(1, 11):
            val = i * j
            tb.add_cell(i, j, width, height, text=val, loc='center', facecolor='white')

    # Row and column labels ...
    for i in range(1, 11):
        tb.add_cell(i, -1, width, height, text=i, loc='right', edgecolor='none', facecolor='none')
        tb.add_cell(-1, i, width, height / 2, text=i, loc='center', edgecolor='none', facecolor='none')
    ax.add_table(tb)
    plt.show()


def exercise75(n, m):
    d = min(n, m)
    while n % d != 0 or m % d != 0:
        d -= 1
    return d


def exercise76(n):
    if n <= 2:
        return -1
    factor = 2
    prime_factors = []
    while factor <= n:
        if n % factor == 0:
            prime_factors.append(factor)
            n = n / factor
        else:
            factor += 1
    return prime_factors


def exercise77(b):
    add = 0
    p = 0
    for i in b[::-1]:
        add += int(i) * pow(2, p)
        p += 1
    return add


def exercise78(decimal):
    result = ""
    while decimal != 0:
        r = decimal % 2
        result = result + str(r)
        decimal = decimal // 2
    return result[::-1]


def exercise79():
    num = random.randint(1, 100)
    current_max = num
    current_max_count = 0
    for _ in range(100):
        num = random.randint(1, 100)
        print(num)
        if num > current_max:
            current_max = num
            current_max_count += 1
            print("%d => Update" % num)

    print("The maximum value found was %d " % current_max)
    print("The maximum value was updated %d times " % current_max_count)


def exercise87(your_str, width):
    return your_str.rjust((width - len(your_str)) // 2 + len(your_str))


def exercise89(your_str):
    your_str = your_str.replace(" i ", " I ")
    if len(your_str) > 0:
        your_str = your_str[0].upper() + your_str[1:len(your_str)]
    for s in range(len(your_str) - 1):
        if your_str[s] in string.punctuation:
            print(s, your_str[s])
            your_str = your_str[0:s + 2] + your_str[s + 2].upper() + your_str[s + 3:len(your_str)]
    return your_str


def exercise90(your_str):
    for i in your_str.replace(" ", ""):
        if not i.isdigit():
            return False
    return True


def exercise91(precedence_str):
    precedence_dict = {"+": 1, "-": 1, "*": 2,
                       "/": 2, "^": 3}
    result = []
    for i in precedence_str:
        if i in precedence_dict.keys():
            result.append(precedence_dict[i])

    if not result:
        return -1
    return ''.join(map(str, result))


def exercise92(num):
    for i in range(2, num):
        if num % i == 0:  # not prime
            return False
    return True


def exercise93(num):
    step = 0
    while True:
        step += 1
        if exercise92(num + step):
            break
    return num + step


def exercise94():
    password_len = random.randint(7, 10)
    return ''.join(map(str, list(map(chr, random.sample(range(33, 127), password_len)))))


def exercise95():
    version = ['old', 'new']
    letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    numbers = '1234567890'
    licence_plate = ""
    if random.choice(version) == 'old':
        licence_plate += "".join(random.choices(letters, k=3))
        licence_plate += "".join(random.choice(numbers) for _ in range(3))
    else:
        licence_plate += "".join(random.choice(numbers) for _ in range(4))
        licence_plate += "".join(random.choice(letters) for _ in range(3))
    return licence_plate


def exercise96(your_password):
    count_upper, count_lower, count_digit, count_punc = 0, 0, 0, 0
    if len(your_password) < 8:
        return False
    for i in your_password:
        if i.isdigit():
            count_digit += 1
        elif i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
        elif i in string.punctuation:
            count_punc += 1
        else:
            print('Invalid character, your password should include at '
                  'least one uppercase letter, one lowercase letter, one punctuation and one number')
            break
    if count_upper >= 1 and count_lower >= 1 and count_digit >= 1 and count_punc >= 1:
        return True
    return False


def exercise97():
    password = exercise94()
    num_of_attempts = 0
    while not exercise96(password):
        num_of_attempts += 1
        password = exercise94()

    return num_of_attempts, password


# Exercise 98
def hex2int(hexa):
    hex_dict = {'A': 10, 'B': 11, 'C': 12,
                'D': 13, 'E': 14, 'F': 15}
    add = 0
    p = 0
    for i in hexa[::-1]:
        if i.isdigit():
            add += int(i) * pow(16, p)
            p += 1
        else:
            add += hex_dict.get(i) * pow(16, p)
            p += 1
    return add


def int2hex(decimal):
    hex_dict = {10: 'A', 11: 'B', 12: 'C',
                13: 'D', 14: 'E', 15: 'F'}
    result = ""
    decimal = int(decimal)
    while decimal != 0:
        r = decimal % 16
        if r > 9:
            result = result + hex_dict.get(r)
            decimal = decimal // 16
        else:
            result = result + str(r)
            decimal = decimal // 16
    return result[::-1]


def exercise99(your_str, base):
    if base == 2:
        decimal = exercise77(your_str)
        return int2hex(decimal)
    elif base == 16:
        decimal = hex2int(your_str)
        return exercise78(decimal)
    else:
        print('base should be 2 or 16')


def exercise101(num1, num2):
    return num1 // exercise75(num1, num2), num2 // exercise75(num1, num2)


# exercise103
# 2 versions, you can enter a date in the form 10 June 1960 or the program shows all the magic dates
def exercise103_v1(your_date):
    date_list = your_date.split()

    months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
              'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
    month = date_list[1].lower() if len(date_list[1]) <= 3 else date_list.lower()[0:3]
    month_index = int(months[month])
    if month_index * int(date_list[0]) == date_list[2][2:]:
        print('The date you entered is a magic date')
    else:
        print("Your date is not a magic date")


def days(month, year):
    days_dict = {1: 31, 2: 28 if year % 4 else 29, 3: 31, 4: 30, 5: 31, 6: 30,
                 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return days_dict[month]


def exercise103_v2():
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    print("Here are the magic dates in 20th century")
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, days(month, year) + 1):
                if day * month == (year % 1900):
                    print(" %d %s %d is a magic year" % (day, months[month], year))


# --- chapter 5 - List exercises --------
def exercise104():
    print("Enter a number, enter 0 to stop ")
    num = input(" -- > ")
    num_list = []
    while int(num) != 0:
        num_list.append(int(num))
        num = input(" -- > ")
    print(num_list)
    return sorted(num_list, reverse=True)


def exercise106(your_list, n):
    print(your_list)
    large_removed = [x for x in your_list if x not in heapq.nlargest(n, your_list)]
    small_removed = [x for x in large_removed if x not in heapq.nsmallest(n, your_list)]
    return small_removed


def exercise107(your_list):
    return list(dict.fromkeys(your_list))


def exercise109(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return divisors


def exercise110(num):
    add = 0
    for i in exercise109(num):
        add += i
    if add == num:
        return True
    return False


def exercise111(your_str):
    str_list = your_str.split()
    for i in range(len(str_list)):
        if str_list[i][-1] in string.punctuation:
            str_list[i] = str_list[i][:-1]  # remove the last char
    return str_list


def exercise113(str_list):
    your_str = ""
    for i in range(len(str_list) - 1):
        your_str = your_str + str_list[i] + ', '
    your_str = your_str + 'and ' + str_list[-1]
    return your_str


def exercise114():
    return sorted(random.sample(range(1, 50), 6))


# including exercise 116
def exercise115(your_str):
    vowel = ['a', 'e', 'u', 'i', 'o']
    pig_latin = ""
    str_list = exercise111(your_str.lower())

    for j in range(len(str_list)):
        vowel_flag = 1  # make sure that it adds ay only once
        word = str_list[j]
        if word[0] in vowel:
            pig_latin += word + 'way '
            continue
        for i in range(len(word)):
            if word[i] in vowel and vowel_flag:
                pig_latin += word[i:] + word[:i] + 'ay '
                vowel_flag = 0
    pig_latin = pig_latin[:len(pig_latin) - 1]
    if your_str[-1][-1] in string.punctuation:
        pig_latin = pig_latin + your_str[-1][-1]  # add the punctuation to the end

    return pig_latin[0].upper() + pig_latin[1:]


def exercise117(coords_list):
    x_coords = []
    y_coords = []
    for x_y in coords_list:
        x_coords.append(x_y[0])
        y_coords.append(x_y[1])
    print(x_coords)
    print(y_coords)
    avg_x = mean(x_coords)
    avg_y = mean(y_coords)
    num = sum([a * b for a, b in zip(x_coords, y_coords)]) - ((sum(x_coords) * sum(y_coords)) / len(x_coords))
    denum = sum([a * b for a, b in zip(x_coords, x_coords)]) - (pow(sum(x_coords), 2) / len(x_coords))
    m = num / denum
    b = avg_y - m * avg_x
    plt.plot(x_coords, y_coords, 'violet')
    plt.legend('y')
    plt.show()
    print('y = %.2fx + %.2f' % (m, b))


# exercise118
def create_deck():
    deck = []
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for i in values:
        for j in suits:
            deck.append(i + j)
    return deck


def shuffle_deck():
    deck = create_deck()
    for i in range(len(deck)):
        k = random.randint(0, 51)
        temp = deck[k]
        deck[k] = deck[i]
        deck[i] = temp
    return deck


def deal(num_of_hands, num_of_cards, deck):
    lists = [[] for _ in range(num_of_hands)]  # create a list for each player
    deck_range = 51
    for _ in range(num_of_cards):
        for j in range(num_of_hands):
            card = random.randint(0, deck_range)
            lists[j].append(deck[card])
            deck.pop(card)
            deck_range -= 1
    return lists, deck


def exercise125(smaller, larger):
    if len(smaller) == 0 or smaller == larger:
        return True
    subset = []
    k = 0
    while k <= len(larger) - 1:
        for i in range(len(smaller)):
            if smaller[i] == larger[k]:
                subset.append(larger[k])
        k += 1
    if subset == smaller:
        return True
    return False


def exercise127(limit):
    p_list = [x for x in range(0, limit + 1)]
    p_list[1] = 0
    print(p_list)
    p = 2
    while p < limit:
        for i in range(p * 2, limit + 1, p):
            p_list[i] = 0
        p = p + 1
        while p < limit and p_list[p] == 0:
            p += 1
    result = [x for x in p_list if x != 0]
    return result


def exercise128(your_dict, value):
    keys = []
    for k, v in your_dict.items():
        if v == value:
            keys.append(k)
    return keys


def exercise129():
    dices = {2: 0, 3: 0, 4: 0, 5: 0,
             6: 0, 7: 0, 8: 0, 9: 0,
             10: 0, 11: 0, 12: 0}
    for _ in range(1000):
        side1 = random.randint(1, 6)
        side2 = random.randint(1, 6)
        dices[side1 + side2] += 1

    return dices


def exercise130(your_str):
    keypad = {1: ['.', ',', '?', '!', ':'], 2: ['A', 'B', 'C'],
              3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
              5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'],
              7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'],
              9: ['W', 'X', 'Y', 'Z']}
    your_str = your_str.upper()
    press = 0
    result = ""
    for _ in range(len(keypad)):
        for k, v in keypad.items():
            if press == len(your_str):
                break
            if your_str[press].isspace():
                result += '0'
                press += 1
            for i in range(len(v)):
                if press == len(your_str):
                    break
                if v[i] == your_str[press]:
                    result += (i + 1) * str(k)
                    press += 1
    return result


def exercise136(str1):
    str1 = str1.lower()
    str_list1 = exercise111(str1)
    str1 = "".join(str_list1)
    dictionary = {}
    for i in str1:
        dictionary[i] = 1
    return dictionary


def exercise137(word):
    word = word.upper()
    points = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
              2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'],
              4: ['F', 'H', 'V', 'W', 'Y'], 5: 'K',
              8: ['J', 'X'], 10: ['Q', 'Z']}
    score = 0
    for i in word:
        for k, v in points.items():
            for j in v:
                if i == j:
                    score += k
    return score


def exercise138(): 
    fig, ax = plt.subplots()
    ax.set_axis_off()
    tb = Table(ax, bbox=[0, 0, 1, 1])

    nrows, ncols = 5, 5
    width, height = 1.0 / ncols, 1.0 / nrows
    val_list = list(random.sample(range(1, 17), nrows))
    val_list += list(random.sample(range(16, 31), nrows))
    val_list += list(random.sample(range(31, 46), nrows))
    val_list += list(random.sample(range(46, 61), nrows))
    val_list += list(random.sample(range(61, 76), nrows))

    # val_list = []
    # c = 1
    # t = 1
    # for _ in range(5):
    #     for _ in range(1, 6):
    #         val_list.append(random.randint(t, c*15))
    #     c += 1
    #     t += 15
    # print(val_list, len(val_list))

    # Add cells
    ind = 0
    pick = random.choice(val_list)
    print(pick)
    for i in range(1, 6):
        for j in range(1, 6):
            val = val_list[ind]
            if pick == val:
                tb.add_cell(j, i, width, height, text=val, loc='center', facecolor='violet')
                ind += 1
            else:
                tb.add_cell(j, i, width, height, text=val, loc='center', facecolor='white')
                ind += 1

    tb.add_cell(1, -1, width, height, text='B', loc='right', edgecolor='none', facecolor='none')
    tb.add_cell(2, -1, width, height, text='I', loc='right', edgecolor='none', facecolor='none')
    tb.add_cell(3, -1, width, height, text='N', loc='right', edgecolor='none', facecolor='none')
    tb.add_cell(4, -1, width, height, text='G', loc='right', edgecolor='none', facecolor='none')
    tb.add_cell(5, -1, width, height, text='O', loc='right', edgecolor='none', facecolor='none')
    tb.add_cell(-1, 1, width, height/2, text='B', loc='center', edgecolor='none', facecolor='none')
    tb.add_cell(-1, 2, width, height/2, text='I', loc='center', edgecolor='none', facecolor='none')
    tb.add_cell(-1, 3, width, height/2, text='N', loc='center', edgecolor='none', facecolor='none')
    tb.add_cell(-1, 4, width, height/2, text='G', loc='center', edgecolor='none', facecolor='none')
    tb.add_cell(-1, 5, width, height/2, text='O', loc='center', edgecolor='none', facecolor='none')

    ax.add_table(tb)
    plt.show()

# --------------CHAPTER 7--------------
# https://pages.cpsc.ucalgary.ca/~bdstephe/PythonWorkbook/ -- files
def exercise141(filename): 
    f = open(filename, 'r')
    for i in range(10):
        print(f.readline())
    f.close()

def exercise144(filename):
    i = 0
    with open(filename, 'r') as f:
        data = f.readlines()
    with open(filename, 'w') as f:
        for number, line in enumerate(data):
            f.write('%d  %s' % (number + 1, line))


def exercise145(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data += line.split()
    max_word = data[0]
    max_len = len(data[0])
    for word in data:
        if len(word) > max_len:
            max_len = len(word)
            max_word = word
    return max_len, max_word


def exercise146(filename):
    # letter_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
    #                'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
    #                'm': 0, 'n': 0, 'o': 0, 'p': 0, 'r': 0, 's': 0,
    #                't': 0, 'u': 0, 'v': 0, 'y': 0, 'z': 0, 'q': 0,
    #                'w': 0, 'x': 0}
    letter_dict = {}
    for ch in 'qwertyuiopasdfghjklzxcvbnm':
        letter_dict[ch] = 0

    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.lower()
            for letter in line:
                if letter in letter_dict.keys():
                    letter_dict[letter] += 1

    max_oocurred_letter = max(letter_dict.keys(), key=(lambda key: letter_dict[key]))

    return letter_dict, max_oocurred_letter


def exercise147(filename):
    data = ""
    counts = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            data += line

    data_list = exercise111(data)
    for word in data_list:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    max_occurred_word = max(counts.keys(), key=(lambda key: counts[key]))
    occurence = counts[max_occurred_word]
    return max_occurred_word, occurence


def exercise150(infile, outfile):
    input_file = open(infile, 'r')
    output_file = open(outfile, 'w')
    for line in input_file.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] != '#':
            output_file.write(line+"\n")
    input_file.close()
    output_file.close()

    
def exercise152(user_input):

    result = {}
    with open('elements.txt', 'r') as f:
        for line in f.readlines():
            proton, symbol, name = line.split(',')
            result[(proton, symbol)] = name

    for k, v in result.items():
        if user_input.isdigit():
            if k[0] == user_input:
                return v.strip(), k[1]
        if user_input.isalpha():
            if k[1] == user_input:
                return v.strip(), k[0]


def exercise153(filename):
    letters_count = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            for letter in line:
                if letter.isalpha():
                    letter = letter.lower()
                    if letter in letters_count:
                        letters_count[letter] = letters_count[letter] + 1
                    else:
                        letters_count[letter] = 1
    return letters_count


def exercise154():
    boys_name = set()
    girls_name = set()
    popular_boys = 0
    popular_girls = 0
    pop_name = ""
    os.chdir('BabyNames')
    for filename in os.listdir('.'):
        with open(filename, 'r') as f:
            for line in f.readlines():
                name, num = line.split()
                if filename[5:] == 'BoysNames.txt':
                    if int(num) > popular_boys:
                        popular_boys = int(num)
                        pop_name = name
                        boys_name.add(name)
                if filename[5:] == 'GirlsNames.txt':
                    if int(num) > popular_girls:
                        popular_girls = int(num)
                        pop_name = name
                        girls_name.add(name)
        popular_boys = 0
        popular_girls = 0
        print(filename, pop_name, end='\n')
    return boys_name, girls_name


def exercise156(y1, y2):
    boys_name = set()
    girls_name = set()
    popular_boys = 0
    popular_girls = 0
    pop_name = ""
    os.chdir('BabyNames')
    for filename in os.listdir('.'):
        if y1 <= int(filename[:4]) <= y2:
            with open(filename, 'r') as f:
                for line in f.readlines():
                    name, num = line.split()
                    if filename[5:] == 'BoysNames.txt':
                        if int(num) > popular_boys:
                            popular_boys = int(num)
                            pop_name = name
                            boys_name.add(name)
                    if filename[5:] == 'GirlsNames.txt':
                        if int(num) > popular_girls:
                            popular_girls = int(num)
                            pop_name = name
                            girls_name.add(name)
            popular_boys = 0
            popular_girls = 0
            print(filename, pop_name, end='\n')
    return boys_name, girls_name


def exercise159(filename):
    end_of_sentence = ".?!"
    line_counter = 0
    prev_line = ""
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line[-1] in end_of_sentence:
                prev_line = ""
                sentence = line.split()
                if list(duplicates(sentence)) == sentence:
                    continue
                else:
                    print('Duplicate word in line % d' % line_counter)
            else:
                prev_line += line
            line_counter += 1


def is_square(n):
    a = math.sqrt(n)
    print(a)
    b = math.floor(a) * math.floor(a)
    print(b)
    if b == n:
        return True
    return False
