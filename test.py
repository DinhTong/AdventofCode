from collections import OrderedDict

#x = input('Enter test number : ')
x = "eao\nwoa\nao\noa"

dataInput = x.replace("\n", "")

def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))

if __name__ == "__main__":
    print ("Original String : ", dataInput)
    print ("Dedupped String : ", removeDupWithOrder(dataInput))

    