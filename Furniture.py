"""7. Furniture.
1. Class House: household type, total area, remaining area and furniture name list.
The new house has no furniture at all.
2. Furniture has a name and area, of which Bed: 4 square meters, Wardrobe: 2 square
meters, Table: 1.5 square meters.
3. Add the above three pieces of furniture to the house.
4. When printing a house, output is required: household type, total area, remaining
area, furniture name list."""


class Furniture:
    def __init__(self, fur_type, area):
        self.type = fur_type
        self.area = area
        print(f'The {self.fur_type} with an area of {self.area} squeare meters')

class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.furniture_list = []

class Furniture:
    def __init__(self, furniture_type, fur_area):
        self.funiture_type = furniture_type
        self.fur_area = fur_area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        print(f'House type: {self.house_type} with total area: {self.area} \t [remaining free area: {self.free_area}] \t furniture: {self.item_list}')

    def add_item(self, item):
        for i in range(self.item_list):
            if self.fur_area > self.free_area:
                print(f'{} is too large to add '% item.name')

        self.item_list.append(item.name)
        self.free_area -= item.area


bed = HouseItem('bed', 4)
yg = HouseItem('yg', 2)
table = HouseItem('table', 1.5)


 # 2. Create a house object
 My_house = House('Two rooms and one living room', 100)
 # 3. Add furniture
my_house.add_item(bed)
my_house.add_item(yg)
my_house.add_item(table)


print(my_house)

https://realpython.com/python-super/#an-overview-of-pythons-super-function
