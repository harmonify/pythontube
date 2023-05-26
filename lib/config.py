from __future__ import annotations

import json
import os

from .decorator import singleton


@singleton
class Config:
    """
    The config class for pythontube.

    Attributes:
    - name: the config file name (default: pythontube)
    - __location__: the root path of the project
    - file_path: the config file path (defaulting to `name` attribute in the
                 project root directory)
    - data: the data of the config file

    Methods:
    - read_config(): read the config file and return the config dict
    - initialize_config(): initialize the config file and return the config dict
    """

    def __init__(self, file_name: str = "pythontube") -> None:
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__), '..'))

        self.file_name = file_name

        # file_path: the path of the config file (defaulting to pythontube.json
        # in the project root directory)
        self.file_path = os.path.join(
            self.__location__, self.file_name).removesuffix(".json") + ".json"

        if getattr(self, 'data', None) is None:
            self.data = self.read_config()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name={self.file_name}>"

    def read_config(self) -> dict[str, str]:
        """ Read the config file and return the data. """
        try:
            print(f"Reading {self.file_path}")
            if os.path.isdir(self.file_path):
                raise FileNotFoundError(
                    f"{self.file_path} is a directory, not a file")
            elif os.path.isfile(self.file_path):
                print(f"{self.file_path} is a file")
                with open(self.file_path, "r") as f:
                    data = json.loads(f.read())
            else:
                print(f"{self.file_path} does not exist")
                data = self.initialize_config()
            print("Done")
            return data
        except FileNotFoundError as e:
            print(e)
            exit(1)
        except json.JSONDecodeError:
            print(f"{self.file_path} is not a valid JSON file")
            exit(1)

    def initialize_config(self) -> dict[str, str]:
        """ Initialize the config file and return the data. """
        print(f"Initializing {self.file_name}")
        # constants
        data = {
            "app": self.file_name,
            "version": "1.0",
        }

        # user input
        data["output_dir_path"] = self._input_output_dir_path()

        # write config
        with open(self.file_path, "w") as f:
            f.write(json.dumps(data))
        print(f"{self.file_path} is created")
        return data

    def _input_output_dir_path(self) -> str:
        """
        Input the output directory path.

        Returns:
        The output directory path.
        """
        while True:
            print(
                "\nEnter the output directory path (e.g. /home/user/pythontube-output)")
            print("Default: '<script-location>/pythontube-output/'")
            output_dir = input(": ") or os.path.join(
                self.__location__, "pythontube-output")

            # check if user specify a relative path or absolute path
            if os.path.isabs(output_dir):
                output_dir_path = os.path.realpath(output_dir)
            else:
                output_dir_path = os.path.realpath(
                    os.path.join(os.getcwd(), *output_dir.split("/")))

            if not os.path.isdir(output_dir_path):
                print(f"{output_dir_path} is not a directory")
                if input("Create directory (y/n)? ") == "y":
                    os.makedirs(output_dir_path)
                    print(f"{output_dir_path} is created")
                    break
            else:
                print(f"\n{output_dir_path} is a directory")
                if input("Is this the right path (y/n)? ") == "y":
                    break
        return output_dir_path


def main(args=None):
    try:
        config = Config("pythontube")
        print("==========================")
        print(config.initialize_config())
        print("==========================\n")

        print("==========================")
        print(config.read_config())
        print("==========================\n")
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == '__main__':
    main()
