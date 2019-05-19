"""
python csv_create.py src_csv dist_csv
"""
import csv
import sys
from extraction_info import extraction_info


def shape_row(x):
    itemlist = []
    a = extraction_info(x,"submission date and time",2)
    b = extraction_info(x,"Annual_Membership_Fee_Regular",1)
    c = extraction_info(x,"Annual_Membership_Fee_Student",1)
    d = extraction_info(x,"J-SLA2019_Conference_Registration_Fee_Regular",1)
    e = extraction_info(x,"J-SLA2019_Conference_Registration_Fee_Student",1)
    f = extraction_info(x,"J-SLA2019_Conference_Banquet_Regular",1)
    g = extraction_info(x,"J-SLA2019_Conference_Banquet_Student",1)
    h = extraction_info(x,"Standard_Saturday_1st_June",1)
    i = extraction_info(x,"Vegetarian_Saturday_1st_June",1)
    j = extraction_info(x,"Standard_Sunday_2nd_June",1)
    k = extraction_info(x,"Vegetarian_Sunday_2nd_June",1)
    l = extraction_info(x,"[total]",1)
    m = extraction_info(x,"Name (in your native language)",2)
    n = extraction_info(x,"Name (in English) ",2)
    o = extraction_info(x,"Affiliation",2)
    p = extraction_info(x,"Email address",2)
    q = extraction_info(x,"Telephone (cell phone number preferred)",2)
    r = extraction_info(x,"Payment type",2)
     #= extraction_info(x,"",)
    itemlist.extend([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r])
    return itemlist



src= sys.argv[1] #ソースにしたいCSV
dist= sys.argv[2] #保存先CSV

data = open(src, "r") #ファイル読み込み

with open(dist, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['submission date and time' , 'Annual_Membership_Fee_Regular' , 'Annual_Membership_Fee_Student' , 'J-SLA2019_Conference_Registration_Fee_Regular' , 'J-SLA2019_Conference_Registration_Fee_Student' , 'J-SLA2019_Conference_Banquet_Regular' , 'J-SLA2019_Conference_Banquet_Student' , 'Standard_Saturday_1st_June' , 'Vegetarian_Saturday_1st_June' , 'Standard_Sunday_2nd_June' , 'Vegetarian_Sunday_2nd_June' , '[total]' , 'Name (in your native language)' , 'Name (in English) ' , 'Affiliation' , 'Email address' , 'Telephone (cell phone number preferred)' , 'Payment type'])

    for row in data:
        #print(row)
        list = shape_row(row)
        writer.writerow(list)
        #print(list)
data.close()
