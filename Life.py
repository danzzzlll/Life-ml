from random import choice

MAX_SIZE = int(input())
DEAD = ' '
LIVE = 'x'


class Neighbors:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def neighbor_xy(x, y):
        for dx, dy in (
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
                (-1, -1),
                (-1, 0),
                (-1, 1)
        ):
            yield x + dx, y + dy


    def show_field(field):
        for y in range(MAX_SIZE):
            print(''.join(field[y]))

    def get_empty_field():
        return [
            [DEAD for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
        ]


class Live:
    def __init__(self,field,neighbor_x, neighbor_y):
        self.field = field
        self.neighbor_x = neighbor_x
        self.neighbor_y = neighbor_y

    def is_live(field, neighbor_x, neighbor_y):
        return 0 <= neighbor_x < MAX_SIZE \
               and 0 <= neighbor_y < MAX_SIZE \
               and field[neighbor_y][neighbor_x] == LIVE




if __name__ == '__main__':

    field = [
        [choice([DEAD, LIVE]) for x in range(MAX_SIZE)] for y in range(MAX_SIZE)
    ]

    while True:
        input('-----------------------------')
        Neighbors.show_field(field)
        buffer = Neighbors.get_empty_field()
        for y in range(MAX_SIZE):
            for x in range(MAX_SIZE):
                c = field[y][x]
                neighbors = 0
                for neighbor_x, neighbor_y in Neighbors.neighbor_xy(x, y):
                    neighbors += 1 if Live.is_live(field, neighbor_x, neighbor_y) else 0
                if c == DEAD:
                    buffer[y][x] = LIVE if neighbors == 3 else DEAD
                else:
                    buffer[y][x] = LIVE if neighbors in (2, 3) else DEAD

        if field == buffer:
            print('stasis')
            break
        field = buffer
