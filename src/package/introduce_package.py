import json

from src.package.package import Package


class IntroducePackage(Package):
    def __init__(self, rl:bool):
        self.rl = rl
        super().__init__("introduce", json.dumps({"rl": self.rl}))

    @staticmethod
    def from_json(data:str):
        sup_package = Package.from_json(data)
        data_dict = json.loads(sup_package.package_data)
        return IntroducePackage(data_dict["rl"])