'''
abs(-3) = 3
abs(3+4j) = 5

chr(65) = 'A'
ord('A') = 65

compile(source, filename, mode) 함수
with open('mymodule.py')as f:
    lines = f.read()
    
code_obj = compile(lines, 'mymodule.py', 'exec')
exec(code_obj)
'''
