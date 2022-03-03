import pickle

class Selfie:

    def __init__(self):
        self.lst_state = []

    def save_state(self):
        self.lst_state.append(pickle.dumps(self))

    def recover_state(self, n):
        if 0 <= n < len(self.lst_state):
            obj = pickle.loads(self.lst_state[n])
            obj.lst_state = self.lst_state
            return obj
        return self

    def n_states(self):
        return len(self.lst_state)

p = Selfie()

p.x = 2
p.save_state()
p.x = 5
p = p.recover_state(0)

print(p.x)