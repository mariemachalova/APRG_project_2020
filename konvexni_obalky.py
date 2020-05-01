from random import randint
from math import atan2
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt



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
        bod = (bod.x,bod.y)
        print(bod)

body = [(14, 46), (7.7, 77), (18.7, 89.4), (36.6, 80.3), (32.8, 54.9), (22.3, 59.9)]
body2 = [(51.7, 52.0), (54.4, 22.8), (43.8, 7.9), (34.7, 10.2), (32.2, 17.4), (23.2, 11.1), (15.6, 17.4),
             (22.2, 42.3), (37.1, 27.2), (44.4, 30.4), (41.6, 37.4)]
body3 = [(63.4, 45.1), (88.0, 54.9), (72.6, 20.6), (65.7, 27.7), (63.4, 45.1)]
body4 = [(47.3, 81.2), (58.5, 77.4), (62.8, 86.3), (88.2, 86.3), (71.1, 60.5), (66.2, 75.2), (51.7, 68.8)]

print("začátek")
vypis_body(body)




# tady zacina program bezet
# nahodne body


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
    while len(stack.get_stack()) >= 2 and ccw(stack.next_to_top(), stack.top_stack(), serazene_body[i]) <= 0:
        stack.pop()
    stack.push(body[i])

#for i = 2 to N-1:
    #while count stack >= 2 and ccw(next_to_top(stack), top(stack), points[i]) <= 0:
        #pop stack
    #push points[i] to stack
#end


