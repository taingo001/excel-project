import csv

#Read file and output the file headers
with open('test-file.csv', mode='r') as csv_file:
    csvFile = csv.reader(csv_file)
    collum_count = 0
    reader = csv.reader(csv_file)
    headers = next(reader)
    print(headers)
    
#Get user input
a,b = input("What section(s) would you like to focus on?").split()

#Print new line
print('\n')

#Use input to print the selected columns
with open('test-file.csv', newline='') as csvfile:
  data = csv.DictReader(csvfile)
  print(a) #print selected header
  print("---------------------------------")
  for column in data:
    print(column[a]) #print data

#Print new line
print('\n')

with open('test-file.csv', newline='') as csvfile:
  data = csv.DictReader(csvfile)
  print(b) #print selected header
  print("---------------------------------")
  for column in data:
    print(column[b]) #print data

