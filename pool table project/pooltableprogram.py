from pooltableclass import *
import json

pool_table_function()

while True:
    

    table_choice = input("Please type the table # you would like to edit or press q to quit program. > ")

    if table_choice == "q":
        # confirm_choice = input("Type YES to quit: All pool tables will be rest. > ")
        # if confirm_choice = "YES":
        break

    if table_choice == "1":
        write_file_array = pool_table_1()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)

    if table_choice =="2":
        write_file_array = pool_table_2()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)
        
    if table_choice =="3":
        write_file_array = pool_table_3()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)

    if table_choice =="4":
        write_file_array = pool_table_4()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)

    if table_choice =="5":
        write_file_array = pool_table_5()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)

    if table_choice =="6":
        write_file_array = pool_table_6()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)

    if table_choice =="7":
        write_file_array = pool_table_7()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)

    if table_choice =="8":
        write_file_array = pool_table_8()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)

    if table_choice =="9":
        write_file_array = pool_table_9()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)

    if table_choice =="10":
        write_file_array = pool_table_10()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)

    if table_choice =="11":
        write_file_array = pool_table_11()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)

    if table_choice =="12":
        write_file_array = pool_table_12()
        with open("07-14-2021.json", "w") as file:
            json.dump(write_file_array, file)


    




