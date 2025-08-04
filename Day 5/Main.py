heights = input("What is the height of each student? ").split( )

for n in range(0,len(heights)):
    heights[n] = int(heights[n])

total_heights = 0

for n in range(0,len(heights)):
    total_heights+=heights[n]
print(f"Total heights of students are: {total_heights}")
total_students = 0

for n in range(0,len(heights)):
    total_students += n - (n-1)
print(f"Total students are:{total_students}")

print(f"Average height of a student is {round((total_heights / total_students),2)}")
