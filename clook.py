""" Circular LOOK """
def CLOOK(arr, head, size):
    distance = 0
    left = []
    right = []
    seek_sequence = []
    total_head_movement = 0
    track = 0

    # Sort tracks based on direction from the head
    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])

    # Sort the tracks
    left.sort()
    right.sort()

    # Traverse through tracks to the right of the head
    if (len(right) > 0):
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

    if (len(left) > 0):
        # Set the head to the first track in left
        total_head_movement += abs(head - left[0])
        head = left[0]

        # Traverse through tracks to the left of the head
        for i in range(len(left)):
            track = left[i]

            # Add track to seek sequence
            seek_sequence.append(track)

            # Calculate distance from head to track
            distance = abs(track - head)

            # Add distance to total head movement
            total_head_movement += distance

            # Change the head to current track
            head = track

    print(f"Total Head Movement: {total_head_movement}")
    print("\nThe disk seek sequence is: ")
    print(*seek_sequence, sep=" ")

# Disk Scheduler Command Line Interface
def main():
    # Loop until the quit option is selected
    while True:
        try:
            print("\nDisk Scheduler Menu\n")
            print("1: C-LOOK")
            print("2: Quit\n")
            menu = int(input("Menu Selection: "))

            if (menu == 1):
                    tracks = [ 4078, 153, 2819, 3294, 1433, 211, 1594, 2004, 2335, 2007, 771, 1043, 3950, 2784, 1881, 2931, 3599, 1245, 4086, 520, 3901, 2866, 947, 3794, 2353, 3970, 3948, 1815, 4621, 372, 2684, 3088, 827, 3126, 2083, 584, 4420, 1294, 917, 2881, 3659, 2868, 100, 1581, 4581, 1664, 1001, 1213, 3439, 4706 ];
                    size = len(tracks)

                    # Get user input for initial head position
                    head = int(input("\nEnter initial head position: "))

                    CLOOK(tracks, head, size)

            elif (menu == 2):
                break
            else:
                print("\nError: Please enter a valid menu option")
        # Handle non-integer input
        except ValueError:
            print("\nError: Please enter a valid menu option or initial head position")

if __name__ == '__main__':
    main()


