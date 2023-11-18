class Television():

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
        """
        inverts the power status of the tv when run
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

        return self.__status

    def mute(self):
        """
        inverts the state of mute when run
        """
        if self.__status == True:

            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self):
        """
        Lowers the channel by 1, wraps around if below minimum
        """
        if self.__status == True:

            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL


    def channel_down(self):
        """
        Lowers the channel by 1, wraps around if below minimum
        """
        if self.__status == True:

            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL


    def volume_up(self):
        """
        lowers the volume by 1 and unmutes if neccessary
        """
        if self.__status == True:

            if self.__muted == True:
                self.mute()

            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        lowers the volume by 1 and unmutes if neccessary
        """
        if self.__status == True:

            if self.__muted == True:
                self.mute()

            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1


    def __str__(self) -> str:
        """
        Used to display the current state of the tv
        :return: status sting
        """
        if self.__muted == False:
            status = f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            status = f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        return status