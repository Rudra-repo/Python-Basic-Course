# BREAK & CONTINUE:

# BREAK : used to terminate the loop when encountered.
# CONTINUE : terminates the execution in the current iteration & contunues execution of the loop with the next iteration.

count = 1
while count <= 100 :
        print(count)
        if(count == 10):
                break
        count += 1 
print("End of loop")

nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
idx = 0
while idx < len(nums):
        if(nums[idx] == x):
                print("Found at idx", idx)
                break
        else:
                print("finding...")
        idx += 1
print("End of Loop")

i = 0
while i <= 5:
        if(i == 3):
                i += 1
                continue     # skip
        print(i)
        i += 1
print("End of code")

i = 1
while i <= 10:
        if(i%2 != 0):
                i += 1
                continue
        print(i)
        i +=1
        
print("End of code")

for i in range(100):
        if(i == 34):
                break
        print(i)