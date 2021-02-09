class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, new_width):
        self.width = new_width
        
    def set_height(self, new_height):
        self.height = new_height        

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        pic = ''
        
        if self.width > 50 or self.height > 50:
            
            return 'Too big for picture.'
        
        else:
            for h in range(self.height):
                pic = pic + '*' * self.width + '\n'

            pic = pic.rstrip()

            return pic
    
    def get_amount_inside(self, target):
        pass

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
#class Square:
