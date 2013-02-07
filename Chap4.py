# All Exercises in Chapter 4 of Learning Python v4


# writing files
def p138newfile():
    file = open('data.txt', 'w')
    file.write("Hello file world!\n")
    file.write("Bye file world.\n")
    file.close()


def p140newfile():
    with open('data2.txt', 'w') as myfile:
        myfile.write('This is another test\n')
        myfile.writelines('Yet another line two but with writelines takes a list\n')
        myfile.write('Yet another line 3\n')

def p141openfile():
    print ('p141openfile')
    file = open('data.txt')
    lines = file.readlines()
    for line in lines:
        print(line, end='')

def p142readfile():
    print ('p142readfile')
    file = open('data.txt')
    file.seek(0)
    print ('Full Read')
    print (file.read())
    file.seek(0)
    print ('Read Lines into list')
    print (file.readlines())
    file.seek(0)
    print ('read 1')
    print (file.readline())
    print ('read 2')
    print (file.readline())
    print ('read byte counts first 1, then 8')
    file.seek(0)
    print (file.read(1))
    print (file.read(8))

def p143iterators():
    print ('p143iterators')
    print ('basic for loop')
    for line in open('data.txt'):
        print (line, end = '')
    print ('Other ways')
    print (open('data.txt').readlines())   # get a list
    print (list(open('data.txt')))  # force a list


if __name__ == "__main__":
    p138newfile()
    p140newfile()
    p141openfile()
    p142readfile()
    p143iterators()