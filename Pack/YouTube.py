from pytube import YouTube


class YT:
    def __init__(self,url) -> None:
        self.__video=YouTube(url)
        try:
            self.__stream=self.__video.streams.get_highest_resolution()
        except:
            pass
        
    def Download(self,a=str):
        """Download

        for download video

        Args:
            a (_str_, optional): a link from youtube . Defaults to str.
        """
        self.__stream.download(output_path=a)