#Createdata.py - 1.05 02/09/2019
#program developed to create index number for a .xls migration file for SAP PM
#The index refers to the number of the task in a task list for maintenance

def part1():
    for i in range(10, int(r), 10):

        for x in range(1, 6):

            print('00' + str(i))

def part2():    
    for i in range(100, int(y), 10):

        for x in range(1, 6):
        
            print('0' + str(i))

def part3():   
    for i in range(1000, int(z), 10):

        for x in range(1, 6):
        
            print(str(i))

print('inform where the data creation should stop:')

limit = input()

limit = int(limit) + 10

if int(limit) < 100:

    r = limit

    part1()


elif int(limit) >= 100 and int(limit) <= 1000:

    r = 100
    y = limit

    part1()
    part2()

elif int(limit) > 1000:

    r = 100
    y = 1000
    z = limit

    part1()
    part2()
    part3()

    


    


    
        
