from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        data = toml.loads(content)
        toml_data = data["tool"]["poetry"]

        name = toml_data.get("name")
        description = toml_data.get("description", "")
        dependencies = list(toml_data.get("dependencies", {}).keys())
        dev_dependencies = list(toml_data.get("development dependencies", {}).keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
