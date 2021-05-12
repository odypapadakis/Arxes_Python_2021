
import csv


def data_processor():
    f = open("Data.tsv", 'rt')
    mycsv = csv.reader(f, delimiter="\t")
    mycsv = list(mycsv)

    #         [ROW][COL]
    print(mycsv[12][9])
    # book = xlrd.open_workbook("Data.tsv")
    