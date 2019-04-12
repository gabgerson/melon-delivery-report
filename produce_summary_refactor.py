

def produce_summary(day, path):

    print(f"Day {day}")
    the_file = open(path)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()



produce_summary(1, "um-deliveries-20140519.txt")


produce_summary(2, "um-deliveries-20140520.txt")

produce_summary(3, "um-deliveries-20140521.txt")

