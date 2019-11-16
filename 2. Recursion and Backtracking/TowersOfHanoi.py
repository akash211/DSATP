# //? What it does?
# //! Calculate How to solve tower of Hanoi problem where we have 3 towers and n number of disks


# //TODO Here is the function which gives us steps to solve tower of hanoi problem:

def towersOfHanoi(numberOfDisks, start_tower=1, end_tower = 3):
    if numberOfDisks:
        towersOfHanoi(numberOfDisks-1, start_tower, 6-start_tower-end_tower)
        print(f"Move disk {numberOfDisks} from tower {start_tower} to tower {end_tower}")
        towersOfHanoi(numberOfDisks-1, 6-start_tower-end_tower, end_tower)

towersOfHanoi(4)

