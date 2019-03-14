import re

m = re.match(r".*BC?$", "helloB").span()
print(m)
