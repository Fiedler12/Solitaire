from Column import Column


class Table():
    def __init__(self):
        self.columns = []
        for x in range(7):
            column = Column()
            self.columns.append(column)