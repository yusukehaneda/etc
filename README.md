# etc

一時的に作ったスクリプトとかをおく場所

## csv_create_[jp|en].pyの利用例
```
 $ python csv_create_jp.py 201904.cgi result_jp.csv
 $ python csv_create_jp.py 201905.cgi result_201905jp.csv
 $ cat result_201905jp.csv | tail -n +2 >> result_jp.csv
```
