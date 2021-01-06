# x = input('Enter your text: ')
# print (x)
#  git config --global user.email "you@example.com"
#   git config --global user.name "Your Name"
x = [1,2,3,4,5]
#print len(x)
#print x[2]

#list = []
# print max(num1, num2, num3, num4)
# print sum(x)
crossWalk = ['E-1','N-2','W-3','S-4']
# d2v = direction to value. This translates direction initial to value.
# v2d = value to direction. This translates value to direction initial.
def directionTranslator (x, y):
    if x == 'd2v':
        for i in crossWalk:
            temp = i.split('-')
            val1 = temp[0]
            val2 = temp[1]
            if y == val1:
                return val2
                break
    elif x == 'v2d':
        for i in crossWalk:
            temp = i.split('-')
            val1 = temp[0]
            val2 = temp[1]
            if str(y) == val2:
                return val1
                break

print directionTranslator ('v2d', 3)

