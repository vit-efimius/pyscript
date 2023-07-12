import re

text = """
Here is an example string containing various numbers, some 
of which are not phone numbers.

Business Address
4553-A First Street
Washington, DC 20001

202-555-6473
301-555-8118
"""

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?                 # area code
	(\s|-|\.)?                         # separator
	(\d{3})                            # first 3 digits
	(\s|-|\.)                          # separator
	(\d{4})                            # last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?     # extension
	)''', re.VERBOSE)

matches = []

for numbers in phoneRegex.findall(text):
	matches.append(numbers[0])

print(matches)