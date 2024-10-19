# from pandas import *
#
# mydataframe=DataFrame({"proid":range(1,5),"proname":['soap','perfume','deo','powder']})
# print(mydataframe)
# mylist=mydataframe.loc[(mydataframe.proname=='perfume')].values.tolist()
# print(mylist)
# mylist=mydataframe.loc[(mydataframe.proname!='soap') & (mydataframe.proname!='powder')].values.tolist()
# print(mylist)
# mylist=mydataframe.iloc[:3].values.tolist();
# print(mylist)
#
# # from pandas import *
# #
# # mydata=DataFrame([100,101,102,103,104],index=['a','b','c','d','e'])
# # print(mydata)
# # print(mydata.loc['a':'c']) # rows from a to c # exceptional case(loc) where column print from a to c not from a to b
# # print(mydata.loc[['b','e']]) # rows b and e
# # print(mydata.iloc[0:3])
#
# #----------------------------------------------------------------------------------
# # DataFrame built-in functions
# # copy "Book1.csv" file inside pycharm project folder
#
# # e.g. copy "Book1.csv" file inside
# # "C:\Users\Nitin\PycharmProjects\pythonProject" folder.
# # Here "pythonProject" is assumed to be the name of the
# # project which we have created.
#
# from pandas import *
#
# book=read_csv("Book1.csv")
# # print(book)
# # print("type of book is\t",type(book))
# # print("\n")
# # print("Let's print first 5 records")
# # print(book.head()) # by default 0 to 5 , 5 is exclusive
# # print("\n")
# # print("let's print first 3 records")
# # print(book.head(3)) # 0 to 3 , 3 is exclusive
# # print("\n")
# # print("print all the records except last 3 records")
# # print(book.head(-3))   #  print all the records except last 3 records
# # # # 0 to -4
# # print("Let's print last 5 records")
# # print(book.tail())  #  [-5:]
# # print("let's print last 2 records")
# # print("\n")
# # print(book.tail(2))  # [-2:]
# # print("\n")
# # print("print all the records except first 3 records")
# # # #[-(-3):]
# # print(book.tail(-3))  #  print all the records except first 3 records
# # print("Total no. of rows and columns in the file")
# # print(book.shape)
# # print("\n")
# # print(book.describe()) #describe is a function and shape is a property
# # print("\n")
# # print("Let's extract first 3 records with 2 columns only")
# # print(book.iloc[:3,:2])
# # print("\n")
# # print(book.loc[0:4,('name','address')])   #  Access a group of rows and columns by label(s) , 4 is inclusive here
# # print("Let's drop a particular column")
# # print(book.drop("age",axis=1))  # here axis=1  means we want to drop the column
# # print("Let's drop some rows")
# # print(book.drop([3,4,5,6],axis=0))      # here axis=0  means we want to drop rows
# # print("let's drop name column and 1,3 ,7 rows")
# # print(book.drop(("name"),axis='columns').drop([1,3,7],axis='rows'))
# #
# # # instead of 1 and 0 you can mention 'columns' and 'rows' respectively
# #
# # # Columns can be dropped at the time of reading itself.
# #
# # print("\n")
# # cancel =['address','age']
# # book1=read_csv("Book1.csv").drop(cancel,axis='columns')
# # print(book1)
#
# # cancel =['address','age']
# # book1=read_csv("Book1.csv").drop([0,1,2,3,4,5],axis='rows')
# # print(book1)

#-----------------------------------------------------------------------------------------------------------------------
# from pandas import *
# iris=read_csv("iris.csv")
# print(iris)

# import pandas as pd
#
# proid = [1, 2, 3, 4]
# proname = ["Soap", "Perfume", "Deo", "Body_Wash"]
# price = [120, 400, 250, 180]
#
# # dictionary of lists
# mydictionary = {'proid': proid, 'proname': proname, 'price': price}
#
# mydataframe = pd.DataFrame(mydictionary)
#
# print(mydataframe)
# mydataframe.to_csv("prod.csv")
# mydataframe.to_json("prod.json")


# install openpyxl

# import pandas as pd
#
# proid = [1, 2, 3, 4]
# proname = ["Soap", "Perfume", "Deo", "Body_Wash"]
# price = [120, 400, 250, 180]
#
# # dictionary of lists
# mydictionary = {'proid': proid, 'proname': proname, 'price': price}
#
# mydataframe = pd.DataFrame(mydictionary)
#
# print(mydataframe)
# # index=False   is not to include dataframe index inside the excel file
# mydataframe.to_excel("prod.xlsx", sheet_name="prod_sheet", index=False)

# install openpyxl

# The ExcelWriter object allows you to use multiple pandas. DataFrame objects can be exported to separate sheets.
#--------------------------------------------------------------------------------------------------------
# import pandas as pd
#
# proid = [1, 2, 3, 4]
# proname = ["Soap", "Perfume", "Deo", "Body_Wash"]
# price = [120, 400, 250, 180]
#
# # dictionary of lists
# mydictionary1 = {'proid': proid, 'proname': proname, 'price': price}
#
# mydataframe1 = pd.DataFrame(mydictionary1)
#
# name = ['Abc', 'Xyz', 'Pqr']
# designation = ['officer', 'manager', 'salesexecutive']
# salary = [40000, 60000, 70000]
#
# mydictionary2 = {'name': name, 'designation': designation, 'salary': salary}
#
# mydataframe2 = pd.DataFrame(mydictionary2)
#
# print(mydataframe1)
# print("\n\n")
# print(mydataframe2)
#
# mydataframe1.to_excel("prod2.xlsx", sheet_name="prod_sheet", index=False)
# input()
# mydataframe2.to_excel("prod2.xlsx", sheet_name="employee_sheet", index=False)  # this will overwrite previous sheet
#--------------------------------------------------------------------------------------------------
 # Series object is a one-dimensional labelled or indexed  array

# import pandas as pd
#
# first=pd.Series([100,20,3,40,5])
# print(first)
# print("sorting Pandas values without indexes changed")
# print(first.sort_values())
# print("sorting Pandas values with indexes changed")
# print(first.sort_values(ignore_index=True))
# print("sorting in descending order ,Pandas values with indexes changed")
# print(first.sort_values(ascending=False,ignore_index=True))


# import pandas as pd
#
# # Creating Dataframe
# students_data = pd.DataFrame({
#     'Prn_No': [101, 102, 103, 104, 105,
#            106, 107, 108, 109, 110],
#     'NAME': ['Jagruti', 'Pavan', 'Harish',
#              'Pooja', 'Rahul', 'Niharika',
#              'Sachin', 'Atul', 'Dean', "Manish"],
#     'course': ['DAC', 'DBDA', 'DBDA', 'DBDA', 'DBDA',
#                'DAC', 'DAC', 'DAC', 'DBDA', 'DBDA']})
#
# # Creating Dataframe
# placement_details = pd.DataFrame(
#     {'Prn_No': [101, 102, 103, 104, 105,
#             106, 107, 108, 109, 110],
#      'status': ['placed', 'not_placed', 'placed',
#                  'placed', 'not_placed', 'not_placed',
#                  'placed', 'not_placed', 'placed', 'placed']})
# #
# # # Merging Dataframe
# # print(pd.merge(students_data, placement_details, on='Prn_No'))
#
# # vargs=lambda x,y=20 : print(f"{x},{y}")
# # vargs(10)
#
# print(students_data)
#
# students_data = students_data.rename(columns={'project_marks': 'Project_grade'})
# print(students_data)
# grade=""
# for marks in students_data["Project_grade"]:
#     if marks>=90:
#         grade='A'
#     elif marks>70 and marks<90:
#         grade='B'
#     else:
#         grade='C'
#     students_data["Project_grade"]=students_data["Project_grade"].replace({marks:grade})
#
# print(students_data)
#-------------------------------
import pandas as pd
import re

proid = [1, 2, 3, 4]
proname = ["Soap", "Perfume", "Deo", "Body_Wash"]
price = [120, 400, 250, 180]

# dictionary of lists
mydictionary1 = {'proid': proid, 'proname': proname, 'price': price}
#
mydataframe1 = pd.DataFrame(mydictionary1)
# print(mydataframe1)
# print("without index ************************")
# print(mydataframe1.to_string(index=False))
#
# print("\nproducts where price more than 200\n")
# print(mydataframe1[mydataframe1.price > 200].to_string(index=False))

# print("\nproducts where price is between 200 and 300\n")
# print(mydataframe1[(mydataframe1.price >= 200) & (mydataframe1.price <= 300)].to_string(index=False))

# print("\nproducts where name is neither Soap nor Deo\n")
# pronames = ['Soap', 'Deo']
# print(mydataframe1[~mydataframe1.proname.isin(pronames)].to_string(index=False))  # case sensitive

# print("\nproducts which contains e \n")
# print(mydataframe1[mydataframe1.proname.str.contains('e')])

def print_sum(*args):
    total = sum(args)  # Sum all the arguments
    print("The sum is:", total)

# Example usage
a=int(input())
b=int(input())
c=int(input())
print_sum(a, b, c)          # Output: The sum is: 6
# print_sum(10, 20, 30, 40)   # Output: The sum is: 100
# print_sum(5, 5, 5, 5, 5)    # Output: The sum is: 25
