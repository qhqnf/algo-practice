import re


def is_palindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub("[^a-z0-9]", "", s)

    return s == s[::-1]


if __name__ == "__main__":
    string = "A man, a plan, a canal: Panama"
    print(is_palindrome(string))

