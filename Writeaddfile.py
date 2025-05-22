file_feed = input("Enter text to write to the file:")
try:
    file_write = open("output.txt","w")
    file_write.write(file_feed)
    file_write.close()
    file_feed1 = input("Add the additional data to append to the file:")
    file_write = open("output.txt","a")
    file_write.write(file_feed1)
    file_write.close()
except FileNotFoundError:
    print("File not found")

finally:
 print(file_feed + file_feed1)





