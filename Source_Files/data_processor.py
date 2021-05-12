
import csv


def data_processor():
    f = open("Data.tsv", 'rt')
    mycsv = csv.reader(f, delimiter="\t")
    mycsv = list(mycsv)

    #         [ROW][COL]
    # print(mycsv[12][9])
    # book = xlrd.open_workbook("Data.tsv")

    year_begin = 2015
    year_end = 2019

    if(year_begin < 2008):
        print("ERROR, earliest data is 2008")
        exit

    if(year_end > 2019):
        print("ERROR, latest data is 2019")
        exit

    # print(2+year_begin - 2008)
    # print(year_end - 2008)
    # print("----------------")
    # for i in range( (2+year_begin - 2008 ), (year_end+2 - 2008 )  ):
    #     # print("i is ",i)
    #     num = int(mycsv[11][i])
    #     print( format(num, ',')  )
    #     # print()

    alist = [11,12,51,52,91,92]

    for j in alist:
        # print(j)
        if (j==11 or j == 12):
            print("Foreigners")
        if(j==51 or j == 52):
            print("Residents")
        if (j==91 or j == 92):
            print("Total")

        for i in range((2 + year_begin - 2008), (year_end + 2 - 2008)):
            # print("i is ",i)
            num = int(mycsv[j][i])
            print(format(num, ',') , "|",end =" ")
        print("\n")

