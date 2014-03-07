import pandas as pd

data = pd.read_csv('aadhaar_data.csv')


print len(data['District'])
print len(data.ix[1])
print len(data)

'''
def mapper():
    
    for line in sys.stdin: #cycle through lines of code
        
        #Your mapper code goes here.
        #You will also need to fill out the reducer
        #code as well before test running or else you will get an error.
        
        #Each line will be
        #a comma-separated list of values.  The
        #header row WILL be included.  Tokenize
        #each row using the commas, and emit a key-
        #value pair containing the district and
        #Aadhaar generated, separated by a tab.
        #Make sure each row has the correct number
        #of tokens and is not the header row!
        
        #You can see a copy of the the input aadhaar data
        #in the link below:
        #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv
        
        #Since you are printing the actual output of program, you
        #can't print a debug statement without breaking the grader.
        #Instead, you should use the logger we've provided at the
        #top of the file.  For example,
        #logger.info("My debugging message")
        
        data = line.strip().split(',')
        #check for header row
        if data[0] == 'Registrar':
            continue

        #check for good data
        if len(data) == 12:
            for i in data:
                print '{0}\t{1}'.format(data[3], data[8])
        
mapper()'''