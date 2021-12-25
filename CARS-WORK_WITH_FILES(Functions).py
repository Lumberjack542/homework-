import csv
import json


def cou(country):
    list_us = []
    lit_europe = []
    list_japan = []
    with open('cars.csv', 'r', encoding='utf-8') as f:
        f = csv.reader(f)

        for i in f:
            i = " ".join(i)
            i = i.split(';')
            if i[-1] == country:
                list_japan.append(i[0])

            elif i[-1] == country:
                list_us.append(i[0])

            elif i[-1] == country:
                lit_europe.append(i[0])
    return list_us, list_japan, lit_europe


country_to_enter = input('Enter country :Japan, US, Europe: ')


cou = cou(country_to_enter)


def save_file(save):
    if save == '.csv':
        file = open('cars-model.csv', 'w', encoding='utf-8')
        file.write(str(cou[1]))
    elif save == '.txt':
        file = open('cars-model.txt', 'w', encoding='utf-8')
        file.write(str(cou[1]))


save_format = input('Enter format: .txt; .csv: ')
save_file(save_format)


