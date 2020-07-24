'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    sub = 'th'
    # Base Case
    if len(word) == 0 or len(word) < len(sub):
        return 0
    
    # Recursive Case
    if word[0:len(sub)] == sub:
        return 1 + count_th(word[len(sub)-1:])
    else:
        return count_th(word[len(sub)-1:])


