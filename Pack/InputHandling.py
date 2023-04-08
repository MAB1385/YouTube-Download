from pytube import YouTube
from os import path
from MyException import DataException
from re import compile
class InputException:

    @staticmethod
    def ChakURL(i=str):
        if i=='':
            raise DataException('URL is not valid')

        r=compile('https:\/\/www\.youtube\.com\/watch\?v=.*')
        if r.match(i)==False:
            raise DataException('URL is not valid')
          
        try:
            s=YouTube(i)
        except:
            raise DataException('URL is not valid')

        return True

    @staticmethod
    def ChakAddress(i=str):
        if i=='':
            raise DataException('Address is not valid')

        if path.exists(i)==False:
           raise DataException('Address is not valid')

        return True