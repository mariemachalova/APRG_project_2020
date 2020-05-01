from random import randint
from math import atan2



class Bod:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(bod1, bod2, bod3):
    return (bod2.y - bod1.y)*(bod3.x - bod1.x) - (bod2.x - bod1.x)*(bod3.y - bod1.y)

def najdi_bod_s_nejnizsim_y(body):
    prvni_bod = body[0]
    bod_s_nejnizsim_y = prvni_bod
    poradi = 0
    vysledne_poradi = poradi

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

def graham_scan(body):
    N = len(body)
    prvni_bod = body[0]
    bod_s_nejnizsim_y, poradi = najdi_bod_s_nejnizsim_y(body)
    body[0] = bod_s_nejnizsim_y
    body[poradi] = prvni_bod
    print('po swapu')
    vypis_body(body)



    global anchor
    anchor = body[0]
    serazene_body = seradit_body_podle_uhlu(body)
    print(vypis_body)
    vypis_body(serazene_body)

    stack = Stack()
    stack.push(serazene_body[0])
    stack.push(serazene_body[1])
    print(stack.get_stack())



    for i in range(2,N-1):
        while len(stack.get_stack()) >= 2 and ccw(stack.next_to_top(), stack.top_stack(), serazene_body[i]) <= 0:
            stack.pop()
        stack.push(body[i])



objekt = [(14, 46), (7.7, 77), (18.7, 89.4), (36.6, 80.3), (32.8, 54.9), (22.3, 59.9)]
body = []
for bod in objekt:
    body.append(Bod(bod[0], bod[1]))

print('zacatek')
vypis_body(body)

graham_scan(body)
