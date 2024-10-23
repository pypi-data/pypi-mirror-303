import math as mt

class Rocket():

    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if isinstance(other,Rocket):
            return (self.x==other.x) and (self.y==other.y)
        return False
            
    
    def __str__(self) -> str:
        return f"A Rocket positioned at ({self.x},{self.y})"
    
    def __repr__(self) -> str:
         return f"Rocket({self.x},{self.y})"
    
    def move_up(self,x_increment=0,y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self,other:'Rocket'):
        distance_vector_x = (self.x) - (other.x)
        distance_vector_y = (self.y) - (other.y)
        distance_scaler = (distance_vector_x ** 2 + distance_vector_y **2) ** 0.5
        return distance_scaler 
    
class Shuttle(Rocket):

    def __init__(self, x=0, y=0,flights_completed=0) -> None:
        super().__init__(x, y)
        self.flights_completed = flights_completed

class CircleRocket(Rocket):

    def __init__(self, x=0, y=0,raduis=0) -> None:
        super().__init__(x, y)
        self.raduis = raduis

    def get_area(self):
        area = (self.raduis **2) * mt.pi
        return area

    def get_circumference(self):
        circum = 2*mt.pi* self.raduis
        return circum          