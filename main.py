# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])
# print(len(s))

# s = input()
# print(s.count(' ') +1)
# k = len(s)//2
# print(k)
# print(s[4:]+s[:4])

# s = input()
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >= 2:
#     print(s.find('f'), s.rfind('f'))

# s = 'fgkjjlkjjljlhfhg'
# a = s.find('h')
# print(a)
# b = s.rfind('h')
# print(b)
# print(s[:a] + s[b+1:])

# a = int(input('first '))
# b = int(input('second '))
# if a>b:
#     print(b)
# else:
#     print(a)

# x = int(input(' '))
# if x>0:
#     print('sign(x)=1')
# elif x<0:
#     print('sign(x)=-1')
# else:
#     print('sign(x)=0')

# x1 = int(input(' '))
# y1 = int(input(' '))
# x2 = int(input(' '))
# y2 = int(input(' '))
# if 1<=x1<=8 and 1<y1<=8 and 1<=x2<=8 and 1<=y2<=8:
#     if (x1+y1)%2==0 and (x2+y2)%2==0:
#         print('yes')
#     else:
#         print('no')
# else:
#     print('EROR')

# Year = int(input())
# if Year%2==0 and Year%100!=0 or Year%400==0:
#     print('yes')
# else:
#     print('No')

x1 = int(input())
x2 = int(input())
x3 = int(input())
if x1==x2==x3:
    print(3)
elif x1==x2 or x1==x3 or x2==x3:
    print('2')
else:
    print('0')

