# My First Data Miner Program

'''
This program
a) performs data cleaning process to remove missing attribute values present in the database.
b) calculates probability of being breast cancer of an imaginary patient
   by evaluationg his/her sample results provided as command-line argument.
'''
#START OF 1.PY

import sys
import copy

dataFile = open('WBC.data', 'r').read()
dataDic = {i.split(',')[0]: i.split(',')[1:] for i in dataFile.split('\n')}
for ids in dataDic:
    for indx, value in enumerate(dataDic[ids]):
       if value.isdigit():
           dataDic[ids][indx] = int(value)

def funDataClean():
    total = 0
    dataDic_copy = copy.deepcopy(dataDic)
    for j in sorted(dataDic):
        attribute_values = []
        if "?" in dataDic[j]:
            class_canser = dataDic[j][9]
            question_index = dataDic[j].index("?")
            for i in sorted(dataDic):
                if dataDic[i][9] != class_canser:
                    dataDic_copy.pop(i)
            for k in sorted(dataDic_copy):
                if type(dataDic_copy[k][question_index]) is int:
                    attribute_values.append(dataDic_copy[k][question_index])
            AV = round(sum(attribute_values) / len(attribute_values))
            dataDic[j][question_index] = AV
            total += AV
            dataDic_copy = copy.deepcopy(dataDic)
    average = total / 21
    print('The average of all missing values is  : ' + '{0:.4f}'.format(average))

y = sys.argv[1].split(",")
patient_data = []
for i in y:
    if "?" is i:
        patient_data.append(list(i))
    else:
        patient_data.append(i.split(":"))
for i in patient_data:
    if "?" not in i:
        i[1] = int(i[1])

def performStepWiseSearch():
    prob = []
    m = 0
    b = 0
    index = 0
    for i in patient_data:
        if "?" in i:
            for j in sorted(dataDic):
                prob.append(j)
        elif "<" in i and "<=" not in i:
            for j in dataDic:
                if dataDic[j][index] < i[1]:
                    prob.append(j)
        elif "<=" in i:
            for j in dataDic:
                if dataDic[j][index] <= i[1]:
                    prob.append(j)
        elif ">" in i and ">=" not in i:
            for j in dataDic:
                if dataDic[j][index] > i[1]:
                    prob.append(j)
        elif ">=" in i:
            for j in dataDic:
                if dataDic[j][index] >= i[1]:
                    prob.append(j)
        elif "!=" in i:
            for j in dataDic:
                if dataDic[j][index] != i[1]:
                    prob.append(j)
        elif "=" in i and "!=" not in i:
            for j in dataDic:
                if dataDic[j][index] == i[1]:
                    prob.append(j)
        index +=1

    for k in sorted(dataDic):
        if prob.count(k) == 9:
            if dataDic[k][9] == "malignant":
                m += 1
            elif dataDic[k][9] == "benign":
                b += 1
    probability = m / (m + b)
    print('\nTest Results:\n'
          '----------------------------------------------'
          '\nPositive (malignant) cases            : ' + str(m) +
          '\nNegative (benign) cases               : ' + str(b) +
          '\nThe probability of being positive     : ' + '{0:.4f}'.format(probability) +
          '\n----------------------------------------------')

funDataClean()
performStepWiseSearch()

#end of 1.py file
