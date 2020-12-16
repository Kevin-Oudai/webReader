import pyautogui
import time
import os

# Find Ordered Item
# Location: 'items/ordered_item/<item>
CONF = 0.8
MOUSE_SPEED = 0.25
COFFEE_LOCATIONS = [(337, 717), (406, 726), (480, 733)]
MS_LOCATIONS = [(635, 703), (671, 617), (706, 537)]
OVEN_LOCATIONS = [(1538, 567)]


def find_order():
    possibleItems = ['coffee.png', 'milk_shake.png', 'vanilla_cake.png']
    count = 0
    while True:
        collect_money()
        if pyautogui.locateCenterOnScreen('items/served_items/restart.png'):
            pyautogui.click(1360, 941)
        for item in possibleItems:
            searchFor = 'items/ordered_item/{}'.format(item)
            locateItem = pyautogui.locateOnScreen(searchFor, confidence=CONF)
            if locateItem:
                return pyautogui.center(locateItem), item
        count += 1

# Create Ordered Item


def create_order(item):
    print("**Creating: {}".format(item))
    if item == 'coffee.png':
        locateItem = COFFEE_LOCATIONS[create_order.counter % 3]
        create_order.counter += 1
        return locateItem
    elif item == 'milk_shake.png':
        if create_order.mscounter % 3 == 0:
            pyautogui.click(626, 834)
            time.sleep(4.1)
        locateItem = MS_LOCATIONS[create_order.mscounter % 3]
        create_order.mscounter += 1
        return locateItem
    elif item == 'vanilla_cake.png':
        addMold = pyautogui.locateOnScreen(
            'items/served_items/cake_mold.png', confidence=CONF)
        moldCenter = pyautogui.center(addMold)
        pyautogui.click(moldCenter[0], moldCenter[1])
        flavorCenter = (1240, 623)
        pyautogui.moveTo(flavorCenter[0], flavorCenter[1], MOUSE_SPEED)
        pyautogui.dragTo(1057, 690, MOUSE_SPEED, button='left')
        ovenCenter = OVEN_LOCATIONS[0]
        pyautogui.dragTo(ovenCenter[0], ovenCenter[1],
                         MOUSE_SPEED, button='left')
        time.sleep(4.1)
        return ovenCenter
    else:
        return None


# Serve Ordered Item
def serve_item(orderCenter, itemCenter):
    print("***Serving: {}".format(itemCenter))
    pyautogui.moveTo(itemCenter[0], itemCenter[1], MOUSE_SPEED)
    pyautogui.dragTo(orderCenter[0], orderCenter[1],
                     MOUSE_SPEED, button='left')


def collect_money():
    print("****Collecting Money")
    locations = pyautogui.locateAllOnScreen(
        'items/served_items/money.png', confidence=CONF)
    for item in locations:
        itemloc = pyautogui.center(item)
        pyautogui.click(itemloc[0], itemloc[1])
# Main Control


def main():
    create_order.counter = 0
    create_order.mscounter = 0
    while True:
        orderCenter, item = find_order()
        itemCenter = create_order(item)
        serve_item(orderCenter, itemCenter)


main()
