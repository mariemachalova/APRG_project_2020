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
    with open(file, 'map_data_0.json') as f:
        start_position.append(Point(robot_position(x), robot_position(y)))

    return start_position

def read_input_file(file):
    finish_position = []
    with open(file, 'map_data_1.json') as f:
        finish_position.append(Point(robot_position(x), robot_position(y)))