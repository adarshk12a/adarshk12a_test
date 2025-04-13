def reverseWords(s: str):
    li= list(s.split(" "))
    print(li)
    rever= li[::-1]
    print(rever)
    output = " ".join(rever)
    print(output)

reverseWords("my name is adarsh")