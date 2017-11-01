# My First Data Miner Program

'''
This program
a) performs data cleaning process to remove missing attribute values present in the database.
b) calculates probability of being breast cancer of an imaginary patient
   by evaluationg his/her sample results provided as command-line argument.
'''

# Starter code that reads database named 'WBC.data' and loads it into a dictionary 'dataDic'

# Reads the datafile. Note: WBC.data should be located where this file belongs.
dataFile = open('WBC.data','r').read()

# Makes data file ready to use by assigning every record to a dictionary class name dataDic.
dataDic = {i.split(',')[0]: i.split(',')[1:]  for i in dataFile.split('\n')} 

# Do not alter any upper lines so that you do not get trouble in loading data file

# Performs data cleaning process, design the content and arguments depending on your design
def funDataClean():


# Performas step-wise search in WBC database, design the content and arguments depending on your design
def performStepWiseSearch():


# 1st phase: Cleaning WBC Database

print('The average of all missing values is  : ' + '{0:.4f}'.format())

# 2nd phase: Retrieving knowledge from WBC dataset

print('\nTest Results:\n'
      '----------------------------------------------'
      '\nPositive (malignant) cases            : ' + str() +
      '\nNegative (benign) cases               : ' + str() +
      '\nThe probability of being positive     : ' + '{0:.4f}'.format() +
      '\n----------------------------------------------')
	  
	  
# end of the 1.py file