import uuid


class UUIDTools(object):
    """uuid function tools"""

    @staticmethod
    def uuid1_hex():
        """
        return uuid1 hex string

        eg: 23f87b528d0f11e696a7f45c89a84eed
        """
        return str(uuid.uuid1().hex)