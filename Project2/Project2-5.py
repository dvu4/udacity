import csv
#import pandas
#import numpy as np

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. 
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    for name in filenames:
        # your code here
        ifile  = open(name, "rb")
        reader = csv.reader(ifile)
        outputfile = 'updated_' + name
        ofile  = open(outputfile, "wb")
        writer = csv.writer(ofile, delimiter=',')#, quotechar='', quoting=csv.QUOTE_ALL)

        for row in reader:
            '''
            count = 1
            for i in row:
                if not(count == 1 or count == 2 or count ==3):
                    print count
                count = count+1
'''
            if (row[3][:3] != '06-'):
                if not(not row[3:8]):
                    writer.writerow(row[0:3] + row[3:8])
                if not(not row[8:13]):
                    writer.writerow(row[0:3] + row[8:13])
                if not(not row[13:18]):
                    writer.writerow(row[0:3] + row[13:18])
                if not(not row[18:23]):
                    writer.writerow(row[0:3] + row[18:23])
                if not(not row[23:28]):
                    writer.writerow(row[0:3] + row[23:28])
                if not(not row[28:33]):
                    writer.writerow(row[0:3] + row[28:33])
                if not(not row[33:38]):
                    writer.writerow(row[0:3] + row[33:38])
                if not(not row[38:43]):
                    writer.writerow(row[0:3] + row[38:43])
                if not(not row[43:48]):
                    writer.writerow(row[0:3] + row[43:48])
                if not(not row[48:53]):
                    writer.writerow(row[0:3] + row[48:53])




        ifile.close()
        ofile.close()
        
        '''with open(name) as csvFile:
            mtaData = pandas.read_csv(csvFile, header = False, dtype = {0:np.str, 1: np.str, 2: np.str, 3:np.str, 4:np.str, 5:np.str, 6: np.str, 7: np.str})
            mtaData = mtaData.ix[:, 0:8]
        outputfile = 'updated_' + name
        mtaData.to_csv(outputfile, header = False, index = False)'''
