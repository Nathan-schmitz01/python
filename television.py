class Television:
    """
    Class to represent the details of a television object.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Method to set default values for the Television object.
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    
    def power(self) -> None:
        '''
        Method to change the status instance variable of the Television object.
        '''
        self.__status = not self.__status
    
    def mute(self) -> None:
        '''
        Method to change the value of muted instance variable.
        '''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        '''
        Method to increment the channel instance variable by one.
        '''
        if not self.__status:
            pass

        elif self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        
        else:
            self.__channel += 1
    
    def channel_down(self) -> None:
        '''
        Method to decrement the channel instance variable by one.
        '''
        if not self.__status:
            pass

        elif self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        
        else:
            self.__channel -= 1
    
    def volume_up(self) -> None:
        '''
        Method to increment the volume instance variable by one.
        '''
        if self.__status:
            self.__muted = False

            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self) -> None:
        '''
        Method to decrement the volume instance variable by one.
        '''
        if self.__status:
            self.__muted = False

            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
    
    def __str__(self) -> str:
        '''
        Method to get the current power, channel, and volume of the instance of the Television.
        :return: a string with the current power, channel, and volume of the instance of the Television.
        '''
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"