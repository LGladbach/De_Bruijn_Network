import json

from src.package.package import Package


class LinearizePackage(Package):
    def __init__(self, address:tuple[str, int], position:float):
        self.address = address[0]
        self.port = address[1]
        self.position = position

        super().__init__("linearize",
                         json.dumps({"address": self.address, "port": self.port, "position": self.position}))

    @staticmethod
    def from_json(data:str):
        sup_package = Package.from_json(data)
        data_dict = json.loads(sup_package.package_data)
        return LinearizePackage((data_dict["address"], data_dict["port"]), data_dict["position"])