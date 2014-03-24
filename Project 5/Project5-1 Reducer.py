import sys

def reducer():
    '''
    Given the output of the mapper for this assignment, simply print
    0 and then the average number of riders per day for the month of 05/2011,
    separated by a tab.
    
    There are 31 days in 05/2011.
    
    Example output might look like this:
    0   10501050.0
    '''

    riders = 0
    old_key = None

    sumValue = 0.0
    daysInMonth = 31.0

    for line in sys.stdin:

        data = line.strip().split('\t')

        sumValue += float(data[1])

    print '0\t{0}'.format(sumValue / daysInMonth)


reducer()
