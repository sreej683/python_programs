io=iter('lasya')
print(next(io))
print('lasya is good girl')
print(next(io))
print(next(io))
print(next(io))
print(next(io))
print(next(io))




class CIRC():
    def _init_(self,sv,ev,u=1):
        self.sv=sv
        self.ev=ev
        self.up=u
    def _iter_(self):
        print('_iter_ is called')
        self.i=self.sv
        return self
    def __next(self):
        print('_next_is called')
        if self.i<self.sv:
            res=self.i
            self.i+=self.u
            return res
        else:
            return stopiteration
CIO=CIRC(1,5)
for i in CIO:
    print(i)
