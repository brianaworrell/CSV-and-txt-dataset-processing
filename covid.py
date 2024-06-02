import csv
from collections import Counter

def p1 (covidtrain):
    outfile = open('result1.csv', "w")
    reader = csv.reader(open(covidtrain))
    header = [] 
    header = next(reader) 
    writer = csv.DictWriter(outfile, fieldnames=header)
    writer.writeheader()
    reader = csv.DictReader(open(covidtrain))
    for num,row in enumerate(reader):
        ages = row['age'].split('-')
        if len(ages) > 1:
            new = (int(ages[0]) + int(ages[1])) / 2
            row['age'] = str(round(new))
        writer.writerow(row)

def p2 (result1):
    outfile = open('result2.csv', "w")
    reader = csv.reader(open(result1))
    header = [] 
    header = next(reader) 
    writer = csv.DictWriter(outfile, fieldnames=header)
    writer.writeheader()
    reader = csv.DictReader(open(result1))
    tochange = ['date_onset_symptoms', 'date_admission_hospital', 'date_confirmation']
    for num,row in enumerate(reader):
        for x in tochange:
            og = row[x]
            parts = og.split('.')
            new = (parts[1] + '.' + parts[0] + '.' + parts[2])
            row[x] = new
        writer.writerow(row)

def p3 (result2):
    outfile = open('result3.csv', "w")
    reader = csv.reader(open(result2))
    header = [] 
    header = next(reader) 
    writer = csv.DictWriter(outfile, fieldnames=header)
    writer.writeheader()
    reader = csv.DictReader(open(result2))
    lats = {}
    longs = {}
    for num,row in enumerate(reader):
        if row['latitude'] != 'NaN':
            if row['province'] in lats:
                lats[row['province']].append(int(float(row['latitude'])))
            else:
                lats[row['province']] = [int(float(row['latitude']))]
        if row['longitude'] != 'NaN':
            if row['province'] in longs:
                longs[row['province']].append(int(float(row['longitude'])))
            else:
                longs[row['province']] = [int(float(row['longitude']))]
    provinces = {}
    for x in lats:
        latave = sum(lats[x]) / len(lats[x])
        latave = round(latave, 2)
        longave = sum(longs[x]) / len(longs[x])
        longave = round(longave, 2)
        provinces[x] = [str(latave), str(longave)]
    reader = csv.DictReader(open(result2))
    for num,row in enumerate(reader):
        if row['latitude'] == 'NaN':
            row['latitude'] = provinces[row['province']][0]
        if row['longitude'] == 'NaN':
            row['longitude'] = provinces[row['province']][1]
        writer.writerow(row)

def getcities (result3):
    reader = csv.DictReader(open(result3))
    provinces = {}
    for num,row in enumerate(reader):
        if row['city'] != 'NaN':
            if row['province'] in provinces:
                provinces[row['province']].append(row['city'])
            else:
                provinces[row['province']] = [row['city']]
    counts = {}
    for x in provinces:
        counts[x] = Counter(provinces[x])
    mostcommon = {}
    for y in counts:
        ties = []
        occurences = counts[y].most_common(1)[0][1]
        for z in counts[y]:
            if counts[y][z] == occurences:
                ties.append(z)
        ties.sort()
        mostcommon[y] = ties[0]
    return mostcommon

def p4 (result3):
    cities = getcities(result3)
    outfile = open('result4.csv', "w")
    reader = csv.reader(open(result3))
    header = [] 
    header = next(reader) 
    writer = csv.DictWriter(outfile, fieldnames=header)
    writer.writeheader()
    reader = csv.DictReader(open(result3))
    for num,row in enumerate(reader):
        if row['city'] == 'NaN':
            row['city'] = cities[row['province']]
        writer.writerow(row)

def getsymptoms (result4):
    reader = csv.DictReader(open(result4))
    provinces = {}
    for num,row in enumerate(reader):
        if row['symptoms'] != 'NaN':
            parts = row['symptoms'].split(';')
            if row['province'] in provinces:
                for x in parts:
                    provinces[row['province']].append(x.strip())
            else:
                for x in range(len(parts)):
                    parts[x] = parts[x].strip()
                provinces[row['province']] = parts
    counts = {}
    for x in provinces:
        counts[x] = Counter(provinces[x])
    mostcommon = {}
    for y in counts:
        ties = []
        occurences = counts[y].most_common(1)[0][1]
        for z in counts[y]:
            if counts[y][z] == occurences:
                ties.append(z)
        ties.sort()
        mostcommon[y] = ties[0]
    return mostcommon

def p5 (result4):
    symptoms = getsymptoms(result4)
    outfile = open('covidResult.csv', "w")
    reader = csv.reader(open(result4))
    header = [] 
    header = next(reader) 
    writer = csv.DictWriter(outfile, fieldnames=header)
    writer.writeheader()
    reader = csv.DictReader(open(result4))
    for num,row in enumerate(reader):
        if row['symptoms'] == 'NaN':
            row['symptoms'] = symptoms[row['province']]
        writer.writerow(row)

def main():
    covidtrain = 'covidTrain.csv'
    p1(covidtrain)
    p2('result1.csv')
    p3('result2.csv')
    p4('result3.csv')
    p5('result4.csv')

if __name__=="__main__": 
    main()