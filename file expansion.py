import os
mydict={"py":"Python","html":"HTML","c":"C","jpg":"Image file"}
filename=(input("Enter the filename:"))
extension=filename.split(".")[-1]
print("the extension",extension)
if(extension=="py"):
   print(mydict["py"])
elif (extension=="html"):
    print(mydict["html"])
elif(extension=="c"):
  print(mydict["c"])
else:
    print(mydict["jpg"])
