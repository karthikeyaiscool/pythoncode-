# program to find HCF/GCD

# enter 2 numbers
numberLargest = int(input("enter Largest number  :"))  
numberSmallest = int(input("enter Smallest number  :"))

# useing Eucliden Algorithms
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is : ",numberLargest )