#! /usr/bin/python3
#1
my_file=open("data.csv")
for eachline in my_file :
	fields=eachline.rstrip().split(",")
	if fields[0] == "Drosophila melanogaster" or fields[0] == "Drosophila simulans" :
		print(fields[2])

#2
my_file=open("data.csv")
for eachline in my_file :
        fields=eachline.rstrip().split(",")
	if len(fields[1]) >=90 and len(fields[1]) <=110 :
		print(fields[2])

#3
my_file=open("data.csv")
for eachline in my_file :
	fields=eachline.rstrip().split(",")
	if  (fields[1].count("a") + fields[1].count("t"))/len(fields[1]) <0.5 and int(fields[3]) >200 :
		print(fields[2])


#4
my_file=open("data.csv")
for eachline in my_file :
        fields=eachline.rstrip().split(",")
	if fields[0] != "Drosophila melanogaster" and (fields[2].startswith("k") or fields[2].startswith("h")) :
		print(fields[2])


#5
my_file=open("data.csv")
for eachline in my_file :
        fields=eachline.rstrip().split(",")
	if (fields[1].count("a") + fields[1].count("t"))/len(fields[1]) > 0.65 :
		print(fields[2], "AT content is high")
	elif (fields[1].count("a") + fields[1].count("t"))/len(fields[1])>= 0.45 :
		print(fields[2], "AT content is medium")
	else :
		print(fields[2], "AT content is low")
