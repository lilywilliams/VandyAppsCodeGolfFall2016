def a(n):
    return str(n)==str(n)[::-1]
def b(n):
    return all(n%i for i in range(2,n))
y=input("y:")
p=[i for i in range(y) if (a(i) and b(i))]
print(p)
