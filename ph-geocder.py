import csv

load_geocodes(level):
    with open('geocodes.province.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None) #skip header
    codelist = dict()

    #build regional codes    
    for row in reader:
            codelist[row[1]] = row[0]
            #print row[1], row[0]
    return codelist

geocode_province():

geocode_region():

geocode_muni():

check_place(placename):
    
    #return 0 if not a place
    #return 1 if it's region
    #return 2 if it's a province
    #return 3 if it's a munincipality








