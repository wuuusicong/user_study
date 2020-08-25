

import re
text = "Which cluster has the largest portion overlapped by the Green cluster, Orange or Red?"

pattern = re.compile(r'\w*\sor\s\w*')

result = pattern.findall(text)[0]
result =result.replace(" ","").split("or")
result = [x.lower() for x in result]
print(result)