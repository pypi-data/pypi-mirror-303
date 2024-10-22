from chainalysis.utils import Stringify


class Utils:
    """
    This class contains util/helper functions for users
    of the SDK.
    """

    def __init__(self):
        self.s = Stringify()

    @property
    def stringify(self) -> Stringify:
        """
        Call the stringify property to access the Stringify class.
        """
        return self.s
