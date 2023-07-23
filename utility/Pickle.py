import pickle
class PickleHelper:
    def __init__(self):
        pass
    def save_to(location, obj):
        f = open(location, "wb")
        pickle.dump(obj, f)
        f.close()

    def load_back(location):
        f = open(location, 'rb')
        g = pickle.load(f)
        f.close()
        return g