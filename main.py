vowels_str = "aeiouAEIOU"
given_str = input("Enter a string : ")
final_str = given_str
for c in given_str:
    if c in vowels_str:
        final_str = final_str.replace(c, '')

print(final_str)
