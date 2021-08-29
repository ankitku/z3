from z3 import *

class UserPropagate(UserPropagateBase):
    def __init__(self, s):
        super(self.__class__, self).__init__(s)
        self.add_fixed(self.myfix)
        self.add_final(self.myfinal)
        self.add_eq(self.myeq)
        self.xvalues = {}
        self.id2x = {self.add(x) : x for x in xs}
        self.x2id = { self.id2x[id] : id for id in self.id2x }
        self.trail = []
        self.lim = []


    # overrides a base class method
    def push(self):
        print("push")
        self.lim.append(len(self.trail))

    # overrides a base class method
    def pop(self, num_scopes):
        print("pop")
        lim_sz = len(self.lim)-num_scopes
        trail_sz = self.lim[lim_sz]
        while len(self.trail) > trail_sz:
            fn = self.trail.pop()
            fn()
        self.lim = self.lim[0:lim_sz]


    def myfix(self, id, e):
        x = self.id2x[id]
        v = e.as_long()
        self.trail.append(lambda : self.undo(x))        
        self.xvalues[x] = v

    def myeq(self, id1, id2):
        print("myeq called with : " + self.id2x[id1] + " = " + self.id2x[id2])
        print("xvalues currently are : " + str(self.xvalues))
        #self.conflict([self.x2id[x] for x in self.xvalues])


    def undo(self, x):
        del self.xvalues[x]


    def myfinal(self):
        print("myfinal was called here")
        print(self.xvalues)

vs = [String("x"),String("y"),String("z"),String("u"), String("v"), String("w")]
xs = [vs[0] + "c" + vs[1] + "c" + vs[2] + vs[4] + vs[1] + "c" + vs[1] + "a", vs[1] + "ac" + vs[5] + "a" + vs[2] + vs[4] + "b" + vs[3]]
print(xs)

s = SimpleSolver()

s.add(xs[0] == xs[1])

p = UserPropagate(s)
print(s.check())
print(s.model())    

