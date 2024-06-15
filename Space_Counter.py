#You have been given the task of making the content on social media platform more user-friendly. Yourtask is to find and return an 
#integer valuerepresenting the count of the number of spaces in a givenstring S
def count_spaces(S):
    count = 0
    for char in S:
        if char == " ":
            count += 1
    return count
S="Hello hey you idiot"
print(count)
