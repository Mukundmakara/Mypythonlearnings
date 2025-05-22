try:
   file_read = open("sample.txt",'r')
   print(file_read.read())
except FileNotFoundError:
   print("File not found")
finally:
      #     file_read.close()
  print("open and read operation on the file went fine")

