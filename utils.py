from models import Coordinate

def count_coordinates():
    return Coordinate.select().count()

