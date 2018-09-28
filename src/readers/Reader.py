
import tying

class Reader(object):

    def get_x(self) -> typing.List[float]:
        raise NotImplementedError

    def get_y(self) -> typing.List[float]:
        raise NotImplementedError

    def get_title(self) -> str:
        return ""
