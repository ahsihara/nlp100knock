data1 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine New Nations Might ' \
        'Also Sign Peace Security Clause Arthur King Can'
data2 = data1.split()
ans = {}
number = [1,5,6,7,8,9,15,16,19]
for i in range(len(data2)):
    if i+1 in number:
        ans.update({data2[i][0]:i+1})
    else:
        ans.update({data2[i][:2]:i+1})
print(ans)
