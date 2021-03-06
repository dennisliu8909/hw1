# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061222.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
id_list = ["C0A880", "C0F9A0", "C0G640", "C0R190", "C0X260"]   # specific station_id
output_list = []  # output list
correct_data = list(filter(lambda item: item['WDSD'] != ('-99.000' or '-999.000'), data)) # delet unexpected data
for station in id_list:    # find WDSD range of specific stations
   target_data = list(filter(lambda item: item['station_id'] == station, correct_data))
   maximum = target_data[0]['WDSD']
   minimum = target_data[0]['WDSD']
   for row in target_data:    # find maximum WDSD and minimum WDSD of specific station
      if row['WDSD'] > maximum:
         maximum = row['WDSD']
      elif row['WDSD'] < minimum:
         minimum = row['WDSD']
   if len(target_data) == 1:  # if there is only one data then there is no range for WDSD
      wd_range = 'None'
   else:
      wd_range = float(maximum) - float(minimum)
   ans_list = [station, wd_range]   # the WDSD range of each station
   output_list.append(ans_list)  # put each ans_list to the final output list
   

#=======================================

# Part. 4
#=======================================
# Print result
print(output_list)
#========================================