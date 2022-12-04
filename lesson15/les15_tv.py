#task3

channels = ["BBC", "Discovery", "TV1000"]

class TVController():

    def __init__(self, channels):
        self.channels = channels
        self.cur_channel = 0

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, n):
        if n < 1 or n > len(self.channels):
            return "No channel found"
        else:
            self.cur_channel = n-1
        return self.channels[self.cur_channel]

    def next_channel(self):
        if len(self.channels)-1 == self.cur_channel:
            self.cur_channel = 0
        else:
            self.cur_channel += 1
        return self.channels[self.cur_channel]

    def previous_channel(self):
        if self.cur_channel == 0:
            self.cur_channel = len(self.channels)-1
        else:
            self.cur_channel -= 1
        return self.channels[self.cur_channel]

    def current_channel(self):
        return self.channels[self.cur_channel]

    def is_exist(self, n):
        if isinstance(n, int):
            if 0 <= n-1 < len(self.channels):
                return "Yes"
            return "No"
        elif isinstance(n, str):
            if n in self.channels:
                return "Yes"
            return "No"
        return "Error"

def main():
    controller = TVController(channels)
    print(controller.first_channel())
    # print(controller.previous_channel())
    # print(controller.previous_channel())
    # print(controller.next_channel())
    # print(controller.next_channel())
    # print(controller.is_exist("BBC"))
    # print(controller.is_exist(2))
    # print(controller.is_exist(9))
    # print(controller.is_exist(dict))

    print("""TV remote buttons:
    1. First channel
    2. Last channel
    3. Go to channel
    4. Next channel
    5. Previous channel
    6. Show the current channel name
    7. Check if channel exist
    8. Turn off TV""")
    while True:
        try:
            command = int(input("Press the button to navigate between channels: "))
            if command == 1:
                print(controller.first_channel())
            elif command == 2:
                print(controller.last_channel())
            elif command == 3:
                n = int(input("Type the channel you want to turn: "))
                print(controller.turn_channel(n))
            elif command == 4:
                print(controller.next_channel())
            elif command == 5:
                print(controller.previous_channel())
            elif command == 6:
                print(controller.current_channel())
            elif command == 7:
                n = input("Type the channel number or channel name: ")
                print(controller.is_exist(n))
            elif command == 8:
                break
            else:
                raise Exception
        except:
            print("Error")


if __name__ == "__main__":
    main()