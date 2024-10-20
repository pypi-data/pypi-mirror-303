from masterpiece.core import Application
from juham.base.base import Base


class JApp(Application):
    """Juham home automation application base class. Registers new plugin group 'juham'."""

    def __init__(self, name: str) -> None:
        """Creates home automation application with the given name.
        If --enable_plugins is False create hard coded configuration
        by calling instantiate_classes() method.

        Args:
            name (str): name for the application
        """
        super().__init__(name, Base(name))

    def instantiate_classes(self) -> None:
        """Instantiates the default set of classes for the application.
        Subclasses are responsible for implementing this method.
        It serves as a fallback mechanism when the application is started for the first time
        and no configuration file named after the application is present.
        """

    def serialize(self):
        try:
            with open(f"{self.name}.json", "r", encoding="utf-8") as f:
                self.deserialize_from_json(f)
        except FileNotFoundError:
            self.warning(
                f'No "{self.name}.json" found, creating built-in configuration'
            )
            self.instantiate_classes()
            with open(f"{self.name}.json", "w", encoding="utf-8") as f:
                self.serialize_to_json(f)
            self.info(
                f"{self.name}.json and class specific configuration files created in ~/.{self.name}/ folder. Edit and restart"
            )
            exit(2)
        except Exception as e:
            self.error(f"Exception {e} occurred while reading {self.name}.json")
            exit(1)

    @classmethod
    def register(cls):
        Application.register_plugin_group("juham")
