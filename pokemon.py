import csv
from collections import Counter

def p1 (pokemontrain):
    reader = csv.DictReader(open(pokemontrain))   
    over40 = 0
    under40 = 0
    for num,row in enumerate(reader):         
        if row['type'] == 'fire':                     
            if int(float(row['level'])) >= 40:
                over40 = over40 + 1
            else:
                under40 = under40 + 1
    percentage = round(100 * over40 / (over40 + under40))
    output = open("pokemon1.txt", "w")
    output.write('Percentage of fire type Pokemons at or above level 40 = ' + str(percentage))

def getweaktype (pokemontrain):
    reader = csv.DictReader(open(pokemontrain))
    weaknesses = {}
    for num,row in enumerate(reader):  
        if row['weakness'] in weaknesses:
            weaknesses[row['weakness']].append(row['type'])
        else:
            weaknesses[row['weakness']] = [row['type']]
    counts = {}
    for x in weaknesses:
        counts[x] = Counter(weaknesses[x])
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

def getoveraverage (pokemontrain):
    reader = csv.DictReader(open(pokemontrain))
    atk = []
    defs = []
    hp = []
    for num,row in enumerate(reader):
        if int(float(row['level'])) > 40:
            if row['atk'] != 'NaN':
                atk.append(float(row['atk']))
            if row['def'] != 'NaN':
                defs.append(float(row['def']))
            if row['hp'] != 'NaN':
                hp.append(float(row['hp']))
    averageatk = sum(atk) / len(atk)
    averagedef = sum(defs) / len(defs)
    averagehp = sum(hp) / len(hp)
    return [round(averageatk,1), round(averagedef,1), round(averagehp,1)]

def getunderaverage (pokemontrain):
    reader = csv.DictReader(open(pokemontrain))
    atk = []
    defs = []
    hp = []
    for num,row in enumerate(reader):
        if int(float(row['level'])) <= 40:
            if row['atk'] != 'NaN':
                atk.append(float(row['atk']))
            if row['def'] != 'NaN':
                defs.append(float(row['def']))
            if row['hp'] != 'NaN':
                hp.append(float(row['hp']))
    averageatk = sum(atk) / len(atk)
    averagedef = sum(defs) / len(defs)
    averagehp = sum(hp) / len(hp)
    return [round(averageatk,1), round(averagedef,1), round(averagehp,1)]

def p2 (pokemontrain):
    weaktypes = getweaktype(pokemontrain)
    overstats = getoveraverage(pokemontrain)
    understats = getunderaverage(pokemontrain)
    outfile = open('pokemonResult.csv', "w")
    reader = csv.reader(open(pokemontrain))
    header = [] 
    header = next(reader) 
    writer = csv.DictWriter(outfile, fieldnames=header)
    writer.writeheader()
    reader = csv.DictReader(open(pokemontrain))
    for num,row in enumerate(reader):
        if row['type'] == 'NaN':
            row['type'] = weaktypes[row['weakness']]
        if row['atk'] == 'NaN':
            if int(float(row['level'])) > 40:
                row['atk'] = overstats[0]
            else:
                row['atk'] = understats[0]
        if row['def'] == 'NaN':
            if int(float(row['level'])) > 40:
                row['def'] = overstats[1]
            else:
                row['def'] = understats[1]
        if row['hp'] == 'NaN':
            if int(float(row['level'])) > 40:
                row['hp'] = overstats[2]
            else:
                row['hp'] = understats[2]
        writer.writerow(row)

def p4 (results):
    data = {}
    reader = csv.DictReader(open(results))   
    for num,row in enumerate(reader):
        thistype = row['type']
        pers = row['personality']
        if thistype in data:
            if pers in data[thistype]:
                pass
            else:
                data[thistype].append(pers)
        else:
            data[thistype] = [pers]
    types = dict(sorted(data.items()))
    for x in types:
        types[x].sort()
    output = open("pokemon4.txt", "w")
    output.write('Pokemon type to personality mapping:' + '\n\n')
    for x in types:
        perstr = types[x][0]
        for y in range(1,len(types[x])):
            perstr = perstr + ', ' + types[x][y]
        output.write('\t' + x + ': ' + perstr + '\n')

def p5 (results):
    hp = []
    reader = csv.DictReader(open(results))   
    for num,row in enumerate(reader):
        if row['stage'] == '3.0':
            hp.append(float(row['hp']))
    average = round(sum(hp)/len(hp))
    output = open("pokemon5.txt", "w")
    output.write('Average hit points for Pokemons of stage 3.0 = ' + str(average))    

def main():
    pokemontrain = 'pokemonTrain.csv'
    p1(pokemontrain)
    p2(pokemontrain)
    p4('pokemonResult.csv')
    p5('pokemonResult.csv')

if __name__=="__main__": 
    main()