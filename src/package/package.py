import json

class Package:
    def __init__(self, package_type:str, package_data:str) -> None:
        self.package_type = package_type
        self.package_data = package_data
        self.package_json = json.dumps({"package_type": package_type, "package_data": package_data})

    @staticmethod
    def from_json(data:str):
        data_dict = json.loads(data)
        return Package(data_dict["package_type"], data_dict["package_data"])