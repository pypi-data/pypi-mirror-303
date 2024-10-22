from pathlib import Path
import argparse
import yaml

from .model import Model


class ModelCollection:
    def __init__(self) -> None:
        self.models: dict = {}

    def upload_item(self, name, location):
        self.models[name].upload(location)

    def load(self, spec_path):
        with open(spec_path, "r", encoding="utf-8") as f:
            spec_content = yaml.safe_load(f)

        for spec_entry in spec_content:
            name = spec_entry["name"]
            location = spec_entry["location"]
            host_name = location["host"]
            host_location = location["path"]
            self.models[name] = Model(name, host_name, host_name, host_location)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--action", type=str)
    parser.add_argument("--model", type=str)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--location", type=Path)

    args = parser.parse_args()

    models = ModelCollection()
    models.load(args.config)

    if args.action == "upload":
        models.upload_item(args.model, args.location)
