from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="tmp_project",
        packages=find_packages(exclude=["tmp_project_tests"]),
        install_requires=[
            "dagster",
        ],
        extras_require={"dev": ["dagit", "pytest"]},
    )
