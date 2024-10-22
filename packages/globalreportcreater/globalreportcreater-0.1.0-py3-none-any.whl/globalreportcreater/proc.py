import csv


def create_report(input,output):
    with (open(input, 'r', encoding='utf-8') as csv_file):
        reader = csv.DictReader(csv_file)
        ageGroup = {
            '18-24': 0,
            '25-39': 0,
            '40+': 0
        }
        city = {}
        ct = 0

        for row in reader:
            ct += 1

            if row['city'] in city.keys():
                city[row['city']] += 1
            else: city[row['city']] = 1

            age = row['age']
            if int(age) >= 40:
                ageGroup['40+'] += 1
            elif int(age) >= 25:
                ageGroup['25-39'] += 1
            else : ageGroup['18-24'] += 1

        with open(output, 'a', encoding='utf-8') as f:
            f.write(f'Общее кол-во клиентов: {ct}\n')
            f.write(f'Кол-во клиентов по возрастным группам:\n')
            for key, value in ageGroup.items():
                f.write(f'  {key}: {value}\n')
            f.write(f'Распределение клиентов по городам:\n')
            for key,value in city.items():
                f.write(f'  {key}: {value}\n')
