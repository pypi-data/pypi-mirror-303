from setuptools import setup, find_namespace_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="perun.proxygui",
    python_requires=">=3.9",
    url="https://gitlab.ics.muni.cz/perun/perun-proxyidp/proxyidp-gui.git",
    description="Module with GUI and API for Perun ProxyIdP",
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_namespace_packages(include=["perun.*"]),
    install_requires=[
        "Authlib==1.3.0",
        "setuptools",
        "PyYAML==6.0.1",
        "Flask==2.3.3",
        "Flask-pyoidc==3.14.3",
        "Flask-Babel==3.1.0",
        "perun.connector==3.8.1",
        "python-smail==0.9.0",
        "SQLAlchemy==2.0.29",
        "pymongo~=4.6",
        "validators==0.28.1",
        "idpyoidc==2.1.0",
        "python-dateutil==2.9.0",
        "Jinja2==3.1.3",
        "requests==2.31.0",
        "Flask-Session[mongodb]~=0.8",
        "pysaml2==7.4.2",
        "cryptojwt==1.8.3",
        "user-agents==2.2.0",
        "flask-smorest==0.42.3",
        "marshmallow==3.21.1",
        "deepdiff==6.7.1",
    ],
    extras_require={
        "postgresql": ["psycopg2-binary==2.9.9", "Flask-session[sqlalchemy]~=0.8"],
    },
)
