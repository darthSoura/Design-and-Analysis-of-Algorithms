def tower_of_hanoi(n, peg1, peg3, peg2):
    if n == 1:
        print("Move disk 1 from ", peg1, "to ", peg3)
        return
    tower_of_hanoi(n-1, peg1, peg2, peg3)
    print("Move disk", n, "from ", peg1, "to ", peg3)
    tower_of_hanoi(n-1, peg2, peg3, peg1)


tower_of_hanoi(4, 'A', 'C', 'B')
