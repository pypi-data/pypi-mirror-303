import logging
import pkg_resources

from fastapi import FastAPI
from leximpact_dotations_back.configure_logging import formatter


# configure _root_ logger
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)
handler = logging.StreamHandler()
logger.handlers[0].setFormatter(formatter)
logger.addHandler(handler)


app = FastAPI()


@app.get("/")
def read_root():
    return {
        "INFO":
        "Bienvenue sur le service d'API web de leximpact-dotations-back ! Pour en savoir plus, consulter la page /docs"
    }


@app.get("/dependencies")
def read_dependencies():
    # limit to a specific list of packages
    selected_dependencies = [
        "OpenFisca-Core", "OpenFisca-France-Dotations-Locales", "numpy", "fastapi"]
    # get the distribution objects for all installed packages
    dists = pkg_resources.working_set
    # extract the names and versions of the packages
    packages_info = {}
    for d in dists:
        dependency_name = d.project_name
        if dependency_name in selected_dependencies:
            packages_info[d.project_name] = d.version
    return packages_info
