    
# Python Code to Inject CSV into SAS Event Stream Processing via HTTP RESTful webservices

import os,sys,csv,re
import requests
import time, datetime
import random

################################################################################################################################
#
#   Inputs
#
################################################################################################################################

host                = 'localhost'
port                = '61051'

project_name        = 'Project'
cont_query_name     = 'CQ'
source_name         = 'Data_Stream'

################################################################################################################################
#
#   Inject CSV into ESP via HTTP Webservices
#
################################################################################################################################


url     = 'http://localhost:61051/SASESP/windows/Project/CQ/Data_Stream/state?value=injected'
headers = {'Content-Type': 'application/xml'}

 
counter    = 1000000
start_time = datetime.datetime.now()

# Loop through CSV file k times
for k in range(10):
    
    with open('truck.csv') as csvfile:
        data = csv.reader(csvfile)
        for i,row in enumerate(data):
            
            # Grab Header Row
            if i==0:
                header = row
            
            # Process all other rows
            else:
                counter = counter + 1
                
                request_string = '''
                <events>
                    <event>
                        <opcode>i</opcode>'''
                
                #request_string = request_string + '\n<timestamp>' + re.sub('\..+','',str(datetime.datetime.now())) + '</timestamp>'
                #request_string = request_string + '\n<records_per_sec>' + str(counter / float((datetime.datetime.now()-start_time).seconds)) + '</records_per_sec>'
                
                for i in range(len(header)):
                    if header[i].strip() == 'record_id':
                        #request_string = request_string + '\n<' + str(header[i]) + ' key="true">' + str(row[i]) + '</' + str(header[i]) + '>'
                        request_string = request_string + '\n<' + str(header[i]) + ' key="true">' + str(counter) + '</' + str(header[i]) + '>'
                    elif header[i].strip() == 'Vehicle_id':
                        request_string = request_string + '\n<' + str(header[i]) + ' key="true">' + str(row[i])  + '</' + str(header[i]) + '>'
                    else:
                        request_string = request_string + '\n<' + str(header[i]) + '>' + str(row[i]) + '</' + str(header[i]) + '>'
                
                request_string = request_string + '''
                    </event>
                </events>
                '''
                
                #print str(request_string)
                
                requests.put(url, data=request_string.strip(), headers=headers)
                
                if counter >= 1000100: 
                    time.sleep(0.20)


#ZEND
