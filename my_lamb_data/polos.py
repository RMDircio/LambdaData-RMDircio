

class Polo:
    def __init__(self, size, color, price=69.99):
        self.size = size
        self.color = color
        self.price = price

    def wash(self):
        print(f'Washing the {self.size} {self.color} polo.')


if __name__ == "__main__":
    polo1 = Polo(size='Large', color='Blue')
    print(polo1.size, polo1.color)
    polo1.wash()
    
    polo2 = Polo(size='Small', color='Yellow')
    print(polo2.size, polo2.color)
    polo2.wash()




