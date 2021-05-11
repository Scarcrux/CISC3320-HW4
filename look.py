
""" LOOK """
def LOOK(tracks, head, direction, size):
    distance = 0
    left = []
    right = []
    seek_sequence = []
    total_head_movement = 0
    track = 0

    # Add track to left or right depending on direction
    # from head
    for i in range(size):
        if (tracks[i] < head):
            left.append(tracks[i])
        if (tracks[i] > head):
            right.append(tracks[i])

    # Sort tracks
    left.sort()
    right.sort()

    # Process the direction specified as a parameter
    # Then process the opposite direction
    counter = 2
    while (counter):
        if (direction == "left"):
            for i in range(len(left) - 1, -1, -1):
                track = left[i]

                # Add track to seek sequence
                seek_sequence.append(track)

                # Calculate distance from head to track
                distance = abs(track - head)

                # Add distance to total head movement
                total_head_movement += distance

                # Change the head to current track
                head = track

            # Reverse the direction
            direction = "right"

        elif (direction == "right"):
            for i in range(len(right)):
                track = right[i]

                # Add track to seek sequence
                seek_sequence.append(track)

                # Calculate distance from head to track
                distance = abs(track - head)

                # Add distance to total head movement
                total_head_movement += distance

                # Change the head to current track
                head = track

            # Reverse the direction
            direction = "left"

        counter -= 1

    print(f"Total Head Movement: {total_head_movement}")
    print("\nThe disk seek sequence is: ")
    print(*seek_sequence, sep=" ")

# Disk Scheduler Command Line Interface
def main():
    # Loop until the quit option is selected
    while True:
        try:
            print("\nDisk Scheduler Menu\n")
            print("1: LOOK")
            print("2: Quit\n")
            menu = int(input("Menu Selection: "))

            if (menu == 1):
                    tracks = [ 4078, 153, 2819, 3294, 1433, 211, 1594, 2004, 2335, 2007, 771, 1043, 3950, 2784, 1881, 2931, 3599, 1245, 4086, 520, 3901, 2866, 947, 3794, 2353, 3970, 3948, 1815, 4621, 372, 2684, 3088, 827, 3126, 2083, 584, 4420, 1294, 917, 2881, 3659, 2868, 100, 1581, 4581, 1664, 1001, 1213, 3439, 4706 ];
                    size = len(tracks)

                    # Get user input for initial head position
                    head = int(input("\nEnter initial head position: "))

                    direction = "right"
                    size = len(tracks)
                    LOOK(tracks, head, direction, size)

            elif (menu == 2):
                break
            else:
                print("\nError: Please enter a valid menu option")
        # Handle non-integer input
        except ValueError:
            print("\nError: Please enter a valid menu option or initial head position")

if __name__ == '__main__':
    main()
