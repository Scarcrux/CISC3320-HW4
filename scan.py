""" Elevator (SCAN) """
def SCAN(tracks, head, direction, size, disk_size):
    distance = 0
    left = []
    right = []
    seek_sequence = []
    total_head_movement = 0
    track = 0

    # Add track to left or right depending on direction
    # from head
    if (direction == "left"):
        left.append(0)
    elif (direction == "right"):
        right.append(disk_size - 1)

    for i in range(size):
        if (tracks[i] < head):
            left.append(tracks[i])
        if (tracks[i] > head):
            right.append(tracks[i])

    # Sort the tracks
    left.sort()
    right.sort()

    # Process the direction specified as a parameter
    # Then process the opposite direction
    counter = 2
    while (counter != 0):
        if (direction == "left"):
            for i in range(len(left) - 1, -1, -1):
                track = left[i]

                # Add track to seek sequence
                seek_sequence.append(track)

                # Calculate distance from head to track
                distance = abs(track - head)

                # Increase the total count
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

                # Increase the total count
                total_head_movement += distance

                # Change the head to current track
                head = track

            # Reverse the direction
            direction = "left"

        counter -= 1

    print(f"Total Head Movement: {total_head_movement}")
    print("The disk seek sequence is: ")
    print(*seek_sequence, sep=" ")

# Driver to test program
if __name__ == '__main__':
    tracks = [ 4078, 153, 2819, 3294, 1433, 211, 1594, 2004, 2335, 2007, 771, 1043, 3950, 2784, 1881, 2931, 3599, 1245, 4086, 520, 3901, 2866, 947, 3794, 2353, 3970, 3948, 1815, 4621, 372, 2684, 3088, 827, 3126, 2083, 584, 4420, 1294, 917, 2881, 3659, 2868, 100, 1581, 4581, 1664, 1001, 1213, 3439, 4706 ];
    head = 100
    direction = "right"
    size = len(tracks)
    disk_size = 5000
    SCAN(tracks, head, direction, size, disk_size)
