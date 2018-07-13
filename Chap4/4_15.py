def editDistance(str1,str2,m,n):

    #base cases
    #if first string is empty, insert all characters of the second string
    if m==0:
        return 20*n

    # if the second string is empty, delete all characters of the first string
    if n==0:
        return 20*m

    # if last characters of the two strings are the same,  compute cost on remaining characters
    if str1[m-1]==str2[n-1]:
        return editDistance(str1,str2,m-1,n-1)

    #if none of the above
    return min( 20 + editDistance(str1,str2,m,n-1), # insert
                20 + editDistance(str1,str2,m-1,n) ,# delete
                5 + editDistance(str1,str2,m-1,n-1) # copy
                )


str1 = "algorithm"
str2 = "alligator"
print(editDistance(str1, str2, len(str1), len(str2)))
