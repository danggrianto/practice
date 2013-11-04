"""Reverse string

Reverse given input from user.
"""
if __name__ == '__main__':
    text = raw_input('enter string : ')
    list = [c for c in text]
    list.reverse()
    print(''.join(list))
