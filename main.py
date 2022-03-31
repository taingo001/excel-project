import csv
import numpy as np
    
# Function to find the average of given columns
def column_average():
  readdata = csv.reader(open("csv_template.csv", 'r'))
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
