def crc(msg, div, code='000'):

    msg = msg + code

    msg = list(msg)

    div = list(div)

    for i in range(len(msg)-len(code)):

        if msg[i] == '1':
            for j in range(len(div)):
                msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)

    return ''.join(msg[-len(code):])


div = '1001'
msg = '10111011'

print('Input message given:', msg)
print('divisor:', div)
code = crc(msg, div)

print('Output:', code)


print('Done:', crc(msg, div, code) == '000')


