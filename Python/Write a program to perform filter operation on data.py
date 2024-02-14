#Write a program to perform filter operation on data
import pandas as pd

data = [ 
(1, 'Anmol', 18, 'male' ),
(3, 'Aryan', 19, 'male'),
(7, 'Sneha', 18, 'female'),
(11, 'Ayushi', 17, 'female'),
(20, 'Ritu', 19, 'female'),
(25, 'Vatsal', 17, 'male')
]

df = pd.DataFrame(data, columns=['rollno', 'name', 'age', 'gender'])

#Perform some filter operations

# 1. Display first four rows
print(df.head(4));

# 2. Display last three rows
print(df.tail(3))

# 3. Display only roll no and age columns jointly
print(df[['rollno','age']])

# 4. Display only name and age columns jointly
print(df[['name','age']])

# 5. Display the type of data
print(df.dtypes)

# 6. Display second and fourth row
print(df.loc[[1,3]])

# 7. Display all the rows where age less than 19
print(df[df['age']<19])

# 8. Add new column 'branch' and assign 'Bsc' to each row of this column
df['branch']='Bsc'
print(df)


# 9. Remove rollno column from data
del df['rollno']
print(df)

# 10. Add roll column again
df['roll']=[2,4,6,8,10,12]
print(df)

# 11. Rename roll column to rollno
df.rename(columns = {'rollno':'roll'}, inplace = True)
print(df)

# 12. Delete 4th row from data

print(df.drop(3))

# 13. Add row with data
print(df)


# 14. Change data for rollno for 1st and 4th row to 21 and 22
df.loc[[1,3], 'rollno']=[21,22]
print(df)
