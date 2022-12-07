from queue import Queue
bufferstream = open("input.txt", "r").read()
for i in range(len(bufferstream)-14):
    print(bufferstream[i:i+14])
    if len(set(bufferstream[i:i+14])) == 14:
        print(i+14)
        break
