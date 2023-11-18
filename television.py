class Television():

    print('hello')
    def __init__(self):
        self.MIN_VOLUME = 0
        self.MAX_VOLUME = 2
        self.MIN_CHANNEL = 0
        self.MAX_CHANNEL = 3

        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL


    def power(self):
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if self.__status == True:

            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self):
        if self.__status == True:

            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status == True:

            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL


    def volume_up(self):
        if self.__status == True:

            if self.__muted == True:
                self.mute()

            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status == True:

            if self.__muted == True:
                self.mute()

            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1


    def __str__(self):
        if self.__muted == False:
            status = f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            status = f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        return status