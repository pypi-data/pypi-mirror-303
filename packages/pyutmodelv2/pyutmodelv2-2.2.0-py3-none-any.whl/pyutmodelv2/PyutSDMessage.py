
from logging import Logger
from logging import getLogger

from dataclasses import dataclass

from pyutmodelv2.PyutLink import PyutLink


@dataclass
class PyutSDMessage(PyutLink):
    message:      str = ''
    sourceY:      int = 0
    destinationY: int = 0
    """
    A message between two lifeline of two SDInstances.

    """
    def __init__(self, message: str = "", src=None, sourceY: int = 0, dst=None, destinationY: int = 0):

        """

        Args:
            message:        for the message (aka method)
            src:            source of the link
            sourceY:        y location on the source lifeline
            dst:            where the link goes
            destinationY:   y location on the destination lifeline
        """
        self.logger: Logger = getLogger(__name__)

        self.logger.debug(f"PyutSDMessage.__init__ {sourceY}, {destinationY}")
        super().__init__(source=src, destination=dst)

        self.message      = message
        self.sourceY      = sourceY
        self.destinationY = destinationY

    # @property
    # def sourceId(self) -> int:  # ignore it because the default is None
    #     return self._src.id     # type: ignore
    #
    # @property
    # def destinationId(self) -> int:
    #     return self._dest.id      # type: ignore
    #
    # def getSource(self):
    #     """
    #     Return Y position on source
    #     @author C.Dutoit
    #     """
    #     return self._src
    #
    # def getDest(self):
    #     """
    #     Return Y position on source
    #     @author C.Dutoit
    #     """
    #     return self._dest
    #
    # def setSource(self, src=None, srcTime=-1):
    #     """
    #     Args:
    #         src:    Source object
    #         srcTime: ???
    #     """
    #     if src is not None:
    #         super().setSource(src)
    #     if srcTime != -1:
    #         self.logger.debug(f"PyutSDMessage - Setting srcTime to: {srcTime}")
    #         # self.setSrcTime(srcTime)
    #         self.sourceY = srcTime
    #
    # def setDestination(self, dst=None, dstTime=-1):
    #     """
    #     Define the destination
    #
    #     Args:
    #         dst:        destination object
    #         dstTime:    Time on the destination
    #     """
    #     if dst is not None:
    #         PyutLink.setDestination(self, dst)
    #     if dstTime != -1:
    #         self.logger.debug(f"Setting dstTime to {dstTime}")
    #         # self.setDstTime(dstTime)
    #         self.destinationY = dstTime

    def __str__(self):
        """

        Returns:    string representing this object
        """
        return f'{self.source} linked to {self.destination}'
