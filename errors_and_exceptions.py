
try:
    # f = open('simple.txt','w')
    f = open('simple.txt','r')
    f.write("Test write to simple text")

except:
    print("Error: Could not find file or read data")

# else:
#     print("Success")
#     f.close()

finally:
    print("I always work!")
