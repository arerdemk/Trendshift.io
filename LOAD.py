from TRANSFORM import *
import datetime


def first():
    x=datetime.datetime.now()
    return print(f'Baslangic:{x}')


def last():
    y=datetime.datetime.now()
    return print(f'Bitis:{y}')

first()


# #### finitomento
# Transform(2101,2400).determine('2101-2400')
# Transform(2401,2700).determine('2401-2700')
# Transform(2701,3000).determine('2701-3000')
# Transform(3001,3300).determine('3001-3300') #Bitis:2024-08-14 11:41:02.570361

#Transform(3301,3600).determine('3301-3600') #Baslangic:2024-08-14 11:55:31.012460 ##Bitis:2024-08-14 12:39:54.622223

Transform(3601,3900).determine('3601-3900')
# Transform(3901,4100).determine('3901-4100')
# Transform(4101,4400).determine('4101-4400')
# Transform(4401,4700).determine('4401-4700')
# Transform(4701,5000).determine('4701-5000')





#### SU LAST ROWA EKLEME MUHABBETINI OGREN BOYLECE FAZLA SPREADSHEET YA DA FILE ILE UGRASMAZSIN

last()
