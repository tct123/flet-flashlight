class FlashlightException(Exception):
    """Base class for all Flashlight errors."""


class FlashlightEnableExistentUserException(FlashlightException):
    """
    Exception thrown when an attempt was made to turn on the torch but it was detected that the camera was being used by another process.
    This means that the torch cannot be controlled.
    """


class FlashlightEnableNotAvailableException(FlashlightException):
    """
    Exception thrown when an attempt was made to turn on the torch but it was detected that the device does not have one equipped.
    """


class FlashlightEnableException(FlashlightException):
    """
    Exception thrown when an error occurred while trying to turn on the device torch.
    """


class FlashlightDisableExistentUserException(FlashlightException):
    """
    Exception thrown when an attempt was made to turn off the torch but it was detected that the camera was being used by another process.
    This means that the torch cannot be controlled.
    """


class FlashlightDisableNotAvailableException(FlashlightException):
    """
    Exception thrown when an attempt was made to turn off the torch but it was detected that the device does not have one equipped.
    """


class FlashlightDisableException(FlashlightException):
    """
    Exception thrown when an error occurred while trying to turn off the device torch.
    """
