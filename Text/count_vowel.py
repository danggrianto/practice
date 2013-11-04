def count_vowel(word):
    vowels = 'aeiou'
    count = 0
    for c in word:
        if c in vowels:
            count += 1
    return count

if __name__ == '__main__':
    word = raw_input('enter word : ')
    print 'number of vowel is %s' % count_vowel(word)
