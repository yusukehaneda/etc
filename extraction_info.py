
def extraction_info(x,item,index):
    if x.find(item) != -1:
        y1 = x[x.find(item):]
        if index == 1:
          y2 = y1.split()
          item = y2[index] 
        else:
          y2 = y1.split('\t')[0]
          y3 = y2[y2.find("="):]
          y4 = y3[2:]
          print(y4)
          item = y4
        if item[:1] == "[":
            item_lsplit = item[1:]
            item_rsplit = item_lsplit[:-1]
            list_info = item_rsplit
        else:
            list_info = item
    else:
        list_info = 0
    return list_info

