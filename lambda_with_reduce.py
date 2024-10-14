import functools as ft
l = [23,42,64,55,90,12]
lo = ft.reduce(lambda x,y:x+y,l)
print(lo)