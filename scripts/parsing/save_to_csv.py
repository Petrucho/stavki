import csv
import os

headers = ['BookMakers', 'Competitions', 'Date', 'Time', 'Team_1', 'Team_2', 'W1', 'Draw', 'W2']
# data = [['FonBet', 'World cup 2022', '20 ноября', '19:00', 'Катар', 'Эквадор', '3.70', '3.25', '2.12'], ['FonBet', 'World cup 2022', '21 ноября', '16:00', 'Англия', 'Иран', '1.30', '4.90', '12.50'], ['FonBet', 'World cup 2022', '21 ноября', '19:00', 'Сенегал', 'Нидерланды', '5.60', '3.65', '1.68'], ['FonBet', 'World cup 2022', '21 ноября', '22:00', 'США', 'Уэльс', '2.60', '3.05', '3.00'], ['FonBet', 'World cup 2022', '22 ноября', '13:00', 'Аргентина', 'Саудовская Аравия', '1.16', '7.30', '21.00'], ['FonBet', 'World cup 2022', '22 ноября', '16:00', 'Дания', 'Тунис', '1.42', '4.40', '8.50'], ['FonBet', 'World cup 2022', '22 ноября', '19:00', 'Мексика', 'Польша', '2.75', '3.15', '2.75'], ['FonBet', 'World cup 2022', '22 ноября', '22:00', 'Франция', 'Австралия', '1.22', '6.30', '15.00'], ['FonBet', 'World cup 2022', '23 ноября', '13:00', 'Марокко', 'Хорватия', '4.70', '3.30', '1.88'], ['FonBet', 'World cup 2022', '23 ноября', '16:00', 'Германия', 'Япония', '1.43', '4.70', '7.50'], ['FonBet', 'World cup 2022', '23 ноября', '19:00', 'Испания', 'Коста-Рика', '1.20', '6.30', '17.00'], ['FonBet', 'World cup 2022', '23 ноября', '22:00', 'Бельгия', 'Канада', '1.35', '5.00', '9.00'], ['FonBet', 'World cup 2022', '24 ноября', '13:00', 'Швейцария', 'Камерун', '1.73', '3.50', '5.40'], ['FonBet', 'World cup 2022', '24 ноября', '16:00', 'Уругвай', 'Южная Корея', '1.75', '3.50', '5.20'], ['FonBet', 'World cup 2022', '24 ноября', '19:00', 'Португалия', 'Гана', '1.42', '4.30', '9.00'], ['FonBet', 'World cup 2022', '24 ноября', '22:00', 'Бразилия', 'Сербия', '1.45', '4.50', '7.60'], ['FonBet', 'World cup 2022', '25 ноября', '13:00', 'Уэльс', 'Иран', '2.25', '3.05', '3.70'], ['FonBet', 'World cup 2022', '25 ноября', '16:00', 'Катар', 'Сенегал', '3.90', '3.15', '2.10'], ['FonBet', 'World cup 2022', '25 ноября', '19:00', 'Нидерланды', 'Эквадор', '1.63', '4.00', '5.40'], ['FonBet', 'World cup 2022', '25 ноября', '22:00', 'Англия', 'США', '1.65', '3.90', '5.50'], ['FonBet', 'World cup 2022', '26 ноября', '13:00', 'Тунис', 'Австралия', '2.85', '3.00', '2.75'], ['FonBet', 'World cup 2022', '26 ноября', '16:00', 'Польша', 'Саудовская Аравия', '1.63', '3.85', '5.70'], ['FonBet', 'World cup 2022', '26 ноября', '19:00', 'Франция', 'Дания', '2.00', '3.35', '4.00'], ['FonBet', 'World cup 2022', '26 ноября', '22:00', 'Аргентина', 'Мексика', '1.57', '3.90', '6.40'], ['FonBet', 'World cup 2022', '27 ноября', '13:00', 'Япония', 'Коста-Рика', '1.85', '3.35', '4.70'], ['FonBet', 'World cup 2022', '27 ноября', '16:00', 'Бельгия', 'Марокко', '1.52', '4.20', '6.50'], ['FonBet', 'World cup 2022', '27 ноября', '19:00', 'Хорватия', 'Канада', '1.77', '3.80', '4.60'], ['FonBet', 'World cup 2022', '27 ноября', '22:00', 'Испания', 'Германия', '2.55', '3.35', '2.80'], ['FonBet', 'World cup 2022', '28 ноября', '13:00', 'Камерун', 'Сербия', '4.40', '3.40', '1.90'], ['FonBet', 'World cup 2022', '28 ноября', '16:00', 'Южная Корея', 'Гана', '2.70', '2.95', '2.95'], ['FonBet', 'World cup 2022', '28 ноября', '19:00', 'Бразилия', 'Швейцария', '1.50', '4.20', '7.20'], ['FonBet', 'World cup 2022', '28 ноября', '22:00', 'Португалия', 'Уругвай', '2.08', '3.35', '3.70'], ['FonBet', 'World cup 2022', '29 ноября', '18:00', 'Эквадор', 'Сенегал', '2.95', '3.20', '2.55'], ['FonBet', 'World cup 2022', '29 ноября', '18:00', 'Нидерланды', 'Катар', '1.32', '5.20', '10.00'], ['FonBet', 'World cup 2022', '29 ноября', '22:00', 'Уэльс', 'Англия', '6.10', '4.00', '1.58'], ['FonBet', 'World cup 2022', '29 ноября', '22:00', 'Иран', 'США', '3.45', '3.35', '2.15'], ['FonBet', 'World cup 2022', '30 ноября', '18:00', 'Австралия', 'Дания', '6.70', '3.70', '1.60'], ['FonBet', 'World cup 2022', '30 ноября', '18:00', 'Тунис', 'Франция', '14.00', '5.60', '1.25'], ['FonBet', 'World cup 2022', '30 ноября', '22:00', 'Польша', 'Аргентина', '5.00', '4.00', '1.68'], ['FonBet', 'World cup 2022', '30 ноября', '22:00', 'Саудовская Аравия', 'Мексика', '6.40', '4.15', '1.55'], ['FonBet', 'World cup 2022', '1 декабря', '18:00', 'Канада', 'Марокко', '3.25', '3.30', '2.30'], ['FonBet', 'World cup 2022', '1 декабря', '18:00', 'Хорватия', 'Бельгия', '3.95', '3.65', '1.90'], ['FonBet', 'World cup 2022', '1 декабря', '22:00', 'Коста-Рика', 'Германия', '10.50', '5.30', '1.30'], ['FonBet', 'World cup 2022', '1 декабря', '22:00', 'Япония', 'Испания', '10.00', '5.40', '1.30'], ['FonBet', 'World cup 2022', '2 декабря', '18:00', 'Гана', 'Уругвай', '4.80', '3.60', '1.78'], ['FonBet', 'World cup 2022', '2 декабря', '18:00', 'Южная Корея', 'Португалия', '9.00', '4.70', '1.38'], ['FonBet', 'World cup 2022', '2 декабря', '22:00', 'Камерун', 'Бразилия', '9.50', '5.20', '1.35'], ['FonBet', 'World cup 2022', '2 декабря', '22:00', 'Сербия', 'Швейцария', '2.80', '3.45', '2.50']]

def save_to_file(data_row):  
  filename = './data/data.csv'
  try:
    if os.path.isfile(filename):  
      # add data to existing file
      with open(filename, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        # writer.writerow(headers)

        # write multiple rows
        writer.writerows(data_row)
        # print('look like successfully write to file')
    else:
      # creating new file with headers and data
      with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(headers)

        # write multiple rows
        writer.writerows(data_row)
        # print('look like successfully write to file')

  except IOError as exception:
      print(f'some error happen with saving to file!!: {filename}\n{IOError("%s: %s" % (filename, exception.strerror))}')
  
  return None

# save_to_file(data)