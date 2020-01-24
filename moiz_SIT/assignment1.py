import csv

reader = csv.reader(open('data/athlete_events.csv', 'r'), delimiter=",")
writer = open('data/writed_athlete.events.csv','w')
writer.write("Name,Sex,Age,Height,Weight,Team,NOC,Year,Season,City,Sport,Event,Medal\n")

for row in reader:
    if row[5]=="Thailand" and row[12]!="NA":
       
        print(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6]+','+row[7]+','+row[8]+','+row[9]+','+row[10]+','+row[11]+','+row[12]+"\n")
        writer.write(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6]+','+row[7]+','+row[8]+','+row[9]+','+row[10]+','+row[11]+','+row[12]+"\n")


writer.close()






#         print("{")
#         print("Name: "+row[0]+",\nSex: "+row[1]+",\nAge: "+row[2]+",\nTeam: "+row[5]+",\nSport: "+row[10]+",\nMedal: "+row[12])
#         print("},")
# print("] }")

