import pickle


class PickleHelper:
    def __init__(self):
        self.message = "this is a test message"

    def save_to(self, location, obj):
        f = open(location, "wb")
        pickle.dump(obj, f)
        f.close()

    def load_back(self, location):
        f = open(location, 'rb')
        g = pickle.load(f)
        f.close()
        return g


if __name__ == '__main__':
    # local testing
    PickleObj = PickleHelper()
    print(PickleObj.message)
    PickleObj.save_to('PickleObj.b', PickleObj)
    PickleObj2 = PickleObj.load_back('PickleObj.b')
    print(PickleObj2.message)
