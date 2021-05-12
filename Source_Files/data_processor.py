
import csv


def data_processor():

    f = open("Data.tsv", 'rt')

    in_tsv = csv.reader(f, delimiter="\t")

    # Make it into a list
    in_tsv = list(in_tsv)

    #         [ROW][COL]
    # print(in_tsv[12][9])
    # book = xlrd.open_workbook("Data.tsv")

    year_begin = 2016
    year_end = 2019

    if(year_begin < 2008):
        print("ERROR, earliest data is 2008")
        exit(1)

    if(year_end > 2019):
        print("ERROR, latest data is 2019")
        exit(1)

    # print(2+year_begin - 2008)
    # print(year_end - 2008)
    # print("----------------")
    # for i in range( (2+year_begin - 2008 ), (year_end+2 - 2008 )  ):
    #     # print("i is ",i)
    #     num = int(in_tsv[11][i])
    #     print( format(num, ',')  )
    #     # print()
    #            FOR,LOC,TOTAL
    Row_list_GR = [11,51,91]
    Row_list_ES = [12,52,92]
    Type = ["FOREIGNERS","LOCALS","TOTAL"]

    Column_list_years = [9,10,11,12]

    # print("-----------DEBUG--------------------------------------")
    # #           [ROW][COL]
    # for i in Column_list_years:
    #     print(in_tsv[0][i])
    #
    # print("-----------------")
    #
    # for j in Row_list_GR:
    #     print(in_tsv[j][0])
    #
    # print("-----------------")
    #
    # for j in Row_list_ES:
    #     print\
    #         (in_tsv[j][0])
    # print("-------------DEBUG--------------------------------------")
    temp_row = ["", "", "", "", "", "", "", "", "", "a"]

    def clear_temp_row():
        temp_row = ["", "", "", "", "", "", "", "", "", ""]
        return temp_row


    my_csv = open('processed_data.csv','w')
    writer = csv.writer(my_csv)

    #   Create the titles (foreigner local total
    for i  in range(len(Type)):
        temp_row[i+1] = Type[i]
    # print(temp_row)
    writer.writerow(temp_row)

    temp_row = clear_temp_row()
    temp_row[0] = in_tsv[0][9]
    # print(temp_row)
    writer.writerow(temp_row)

    print("\n-----------------")


    # for i in Column_list_years:
    #     #   Print the year
    #     print(in_tsv[0][i])
    #
    #     print("Greece")
    #     k = 0
    #     for j in Row_list_GR:
    #         # print(in_tsv[j][0], end=" ")
    #         print(Type[k],end=" ")
    #         print(in_tsv[j][i],end =" ")
    #         k = k+1
    #
    #     print("\n")
    #
    #     print("Spain")
    #     k = 0
    #     for j in Row_list_ES:
    #         # print(in_tsv[j][0], end=" ")
    #         print(Type[k], end=" ")
    #         print(in_tsv[j][i], end=" ")
    #
    #     print("\n-----------------")





    # k = 0
    # print("Greece")
    # for i in Row_list_GR:
    #     print(Type[k])
    #     k= k+1
    #     for j in Column_list_years:
    #         print(i,j)



    # for j in a_list:
    #     # print(j)
    #     if (j==11 or j == 12):
    #         print("Foreigners")
    #     if(j==51 or j == 52):
    #         print("Residents")
    #     if (j==91 or j == 92):
    #         print("Total")
    #
    #     for i in range((1 + year_begin - 2008), (year_end + 2 - 2008)):
    #         # print("i is ",i)
    #         num = int(in_tsv[j][i])
    #         print(format(num, ',') , "|",end =" ")
    #     print("\n")


    # years = [2016,2017,2018,2019]
    # print(years)