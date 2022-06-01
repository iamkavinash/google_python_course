#Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
#newfilenames = [print(f"{x:.1s}")for x in filenames if x.endswith("hpp") ]
newfilenames=[]
for x in filenames:
    if x.endswith("hpp"):
        y = x.replace("hpp","h")
        newfilenames.append(y)
    else:
        newfilenames.append(x)

print(newfilenames) 
print("--------------------------OR------------------------------")
newfilenames = [e.replace('.hpp','.h') for e in filenames]
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]