from matplotlib import pyplot as plt
from random import randint
from math import atan2



class Bod:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(bod1, bod2, bod3):
    return (bod2.x - bod1.x)*(bod3.y - bod1.y) - (bod2.y - bod1.y)*(bod3.x - bod1.x)

def najdi_bod_s_nejnizsim_y(body):
    prvni_bod = body[0]
    bod_s_nejnizsim_y = prvni_bod
    poradi = 0
    vysledne_poradi = poradi

  # projdeme to bod po bodu
    for bod in body:
        if (bod.y < bod_s_nejnizsim_y.y):
            bod_s_nejnizsim_y = bod
            vysledne_poradi = poradi
        poradi += 1

    return (bod_s_nejnizsim_y, vysledne_poradi)

def polarni_uhel(bod1, bod2=None):
    if bod2 == None:
        bod2 = anchor
    y_odvesna=bod1.y-bod2.y
    x_odvesna=bod1.x-bod2.x
    return atan2(y_odvesna,x_odvesna)

def vzdalenost_bodu(bod1, bod2=None):
    if bod2==None:
        bod2 = anchor
        y_odvesna=bod1.y-bod2.y
        x_odvesna=bod1.x-bod2.x
        return y_odvesna**2 + x_odvesna**2


def seradit_body_podle_uhlu(body):
    if len(body) <=1:
        return body
    mensi=[]
    vetsi=[]
    rovno=[]
    random_uhel = polarni_uhel(body[randint(0,len(body)-1)],body[0])
    for bod in body:
        uhel_bodu=polarni_uhel(bod, body[0])
        if uhel_bodu < random_uhel:
            mensi.append(bod)
        elif uhel_bodu == random_uhel:
            rovno.append(bod)
        else:
            vetsi.append(bod)
    return seradit_body_podle_uhlu(mensi) \
            + sorted(rovno, key=vzdalenost_bodu) \
            + seradit_body_podle_uhlu(vetsi)


def vypis_body(body):
    for bod in body:
        print(bod.x, bod.y)

# tady zacina program bezet
bodA = Bod(1,5)
bodB = Bod(5,6)
bodC = Bod(1,2)
bodD = Bod(8,2)

body = [bodA, bodB, bodC, bodD]

print('zacatek')
vypis_body(body)

# let N be number of points
N = len(body)


prvni_bod = body[0]
bod_s_nejnizsim_y, poradi = najdi_bod_s_nejnizsim_y(body)

# swap points[0] with the point with the lowest y-coordinate
# prohodime body
body[0] = bod_s_nejnizsim_y
body[poradi] = prvni_bod

print('po swapu')
vypis_body(body)

# sort points by polar angle with points[0]
global anchor
anchor = body[0]
serazene_body = seradit_body_podle_uhlu(body)



print(vypis_body)
vypis_body(serazene_body)

# let stack = empty_stack()
# push points[0] to stack
# push points[1] to stack
# for i = 2 to N-1:



class Stack():
    def __init__(self):
        self.serazene_body = []

    def push(self,serazene_body):
        self.serazene_body.append(serazene_body)

    def pop(self):
        return self.serazene_body.pop()

    def count(self):
        return self.serazene_body.count()

    def is_empty(self):
        return self.serazene_body == []

    def top_stack(self):
         if not self.is_empty():
            return self.serazene_body[-1]

    def next_to_top(self):
        if not self.is_empty():
            return self.serazene_body[-2]

    def get_stack(self):
        return self.serazene_body

stack=Stack()
stack.push(serazene_body[0])
stack.push(serazene_body[1])
print(stack.get_stack())

for i in range(2,N-1):
    while stack.count() >= 2 and ccw(stack.next_to_top(serazene_body), stack.top_stack(serazene_body), serazene_body[i]) <= 0:
        stack.pop(serazene_body[-1])
    stack.push(body[i])

#for i = 2 to N-1:
    #while count stack >= 2 and ccw(next_to_top(stack), top(stack), points[i]) <= 0:
        #pop stack
    #push points[i] to stack
#end

