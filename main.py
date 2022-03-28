import csv
import numpy as np

#Ask what file to read--simulate uploading file
FILENAME= 'csv_template.csv'

# Function to read file and output the file headers
def read_file(FILENAME):
  with open(FILENAME, mode='r') as csv_file:
      #csvFile = csv.reader(csv_file)
      reader = csv.reader(csv_file)
      headers = next(reader)
      print(', '.join(headers))
    
# Function to get user input
def get_input():
  selected = input("What section(s) would you like to focus on?\nEnter here: ").split()
  return selected

#Function that uses input to print the selected columns
def print_columns(selected):
  with open(FILENAME, newline="") as csvfile:
      data = list(csv.DictReader(csvfile))
      for element in selected:
          print(element)  # print selected header
          print("---------------------------------")
          for column in data:  
              print(column[element])  # print data
          print("\n")

# Function to find the average of given columns
def column_average(FILENAME):
  readdata = csv.reader(open(FILENAME, 'r'))
  data = []
  
  for row in readdata:
    data.append(row)

  data.pop(0) #delete headers
  
  avgcost = []  
  avgpaid = []
  avgowed = []
  
  for i in range(len(data)):
    avgcost.append(float(data[i][2])) #avg of Cost
    avgpaid.append(float(data[i][3])) #avg of Paid
    avgowed.append(float(data[i][4])) #avg of Owed

    
  #Get the average of Cost, Paid, and Owed Columns
  C_avg = np.mean(avgcost)
  C_avg = round(C_avg, 2)
  P_avg = np.mean(avgpaid)
  P_avg = round(P_avg, 2)
  O_avg = np.mean(avgowed)
  O_avg = round(O_avg, 2)
  print ('Mean of Cost:', '$', C_avg)
  print ('Mean of Paid :', '$', P_avg)
  print ('Mean of Owed :', '$', O_avg)

# Code to run the script
read_file(FILENAME)
print_columns(get_input())
column_average(FILENAME)
