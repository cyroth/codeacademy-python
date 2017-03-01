pyg = 'ay'

original = raw_input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
#contatenacte there
    new_word = word + first + pyg
#remove the first letter
    new_word = new_word[1:len(new_word)]
    print "the translated word is: %s" % (new_word)
else:
    print 'empty'
