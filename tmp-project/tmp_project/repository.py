from dagster import load_assets_from_package_module, repository

from tmp_project import assets
from .jobs.hello_job import hello_job, my_directory_sensor

@repository
def tmp_project():
    return [load_assets_from_package_module(assets), hello_job, my_directory_sensor]
