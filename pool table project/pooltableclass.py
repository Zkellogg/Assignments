from os import write
from datetime import datetime


tables_array = []

write_file_array = []


class PoolTable:
    def __init__(self, id, taken, time_out, time_in):
        self.id = id
        self.taken = taken
        self.time_out = time_out
        self.time_in = time_in

for i in range(1, 13):
    id = 'pool_table_{}'.format(i)
    taken = False
    time_out = 0
    time_in = 0
    tables_array.append(PoolTable(id, taken, time_out, time_in))


def pool_table_function():
    for table in tables_array:
        print("--------------------------------------------------------------")
        print(f"This is {table.id}")
        print("\n")
        print(f"Is Occupied? {table.taken}")
        print("\n")
        # print(f"Table has been in use for x min.")
        # print("\n")
        print("--------------------------------------------------------------")

def pool_table_1():
    

    check = input("""
    Press 1 to check-out the table.
    -------------------------------
    Press 2 to check-in the table. > """)

    print("\n")

    if check == "1":
        if tables_array[0].taken == True:
            print("This big boy already checked out!..")
        else:
            tables_array[0].taken = True
            tables_array[0].time_out = datetime.now()
            print(f"Pool table checked out at {tables_array[0].time_out}")
            print("\n")
            input("Press any key to continue > ")
            pool_table_function()
                    
    if check == "2":
        tables_array[0].taken = False
        tables_array[0].time_in = datetime.now()
        time_used = tables_array[0].time_in - tables_array[0].time_out
        time_spent = time_used.total_seconds() / 60
        write_dict = {"table": tables_array[0].id, "time used": time_spent}
        write_file_array.append(write_dict)
        
        print(f"Pool Table 1 is checked in, it was out for {time_used}. ")
        print("\n")
        input("Press any key to continue > ")
        return write_file_array

def pool_table_2():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[1].taken = True
        print("Pool Table 2 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[1].taken = False
        print("Pool Table 2 is checked in")
        pool_table_function()

def pool_table_3():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[2].taken = True
        print("Pool Table 3 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[2].taken = False
        print("Pool Table 3 is checked in")
        pool_table_function()

def pool_table_4():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[3].taken = True
        print("Pool Table 4 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[3].taken = False
        print("Pool Table 4 is checked in")
        pool_table_function()

def pool_table_5():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[4].taken = True
        print("Pool Table 5 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[4].taken = False
        print("Pool Table 5 is checked in")
        pool_table_function()  

def pool_table_6():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[5].taken = True
        print("Pool Table 6 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[5].taken = False
        print("Pool Table 6 is checked in")
        pool_table_function()  

def pool_table_7():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[6].taken = True
        print("Pool Table 7 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[6].taken = False
        print("Pool Table 7 is checked in")
        pool_table_function()
    
def pool_table_8():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[7].taken = True
        print("Pool Table 8 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[7].taken = False
        print("Pool Table 8 is checked in")
        pool_table_function()

def pool_table_9():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[8].taken = True
        print("Pool Table 9 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[8].taken = False
        print("Pool Table 9 is checked in")
        pool_table_function()

def pool_table_10():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[9].taken = True
        print("Pool Table 10 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[9].taken = False
        print("Pool Table 10 is checked in")
        pool_table_function()

def pool_table_11():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[10].taken = True
        print("Pool Table 11 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[10].taken = False
        print("Pool Table 11 is checked in")
        pool_table_function()

def pool_table_12():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[11].taken = True
        print("Pool Table 12 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[11].taken = False
        print("Pool Table 12 is checked in")
        pool_table_function()

# with open("PoolTable.txt", "a") as file:
#     write.file()




    
    
    


