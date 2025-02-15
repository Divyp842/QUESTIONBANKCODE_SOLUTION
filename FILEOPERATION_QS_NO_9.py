def fileoperation(file1,file2,file3):
 with open('file1', 'r') as file1, open('file2', 'r') as file2, open('file3', 'w') as file3:
    
    for line in file1:
        file3.write(line)
      
    for line in file2:
        file3.write(line)

fileoperation("file1.txt","file2.txt","file3.txt")
print("Lines from file1 and file2 have been written to file3.")

