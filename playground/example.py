class stylize: 
    def __init__(self, order, **kwargs) -> None:
        
        pass

string = '\
Lorem ipsum dolor sit amet,\n\
consectetur adipiscing elit, sed do\n\
eiusmod tempor incididunt ut labore\n\
et dolore magna aliqua. Ut enim ad\n\
minim veniam, quis nostrud exercitation\n\
ullamco laboris nisi ut aliquip ex ea\n\
commodo consequat. Duis aute irure\n\
dolor in reprehenderit in voluptate\n\
velit esse cillum dolore eu\n\
fugiat nulla pariatur. Excepteur sint\n\
occaecat cupidatat non proident, sunt\n\
in culpa qui officia deserunt mollit\n\
anim id est laborum.'

print('<-- default standard ')
print('class')
a = stylize('order')
print(string)

print('effect tests: \n')
for i in range (0, 100): 
    print(f'Now testing {i}')
    ts = f'\033[0m\033[{i}m{string}'
    print(ts)

