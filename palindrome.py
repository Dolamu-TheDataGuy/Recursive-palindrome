def isPalindrome(s):
    s = s.lower().replace(' ', '')
    if s == '' or len(s) == 1:
        return True
    else:
        if s[0] != s[-1]:
            return False
        s = s[1:-1]
        return isPalindrome(s)  # note: we might delete s = s[1:-1] and write directly return isPalindrome(s[1:-1])


def main():
    word = input('enter a string: ')
    print('is that a palindrome?')
    if isPalindrome(word):
        print("Yes it's a palindrome")
    else:
        print("No it's not a palindrome")


if __name__ == '__main__':
    main()