name = input()

if name[0] == name[1]:
    b_name = name.replace(name[0], 'b', 1)
    f_name = name.replace(name[0], 'f', 1)
    m_name = name.replace(name[0], 'm', 1)
else:
    b_name = name.replace(name[0], 'b')
    f_name = name.replace(name[0], 'f')
    m_name = name.replace(name[0], 'm')

print(f'{name}, {name}, bo-{b_name}')
print(f'banana-fana fo-{f_name}')
print(f'fee-fi-mo-{m_name}')
print(f'{name}!')
