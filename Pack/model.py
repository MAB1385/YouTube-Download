from MyException import DataException
from InputHandling import InputException
from YouTube import YT
class File:
    def __init__(self,l=str,a=str) -> None:
        if ans := self.Chek(l,a):
            self.__url=l
            self.__address=a
            self.__video_down=YT(self.__url)
        else:
            self.__url=''
            self.__address=''
            self.__video_down=''

    def Chek(self,l,a):
        try:
            InputException.ChakURL(l)
            InputException.ChakAddress(a)
        except DataException as error:
            raise error
        
        else:
            return True

    def DownloadVideo(self):
        
        self.__video_down.Download(self.__address)
        

    def __str__(self) -> str:
        return f'URL={self.__url}\tAddress={self.__address}'
