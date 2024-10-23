import importlib
from typing import List
import click
import sys
import importlib.metadata
import logging
from .configuration import Configuration
from .utils import check_last_masterdac
from packaging.version import parse as parse_version

logging.basicConfig(level=logging.INFO)

original_args = [arg for arg in sys.argv]


@click.group()
def main():
    pass


@main.group()
def courses():
    """Permet de gérer la liste des cours suivis"""
    pass


@click.argument("courses", type=click.Choice(["amal", "rld", "rital"]), nargs=-1)
@courses.command("add")
def courses_add(courses: List[str]):
    """Ajout de cours"""
    configuration = Configuration()
    configuration.courses.update(courses)
    configuration.save()


@click.argument("courses", type=click.Choice(["amal", "rld", "rital"]), nargs=-1)
@courses.command("rm")
def courses_rm(courses: List[str]):
    """Enlever un cours"""
    configuration = Configuration()
    for course in courses:
        configuration.courses.remove(course)
    configuration.save()


@courses.command("list")
def courses_list():
    """Liste des cours"""
    for course in Configuration().courses:
        print(course)  # noqa: T201


@click.option("--no-self-update", is_flag=True)
@main.command()
def update(no_self_update: bool):
    """Mettre à jour l'ensemble des modules pour les cours suivis"""
    if not no_self_update:
        check_last_masterdac(original_args)

    # Check that package are installed

    configuration = Configuration()
    install = importlib.import_module("master_dac.install")

    processed = set()
    for course in configuration.courses:
        getattr(install, course)(processed)

    print(  # noqa: T201
        "Don't forget to download the datasets with `master-dac download-datasets`"
    )


@main.command()
def download_datasets():
    """Mettre à jour l'ensemble des jeux de données pour les cours suivis"""
    configuration = Configuration()
    install = importlib.import_module("master_dac.datasets")

    for course in configuration.courses:
        getattr(install, course, lambda *args: None)()


@main.group()
def rld():
    """Commandes spécifiques au module RLD"""
    pass


@click.option("--hide", is_flag=True)
@click.option("--interactive", is_flag=True, help="Interactive mode to inspect states")
@click.option(
    "--num-karts",
    type=int,
    help="Number of karts (must be greater than number of zip files)",
)
@click.argument("file_or_modules", type=str, nargs=-1)
@rld.command("stk-race")
def rld_stk_race(hide, num_karts, file_or_modules, interactive):
    """Race"""
    check_last_masterdac(original_args)

    version = parse_version(importlib.metadata.version("pystk2_gymnasium"))
    assert version >= parse_version("0.6.0") and version < parse_version(
        "0.7.0"
    ), f"Expected pytstk2-gymnasium version 0.6.*, got {version}. Please update."

    from master_dac.rld.stk import race

    race(hide, num_karts, file_or_modules, interactive=interactive)
