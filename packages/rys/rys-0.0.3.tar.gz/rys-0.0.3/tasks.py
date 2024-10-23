from pathlib import Path

from invoke import task
from jinja2 import Template

system = "rys"        # Directory name of the project
main_branch = "main"  # The release branch on origin
dev_branch = "dev"    # The main development branch on origin

project_template = """
[build-system]
requires = ["flit_core >=3.9,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "{{ system }}"
authors = [
    {name = "Arkadiusz Michał Ryś", email = "Arkadiusz.Michal.Rys@gmail.com"},
]
readme = "README.rst"
requires-python = ">={{ minimum_version }}"
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "Natural Language :: English",
]
dynamic = ["version", "description"]
license = {file = "LICENSE"}
keywords = [""]
dependencies = [
{%- for dependency in requirements.rys %}
    "{{ dependency }}",
{%- endfor %}
]

[project.optional-dependencies]
test = [
{%- for dependency in requirements.test %}
    "{{ dependency }}",
{%- endfor %}
]
doc = [
{%- for dependency in requirements.doc %}
    "{{ dependency }}",
{%- endfor %}
]
dev = [
{%- for dependency in requirements.dev %}
    "{{ dependency }}",
{%- endfor %}
]

[project.urls]
source = "https://git.rys.one/arrys/rys"
"""


@task
def lint(c):
    """"""
    c.run(f"python3 -m black {system}")
    c.run(f"python3 -m pylint {system}")


@task(name="docs")
def documentation(c):
    """Build the documentation."""
    c.run("python3 -m sphinx docs docs/build/html")


@task(name="preview", aliases=("rst",))
def preview(c):
    """Show a preview of the README file."""
    import sys
    rst_view = c.run(f"restview --listen=8888 --browser --pypi-strict README.rst", asynchronous=True, out_stream=sys.stdout)
    print("Listening on http://localhost:8888/")
    rst_view.join()


@task
def clean(c):
    """Remove all artefacts."""
    patterns = ["build", "docs/build"]
    for pattern in patterns:
        c.run(f"rm -rf {pattern}")


@task
def test(c):
    """Run all tests under the tests directory."""
    print(type(c))
    #c.run("python3 -m pytest")


@task
def coverage(c):
    """Run coverage from the 'tests' directory."""
    c.run("python3 -m coverage erase")
    c.run("python3 -m coverage run --source . -m unittest discover tests 'test_*' -v")
    c.run("python3 -m coverage report -m")
    c.run("python3 -m coverage html")


@task
def minimum(c):
    """Check the minimum required python version for the project."""
    c.run("vermin --no-parse-comments .")


@task(name="migrate")
def migrate_requirements(c):
    """Copy requirements from the requirements.txt file to pyproject.toml."""
    lines = Path("requirements.txt").read_text().split("\n")
    current = system.lower().replace("-", "_")
    requirements = {current: [], "test": [], "doc": [], "graphical": [], "dev": []}
    for line in lines:
        if line.startswith("#"):
            candidate = line[1:].lower().strip().replace(" ", "_").replace("-", "_")
            if candidate in requirements.keys():
                current = candidate
                continue
        if line.strip() == "" or ("=" in line and "#" in line):
            continue
        versioned_package = line.split("#")[0].split()
        requirements[current].append("".join(versioned_package))
    import vermin
    config = vermin.Config()
    source_file_paths = list(set(vermin.detect_paths([system, "tests", "docs"], config=config)))
    minimums, *_ = vermin.Processor().process(source_file_paths, config, config.processes())
    minimum_version = vermin.version_strings(list(filter(lambda ver: ver, minimums)))
    Path("pyproject.toml").write_text(
        Template(project_template[1:]).render(requirements=requirements, system=system, minimum_version=minimum_version)
    )


@task
def release(c, version):
    """"""
    if version not in ["minor", "major", "patch"]:
        print("Version can be either major, minor or patch.")
        return

    migrate_requirements(c)

    import importlib
    current_module = importlib.import_module(system)
    __version_info__ = current_module.__version_info__
    __version__ = current_module.__version__
    _major, _minor, _patch = __version_info__

    if version == "patch":
        _patch = _patch + 1
    elif version == "minor":
        _minor = _minor + 1
        _patch = 0
    elif version == "major":
        _major = _major + 1
        _minor = 0
        _patch = 0

    c.run(f"git checkout -b release-{_major}.{_minor}.{_patch} {dev_branch}")
    c.run(f"sed -i 's/{__version__}/{_major}.{_minor}.{_patch}/g' {system}/__init__.py")
    print(f"Update the readme for version {_major}.{_minor}.{_patch}.")
    input("Press enter when ready.")
    c.run(f"git add -u")
    c.run(f'git commit -m "Update changelog version {_major}.{_minor}.{_patch}"')
    c.run(f"git push --set-upstream origin release-{_major}.{_minor}.{_patch}")
    c.run(f"git checkout {main_branch}")
    c.run(f"git pull")
    c.run(f"git merge --no-ff release-{_major}.{_minor}.{_patch}")
    c.run(f'git tag -a {_major}.{_minor}.{_patch} -m "Release {_major}.{_minor}.{_patch}"')
    c.run(f"git push")
    c.run(f"git checkout {dev_branch}")
    c.run(f"git merge --no-ff release-{_major}.{_minor}.{_patch}")
    c.run(f"git push")
    c.run(f"git branch -d release-{_major}.{_minor}.{_patch}")
    c.run(f"git push origin --tags")
