class Base:

    _nb_objects = 0


    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            _nb_objects+=1

            id = Base._nb_objects