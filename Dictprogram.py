Name1 = input("Enter a Name of a student: ")
dic_items = {"RAM":"90","Shyam":"95","KAAM":"98","TAAM":"99","HARE":"100"}
if Name1 in dic_items:
 print("{} has obtained {} marks in english literature".format(Name1, dic_items[Name1]))
else:
 print("Name not in dictionary")