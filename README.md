# Python program

#### This program performs the following actions:

+ Downloads a ".tsv" dataset from eurostat
+ Cleans up the data so only specific data is kept: 
	+ Years : 2016, 2017, 2018, 2019
	+ Countries: Greece, Spain
	+ Type of visitor: Foreigners and Total number of visitors
	
+ Stores the data into a csv file
+ Stores the cleaned Data into a MySQL Database
+ Creates charts using the data, using the MatPlotLib python module