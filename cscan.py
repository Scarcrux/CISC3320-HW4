""" Circular SCAN """
def CSCAN(arr, head, size, disk_size):
    distance = 0
    left = []
    right = []
    seek_sequence = []
    total_disk_movement = 0
    track = 0


    # Add end values
    left.append(0)
    right.append(disk_size - 1)

    # Add track to left or right depending on direction
    # from head
    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])

    # Sort the tracks
    left.sort()
    right.sort()

    # Traverse through tracks to the right of the head
    for i in range(len(right)):
        track = right[i]

        # Add track to seek sequence
        seek_sequence.append(track)

        # Calculate distance from head to track
        distance = abs(track - head)

        # Add distance to total head movement
        total_disk_movement += distance

        # Change the head to current track
        head = track

    # Once reached the right end
    # jump to the beggining.
    head = 0

    # Add seek count for head returning from disk_size to 0
    total_disk_movement += (disk_size - 1)

    # Traverse through tracks to the left of the head
    for i in range(len(left)):
        track = left[i]

        # Add track to seek sequence
        seek_sequence.append(track)

        # Calculate distance from head to track
        distance = abs(track - head)

        # Add distance to total head movement
        total_disk_movement += distance

        # Change the head to current track
        head = track

    print("Total number of seek operations =",
          total_disk_movement)
    print("Seek Sequence is")
    print(*seek_sequence, sep=" ")

# Driver to test program
if __name__ == '__main__':
    tracks = [ 4078, 153, 2819, 3294, 1433, 211, 1594, 2004, 2335, 2007, 771, 1043, 3950, 2784, 1881, 2931, 3599, 1245, 4086, 520, 3901, 2866, 947, 3794, 2353, 3970, 3948, 1815, 4621, 372, 2684, 3088, 827, 3126, 2083, 584, 4420, 1294, 917, 2881, 3659, 2868, 100, 1581, 4581, 1664, 1001, 1213, 3439, 4706 ];
    head = 100;
    size = len(tracks)
    disk_size = 5000
    CSCAN(tracks, head, size, disk_size)
