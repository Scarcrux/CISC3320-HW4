""" First Come-First Serve (FCFS)"""
def FCFS(tracks, head, size):
    total_head_movement = 0
    distance = 0
    track = 0

    for i in range(size):
        track = tracks[i]

        # Calculate distance from head to track
        distance = abs(track - head)

        # Add distance to total head movement
        total_head_movement += distance

        # Change the head to current track
        head = track

    print(f"Total Head Movement: {total_head_movement}")
    print("The disk seek sequence is: ")
    print(*tracks, sep=" ")

# Driver to test program
if __name__ == '__main__':
    tracks = [ 4078, 153, 2819, 3294, 1433, 211, 1594, 2004, 2335, 2007, 771, 1043, 3950, 2784, 1881, 2931, 3599, 1245, 4086, 520, 3901, 2866, 947, 3794, 2353, 3970, 3948, 1815, 4621, 372, 2684, 3088, 827, 3126, 2083, 584, 4420, 1294, 917, 2881, 3659, 2868, 100, 1581, 4581, 1664, 1001, 1213, 3439, 4706 ];
    head = 100;
    size = len(tracks);
    FCFS(tracks, head, size);
