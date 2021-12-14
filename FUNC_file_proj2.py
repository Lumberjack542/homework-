import random
import pickle
import json
import ast
import pandas as pd
import csv

list_words = 'кот ушел давно тирания беспомощная клоун однажды завал противотанк немец дурак африка дзен новый'.split()
genre_list = ['horror', 'fantastic', 'fantasy', 'science', 'drama', 'comedy']
countries_list = ['Usa', 'Russia', 'France', 'Italy', 'Poland', 'Ukraine', 'Germany', 'Swiss', 'Canada', 'Denmark']

save = input('Enter format you want to save:')


def save_file(name_file, mode):
    f = open(name_file, mode, encoding='utf-8')
    for i in range(10):
        film = {'id': i,
                'name': ' '.join(random.sample(list_words, 2)).upper(),
                'mark': random.randint(0, 100),
                'year': random.randint(1895, 2021),
                'genre': set(random.sample(genre_list, 3)),
                'countries': tuple(random.sample(countries_list, 2))}
        f.write(str(film) + '\n')


def save_file_json(name_file, mode):
    import json
    list_with_dictionary_for_json = []
    for i in range(10):
        film = {"id": i,
                "name": ' '.join(random.sample(list_words, 2)).upper(),
                "mark": random.randint(0, 100),
                "year": random.randint(1895, 2021),
                "genre": random.sample(genre_list, 3),
                "countries": tuple(random.sample(countries_list, 2))}
        list_with_dictionary_for_json.append(film)
   # print(list_with_dictionary_for_json)
    with open(name_file, mode, encoding='utf-8') as f_json:
        json.dump(list_with_dictionary_for_json, f_json, indent=3)


if save == 'txt':
    save_for = 'movies.txt'
    save_file(save_for, "w")
    file = open('qwe.txt', 'w', encoding='utf-8')
    file1 = open('movies.txt', 'r', encoding='utf-8')

    list_dict = []

    for dict_f in file1:
        dict_f = ast.literal_eval(dict_f)
        list_dict.append(dict_f)

    for i in list_dict:
        print(i)

    enter = input('Enter year, mark, countries or genre for find film: ')
    for i in list_dict:
        if enter == str(i['mark']) or enter == str(i['year']):
            print(i['name'])
            file.write(str(i['name'] + '\n'))

        elif enter in i['genre'] or enter in set(i['countries']):
            print(i['name'])
            file.write(str(i['name'] + '\n'))
    file.close()
    file1.close()

if save == 'csv':
    save_for = 'movies.csv'
    save_file(save_for, "w")
    file = open('qwe.csv', 'w', encoding='utf-8')
    file1 = open('movies.csv', 'r', encoding='utf-8')

    list_dict = []

    for dict_f in file1:
        dict_f = ast.literal_eval(dict_f)
        list_dict.append(dict_f)

    for i in list_dict:
        print(i)

    enter = input('Enter year, mark, countries or genre for find film: ')
    for i in list_dict:
        if enter == str(i['mark']) or enter == str(i['year']):
            print(i['name'])
            file.write(str(i['name'] + '\n'))

        elif enter in i['genre'] or enter in set(i['countries']):
            print(i['name'])
            file.write(str(i['name'] + '\n'))
    file.close()
    file1.close()

if save == 'json':
    save_for = 'movies.json'
    save_file_json(save_for, "w")
    file_json1 = open('movies.json', 'r', encoding='utf-8')
    file_write_json = open('qwe.json', 'w', encoding='utf-8')
    f1_json = json.load(file_json1)
    for i in f1_json:
        print(i)
    enter = input('Enter year, mark, countries or genre for find film: ')

    for i in f1_json:
        if enter == str(i['mark']) or enter == str(i['year']):
            print(i['name'])
            file_write_json.write(str(i['name'] + '\n'))

        elif enter in i['genre'] or enter in set(i['countries']):
            print(i['name'])
            file_write_json.write(str(i['name'] + '\n'))

    file_write_json.close()
    print(file_write_json.closed)
