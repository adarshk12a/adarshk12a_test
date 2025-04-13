#1. Reverse a Integer (2 differnt ways)
def reverse_number(x: int):
    ##print(x)
    y=str(x)[::-1]
    return y

print(reverse_number(123))

number = 12345
reverse = 0
while number > 0:
  last_digit = number % 10
  reverse = reverse * 10 + last_digit
  number = number // 10

print(reverse)

#2 Merger strings alternatively
def mergeAlternately(word1: str, word2: str):
    maxLength= max(len(word1), len(word2))
    print(maxLength)
    i = 0;
    output=''
    while i<= (maxLength-1):
        if (i<= (len(word1)-1)):
            output += word1[i]
        if (i<= (len(word2)-1)):
            output += word2[i]
        i= i+1
    print(output)
mergeAlternately('12345678','abcde')
