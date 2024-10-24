import catalogue
import confection
from confection import Config


class registry(confection.registry):
    components = catalogue.create("fasr", "components", entry_points=True)
    layers = catalogue.create("fasr", "layers", entry_points=True)

    @classmethod
    def create(cls, registry_name: str, entry_points: bool = False) -> None:
        """Create a new custom registry."""
        if hasattr(cls, registry_name):
            raise ValueError(f"Registry '{registry_name}' already exists")
        reg = catalogue.create("fasr", registry_name, entry_points=entry_points)
        setattr(cls, registry_name, reg)


__all__ = ["Config", "registry"]
