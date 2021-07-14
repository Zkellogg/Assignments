from os import write


tables_array = []

class PoolTable:
    def __init__(self, id, taken, time_used):
        self.id = id
        self.taken = taken
        self.time_used = time_used

for i in range(1, 13):
    id = 'pool_table_{}'.format(i)
    taken = False
    time_used = 0
    tables_array.append(PoolTable(id, taken, time_used))


def pool_table_function():
    for table in tables_array:
        print("--------------------------------------------------------------")
        print(f"This is {table.id}")
        print("\n")
        print(f"Is Occupied? {table.taken}")
        print("\n")
        print(f"Table has been in use for {table.time_used} min.")
        print("\n")
        print("--------------------------------------------------------------")

def pool_table_1():
    

    check = input("""
    Press 1 to check-out the table.
    Press 2 to check-in the table. > """)

    if check == "1":
        tables_array[0].taken = True
        print("Pool Table 1 is checked out")
        pool_table_function()
                    
    if check == "2":
        tables_array[0].taken = False
        print("Pool Table 1 is checked in")
        pool_table_function()

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

with open("PoolTable.txt", "a") as file:
    write.file()




    
    
    


