import pickle


class ClassA(object):
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def printout(self):
        print("a = " + str(self.a) + "\t" + "b = " + str(self.b))


def dump_note():
    """
        序列化测试
    """

    aa = ClassA(4, 5)
    output = open('classdata.pkl', 'wb')
    pickle.dump(aa, output)
    output.close()

    with open('classdata.pkl', 'rb') as pkl_file:
        data = pickle.load(pkl_file)
        data.printout()
