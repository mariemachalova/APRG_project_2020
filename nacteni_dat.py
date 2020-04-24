x = []
y = []
robot_position= []
    self.x = x
    self.y = y


def get_x(self):
    return self.x
 def get_y(self):
    return self.y

def read_input_file(file):
    start_position = []
    with open(file, 'r') as f:
        for line in f:
            x, y = ''.join(line.split()).split(',')
            start_position.append(Point(robot_position(x), robot_position(y)))

    return start_position