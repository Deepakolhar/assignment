
  
# main code 
k=int(input("Enter the Number of Employees:"))
f = open("output.txt","a")
with open('input.txt','r') as file: #open input file in read mode to retrive the input
    string = file.read() 
array = list(string.split("\n")) # spliting the newline character of the input data
#print(array)
arr=[]
dict={}
for eve in array:
    (key,val)=eve.split(": ")
    dict[int(val)] = key
    arr.append(int(val))  
#print(namearray)
#print(valuearray)
#print(dict)
n =len(arr)

startIndex=0
endIndex=0
result = +2147483647  
# Sorting the array. 
arr.sort() 
#print(arr)
# Find minimum value among 
# all K size subarray. 

for i in range(n-k+1):
    oldValue = result
    result = int(min(result, arr[i+k-1] - arr[i]))
    if(oldValue != result): 
        startIndex = i
        endIndex = i+k-1
       # print(result,i,i+k-1)
    #print("Start Index: "+str(startIndex)+" End Index: "+str(startIndex+k-1))
    """for j in range(startIndex,endIndex+1):
        print(arr[j])"""

disparr=[]
for i in range(startIndex,endIndex+1):
    disparr.append(arr[i])
#print(disparr)
f.write("\nThe goodies selected for distribution are:\n\n\n")
for i in range(len(disparr)):
    outputString = str(dict[disparr[i]]+": "+str(disparr[i])+"\n")
    f.write("\n"+outputString)
extra = str("\n\n\nAnd the difference between the chosen goodie with highest price and the lowest price is: "+str(result)+"\n")
f.write(extra)
f.close()
