# import regular expressions
import re

patterns = ['term1','term2']

text = 'This is a string with term1, not the other'

# for pattern in patterns:
#     print("I'm seraching for: " + pattern)

#     if re.search(pattern,text):
#         print("match")

#     else:
#         print("no match")

match = re.search('term1',text)
print(match.start())

split_term = '@'

email = 'user@gmail.com'

print(re.split(split_term,email))

print(re.findall('match','test phrase match match match in middle'))


def multi_re_find(patterns,phrase):
    for pat in patterns:
        print(f"Searching for pattern {pat}")
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns = ['sd*']

multi_re_find(test_patterns,test_phrase)