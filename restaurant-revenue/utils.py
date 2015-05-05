import datetime

# less categorical data, so just used dictionaries.

TYPE_DICT = {'IL' : 1, 'FC' : 2, 'DT' : 3}

CITY_DICT = {'\xc4\xb0zmir': 1, '': 2, 'Mu\xc4\x9fla': 3, 
'Tekirda\xc4\x9f': 4, 'K\xc3\xbctahya': 5, 'Afyonkarahisar': 6, 
'Adana': 7, 'K\xc4\xb1rklareli': 8, 'Elaz\xc4\xb1\xc4\x9f': 9, 
'Ayd\xc4\xb1n': 10, 'Gaziantep': 11, 'Ankara': 12, 'Kayseri': 13, 
'Sakarya': 33, 'Tokat': 15, 'Eski\xc5\x9fehir': 17, 'Bolu': 18, 
'\xc5\x9eanl\xc4\xb1urfa': 19, 'Trabzon': 20, 'Kocaeli': 21, 'Samsun': 22, 
'U\xc5\x9fak': 23, 'Kastamonu': 24, 'Antalya': 34, 'Karab\xc3\xbck': 25, 
'Isparta': 26, 'Denizli': 27, 'Diyarbak\xc4\xb1r': 35, 'Osmaniye': 29, 
'Amasya': 30, 'Bal\xc4\xb1kesir': 31, 'Bursa': 32, 'Edirne': 14, 
'\xc4\xb0stanbul': 16, 'Konya': 28}

GROUP_DICT = {'Big Cities' : 1, 'Other' : 2}



def city_conv(x):
    if x in CITY_DICT:
        return CITY_DICT[x]
    else:
        return 0

def type_conv(x):
    if x in TYPE_DICT:
        return TYPE_DICT[x]
    else:
        return 0

def group_conv(x):
    if x in GROUP_DICT:
        return GROUP_DICT[x]
    else:
        return 0

def f(x):
    try:
        val = float(x)
        return val
    except:
        return 0

def date_processing(pd_date):
    t = datetime.datetime(pd_date.year, pd_date.month, pd_date.day, 0, 0, 0)
    return (t-datetime.datetime(1970,1,1)).total_seconds()