def read_next(*collections):
    for seq in collections:
        #for item in seq:
            #yield item
        yield from seq

for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

