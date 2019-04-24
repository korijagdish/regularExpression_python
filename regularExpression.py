import re
str='  vibrant gujarat 2019 will head in Ahmedabad'
res=re.sub('Ahmedabad','gandhinagar',str)
print(res)
str='vibrant gujarat 2019 will head in Ahmedabad'
res1=re.subn('ahmedabad','Aandhinagar',str)
print(res1)
res2=re.subn('ahmedabad','Aandhinagar',str,re.u)
print(res2)
