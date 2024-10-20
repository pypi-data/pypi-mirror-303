from masterpiece.core import MasterPiece, Application, Log
from juham.base.base import Base

class MyHomeApp(Application):
    """Juham home automation application.
    """

    encoding = "utf-8"
    
    def __init__(self, name: str = "myhome"):
        """Creates home automation application with the given name."""
        super().__init__(name)
        self.payload = Base(name)

    def instantiate_classes(self):
        """Instantiate home automation objects."""
        self.add(VisualCrossing())

    @classmethod
    def register(cls):
        app_name = "myhome"
        MasterPiece.app_name(app_name)
        MasterPiece.set_log(Log(app_name))
        Application.load_class_attributes()


def main():
    MyHomeApp.load_plugins()
    MyHomeApp.parse_args()
    app = MyHomeApp()
    app.run()


if __name__ == "__main__":
    main()
