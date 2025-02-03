# Using regular expressions
import re

pattern = r'\d{3}-\d{2}-\d{4}'  # SSN format
text = "My number is 123-45-6789."
match = re.search(pattern, text)
if match:
    print("Found SSN:", match.group())