import pyautogui
import time

CONF = 0.985
MOUSE_SPEED = 0.25
COFFEE_LOCATIONS = [(337, 717), (406, 726), (480, 733)]
MS_LOCATIONS = [(635, 703), (671, 617), (706, 537)]
OVEN_LOCATIONS = [(1538, 567)]
ORDER_REGIONS = [
    (282, 130, 156, 266),
    (632, 139, 161, 273),
    (974, 136, 156, 268),
    (1321, 138, 160, 272)
]
SEARCH_DELAY = 3


def find_order():
    possibleItems = ['coffee.png', 'milk_shake.png', 'vanilla_cake.png']
    customerOrder = []
    for i in range(4):
        for item in possibleItems:
            searchFor = 'items/ordered_item/{}'.format(item)
            itemLocations = pyautogui.locateAllOnScreen(
                searchFor, region=ORDER_REGIONS[i], confidence=CONF)
            if itemLocations:
                for location in itemLocations:
                    customerOrder.append((item, location))
        if len(customerOrder) > 0 or len(customerOrder) == 3:
            print("ORDER")
            for food in customerOrder:
                print(food)
            return customerOrder


find_order()
