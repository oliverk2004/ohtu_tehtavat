from project_reader import ProjectReader


def main():
    url = "https://raw.githubusercontent.com/oliverk2004/ohtu_tehtavat/main/osa2/project-reader/pyproject.toml"
    reader = ProjectReader(url)
    print(reader.get_project())


if __name__ == "__main__":
    main()
