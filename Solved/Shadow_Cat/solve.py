#!/usr/bin/env python3

results = '''
jr:1:17792:0:99999:7:::
z:_:17930:0:99999:7:::
a:a:17930:0:99999:7:::
x:b:17930:0:99999:7:::
q:c:17930:0:99999:7:::
l:w:17930:0:99999:7:::
v:h:17930:0:99999:7:::
e:i:17930:0:99999:7:::
f:j:17930:0:99999:7:::
b:k:17930:0:99999:7:::
r:l:17930:0:99999:7:::
g:m:17930:0:99999:7:::
n:n:17930:0:99999:7:::
o:x:17930:0:99999:7:::
p:y:17930:0:99999:7:::
s:d:17930:0:99999:7:::
c:e:17930:0:99999:7:::
w:f:17930:0:99999:7:::
d:g:17930:0:99999:7:::
t:o:17930:0:99999:7:::
h:p:17930:0:99999:7:::
m:q:17930:0:99999:7:::
k:u:17930:0:99999:7:::
i:v:17930:0:99999:7:::
y:r:17930:0:99999:7:::
j:s:17930:0:99999:7:::
u:t:17930:0:99999:7:::
underscore:z:17930:0:99999:7:::
'''.strip()
results = results.replace('underscore', '_')

# create replacement table
replacements = list(map(lambda x: (x.split(':')[0], x.split(':')[1]), results.splitlines()))
print('replacements', replacements)

'''
# debugging values
replacements0 =  list(map(lambda x: x[0], replacements))
replacements1 =  list(map(lambda x: x[1], replacements))
print('replacements[0]', sorted(replacements0))
print('replacements[1]', sorted(replacements1))
print('length', len(replacements1))
'''

# do replacement
orig = 'hajjzvajvzqyaqbendzvajvqauzarlapjzrkybjzenzuvczjvastlj'
final = ''
for ch in orig:
    for before, after in replacements:
        # Catch 
        if before == ch:
            ch = ch.replace(before, after)
            break
    final += ch

# print flag
print(final)
print(f"VolgaCTF{{{final}}}")