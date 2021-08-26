# WORKING ON SMALL OUTPUT FOR CREATING NEW OUTPUT
def subsequences(s, soFar = ""):
    if len(s) == 0: 
        print(soFar)
        return

    subsequences(s[1:],soFar+s[0])
    subsequences(s[1:],soFar)



s = "abc"
ans = subsequences(s)