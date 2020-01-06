#Jack Miller
#lab 1

userInput = input("Enter file name: ")
File = open(userInput,"r")
count=0
read = File.readline()
while(read!=""):
   count+=1
   read = File.readline()
print("Number of lines =", count)


File.close()