'''

A trie is a specialized type of tree data structure. When used in
the context of a dictionary, each node stores the entire alphabet, and words can be reTRIEved by traversing down a branch part of the tree. The structure of a trie tree is a set of
linked tries emanating from a head trie. Each trie contains
a set of pointers (child tries), one for each alphabetic value.

The image below gives a representation of how a
trie dictionary might store the words peter, piper, picked,
peck, pickled, and peppers. For simplicity, most of the child
 nodes are omitted but the tree hierarchy can be readily seen and
  how a letter at a given level branches out (e.g p, pe, etc).
'''


class Trie:
    def __init__(self, *args):
        if len(args) > 0:
            self.words = args[0]
        else:
            self.words = []

    def update(self, new_words):
        for word in new_words:
            if word not in self.words:
                self.words.append(word)

    def is_word(self, word):
        if word in self.words:
            return True
        else:
            return False

    def remove(self, word):
        if word in self.words:
            self.words.remove(word)

    def contents(self, start="a", end="z"):
        if self.words == []:
            return "Dictionary is currently empty"
        if start == "a" and end == "z":
            return sorted(set(self.words))
        alph = "abcdefghijklmnopqrstuvwxyz"
        start = alph.index(start)
        end = alph.index(end)
        if start > end:
            return "End cannot be earlier in the alphabet than start"
        alph = alph[start: end + 1]
        return sorted([word for word in self.words if word[0] in alph])


    def num_words(self):
        length = len(set(self.words))
        if length == 0:
            return "Dictionary is currently empty"
        return length

def load(words):
    words = [word.lower() for word in words]
    return Trie(words)


d = load(["Peter", "Piper", "picked", "peppers"])
print(d.contents())
print(d.remove("peppers"))
print(d.is_word("peppers"))
print(d.update(["pineapples"]))
print(d.contents("p", "p"))
print(d.num_words())
