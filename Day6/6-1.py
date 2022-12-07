from queue import Queue
bufferstream = open("input.txt", "r").read()
for i in range(len(bufferstream)-4):
    print(bufferstream[i:i+4])
    if len(set(bufferstream[i:i+4])) == 4:
        print(i+4)
        break
