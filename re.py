import re
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+     # username
	@                     # @ symbol
	[a-zA-Z0-9.-]+        # domain name
	(\.[a-zA-Z]{2,4})     # dot-something
  )''', re.VERBOSE)

matches = []
text = """
An example text containing an email address, such as user@example.com or something like hello@example.com
"""

for groups in emailRegex.findall(text):
	matches.append(groups[0])

print(matches)