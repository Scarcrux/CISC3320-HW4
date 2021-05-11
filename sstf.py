""" Shortest Seek Time First (SSTF) """
def SSTF(tracks, head, size):
    if (size == 0):
        return

    seek_sequence = [0] * (size + 1)
    total_head_movement = 0
    track = [0] * size

    # Initialize array
    for i in range(size):
        track[i] = [0, 0]

    for i in range(size):
        index = -1
        minimum = float('inf')
        seek_sequence[i] = head

        # Calculate distance from head to track
        for i in range(len(track)):
            track[i][0] = abs(tracks[i] - head)

        # Find unaccessed track at minimum distance from head
        for i in range(len(track)):
            if (not track[i][1] and
                    minimum > track[i][0]):
                minimum = track[i][0]
                index = i

        track[index][1] = True

        # Add distance to total head movement
        total_head_movement += track[index][0]

        # Change head to the current track
        head = tracks[index]

    # Add head to the seek sequence
    seek_sequence[len(seek_sequence) - 1] = head

    print(f"Total Head Movement: {total_head_movement}")
    print("\nThe disk seek sequence is: ")
    print(*seek_sequence, sep=" ")

# Disk Scheduler Command Line Interface
def main():
    # Loop until the quit option is selected
    while True:
        try:
            print("\nDisk Scheduler Menu\n")
            print("1: SSTF")
            print("2: Quit\n")
            menu = int(input("Menu Selection: "))

            if (menu == 1):
                    tracks = [ 4078, 153, 2819, 3294, 1433, 211, 1594, 2004, 2335, 2007, 771, 1043, 3950, 2784, 1881, 2931, 3599, 1245, 4086, 520, 3901, 2866, 947, 3794, 2353, 3970, 3948, 1815, 4621, 372, 2684, 3088, 827, 3126, 2083, 584, 4420, 1294, 917, 2881, 3659, 2868, 100, 1581, 4581, 1664, 1001, 1213, 3439, 4706 ];
                    size = len(tracks)

                    # Get user input for initial head position
                    head = int(input("\nEnter initial head position: "))

                    SSTF(tracks, head, size)

            elif (menu == 2):
                break
            else:
                print("\nError: Please enter a valid menu option")
        # Handle non-integer input
        except ValueError:
            print("\nError: Please enter a valid menu option or initial head position")

if __name__ == '__main__':
    main()
