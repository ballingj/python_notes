for bottles in range(99, 0, -1):
    print(f"{bottles} bottles of beer on the wall.")
    print(f"{bottles} bottles of beer.")
    if bottles > 1:
        print(f"Take one down, pass it around, {bottles-1} bottles of beer on the wall.")
        print("**************************************************************************")
    else:
        print("Take one down, pass it around, no more bottles of beer on the wall.")
        print("**************************************************************************")
