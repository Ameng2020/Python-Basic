import math

def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type')
    if b**2-4*a*c<=0:
        print("输入不合法（b**2-4*a*c<=0）")
    else:
        x1 = (-b+math.sqrt(b**2-4*a*c<=0))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c<=0))/(2*a)
        if x1 == x2:
            return '%.2f'% x1
        else:
            return '%.2f'% x1,'%.2f'% x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')          
