print('测测你能不能读懂我的心')
from random import randint
n=randint(1,100)
print('测测你能不能读懂我的心')
i=0
while True:
    num=int(input('输入你认为的数字 1-100:'))
i+=1
if(num>n):
  print('错误，你还是不了解我')
elif(num<n):
  print('错误，你伤透了我的心')
else:
  print('漂亮！你这么懂我，你是我的了！')

