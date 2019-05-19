"""
python csv_create.py src_csv dist_csv
"""
import csv
import sys

def extraction_info(x,item,index):
    if x.find(item) != -1:
        y1 = x[x.find(item):]
        y2 = y1.split()
        y3 = y2[index] 
        if y3[:1] == "[":
            y4 = y3[1:]
            y5 = y4[:-1]
            list_info = y5
        else:
            list_info = y3
    else:
        list_info = 0
    return list_info

def shape_row(x):
    itemlist = []
    a = extraction_info(x,"送信日時",2)
    b = extraction_info(x,"年会費_一般",1)
    c = extraction_info(x,"年会費_学生",1)
    d = extraction_info(x,"年次大会参加費_一般会員",1)
    e = extraction_info(x,"年次大会参加費_学生会員",1)
    f = extraction_info(x,"懇親会参加費_一般会員",1)
    g = extraction_info(x,"懇親会参加費_学生会員",1)
    h = extraction_info(x,"お弁当_6月1日分",1)
    i = extraction_info(x,"お弁当ベジタリアン_6月1日分",1)
    j = extraction_info(x,"お弁当_6月2日分",1)
    k = extraction_info(x,"お弁当ベジタリアン_6月2日分",1)
    l = extraction_info(x,"合計",1)
    m = extraction_info(x,"お名前",2)
    n = extraction_info(x,"名前(ローマ字) ",2)
    o = extraction_info(x,"所属",2)
    p = extraction_info(x,"メールアドレス",2)
    q = extraction_info(x,"電話番号",2)
    r = extraction_info(x,"支払方法",2)
     #= extraction_info(x,"",)
    itemlist.extend([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r])
    return itemlist



src= sys.argv[1] #ソースにしたいCSV
dist= sys.argv[2] #保存先CSV

data = open(src, "r") #ファイル読み込み

with open(dist, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['送信日時' , '年会費_一般' , '年会費_学生' , '年次大会参加費_一般会員' , '年次大会参加費_学生会員' , '懇親会参加費_一般会員' , '懇親会参加費_学生会員' , 'お弁当_6月1日分' , 'お弁当ベジタリアン_6月1日分' , 'お弁当_6月2日分' , 'お弁当ベジタリアン_6月2日分' , '合計' , 'お名前' , '名前(ローマ字) ' , '所属' , 'メールアドレス' , '電話番号' , '支払方法'])

    for row in data:
        #print(row)
        list = shape_row(row)
        writer.writerow(list)
        print(list)
data.close()
