import board_check
state_list = []
def baseb(n, b):
    e = n//b
    q = n%b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return baseb(e, b) + str(q)
file = open('file.txt', 'a')
draw = 0
x = 0
o = 0
for i in range(19683):
    state = list(baseb(i, 3))
    str_state = str(state)
    if str_state.count('0') <= 4:
        if str_state.count('1') >= 4 and str_state.count('1') <= 5:
            if str_state.count('2') >= 2 and str_state.count('2') <= 4:
                state = board_check.sorter(state)
                if state[0] == '0':
                    file.writelines(f'{state}\n')
                    draw += 1
                elif state[0] == '1':
                    file.writelines(f'{state}\n')
                    x += 1
                elif state[0] == '2':
                    file.writelines(f'{state}\n')
                    o += 1
print(x)
print(o)
print(draw)
print(x + o + draw)
