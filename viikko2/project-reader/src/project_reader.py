from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = toml.loads(content)

        project_name = data.get('tool').get('poetry').get('name')
        project_description = data.get('tool').get('poetry').get('description')
        project_license = data.get('tool').get('poetry').get('license')
        authors = data.get('tool').get('poetry').get('authors')
        dependendies = data.get('tool').get('poetry').get('dependencies')
        dev_dependencies = data.get('tool').get('poetry').get('group').get('dev').get('dependencies')

        return Project(project_name, project_description, project_license, authors, dependendies, dev_dependencies)

