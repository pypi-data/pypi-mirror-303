from masterpiece.core import MasterPiece


class JDatabase(MasterPiece):
    """The base class for data storage classes.Serves as an abstract interface for managing
    interactions with various types of databases. Designed to support multiple backend databases,
    this class provides a unified API for writing sensor data and other parameters, ensuring that the
    system can seamlessly integrate with different storage solutions.
    """

    token: str = ""
    org: str = "juham"
    host: str = ""
    database = "home"

    def __init__(self, name):
        super().__init__(name)

    def write(self, point):
        """Write record to database table.

        @param point point to be written
        """
        raise Exception("write not implemented")

    def to_dict(self):
        data = super().to_dict()
        data["_database"] = {}
        attributes = ["host", "org", "database", "token"]
        for attr in attributes:
            if getattr(self, attr) != getattr(type(self), attr):
                data["_base"][attr] = getattr(self, attr)
        return data

    def from_dict(self, data_dict):
        super().from_dict(data_dict)
        for key, value in data_dict["_database"].items():
            setattr(self, key, value)
