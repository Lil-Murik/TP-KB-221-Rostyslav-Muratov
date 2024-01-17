str1 = "     hello World     "
strip = str1.strip()
print(f"Original: '{str1}'")
print(f"Strip: '{strip}'\n")

str2 = "hello world"
capitalized = str2.capitalize()
print(f"Original: '{str2}'")
print(f"Capitalized: '{capitalized}'\n")

str3 = "Hello World Hello World HELLO WORLD"
upper = str3.upper()
lower = str3.lower()
print(f"Original: '{str3}'")
print(f"Upper: '{upper}'")
print(f"Lower: '{lower}'\n")

str4 = "hello word HEllo world"
title = str4.title()
print(f"Original: '{str4}'")
print(f"Title: '{title}'\n")

str5 = "hello wORLD HEllo wORLD"
swapcase = str5.swapcase()
print(f"Original: '{str5}'")
print(f"Swapcase: '{swapcase}'\n")

str6 = "Hello beautiful girl"
replace = str6.replace("girl", "world")
print(f"Original: '{str6}'")
print(f"Replace: '{replace}'")
