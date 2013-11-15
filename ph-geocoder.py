import csv

def loaddata():
    with open('geocodes.province.csv', 'rb') as f:
        reader = csv.reader(f)
        next(reader, None) #skip header
        codelist = dict()
        #build regional codes    
        for row in reader:
            codelist[row[1]] = row[0]
            #print row[1], row[0]
    return codelist

def geocode_province():
    pass

def geocode_region():
    pass

def geocode_muni():
    pass

def check_place(placename):
    pass

data = loaddata()
for k,v in data.iteritems():
    print len(k), k + ":" + v 
    #return 0 if not a place
    #return 1 if it's region
    #return 2 if it's a province
    #return 3 if it's a munincipality








