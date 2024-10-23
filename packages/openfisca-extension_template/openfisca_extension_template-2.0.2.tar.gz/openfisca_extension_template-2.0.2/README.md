# OpenFisca Extension-Template

This repository is here to help you bootstrap your own OpenFisca
[extension](http://openfisca.org/doc/contribute/extensions.html) package.

**You should NOT fork it** but follow the set up instructions below.

> Otherwise, you will have to clean up all tags when you deploy your own
> extension package.

## Setting up your Extension Package

This set of instructions **only needs to be followed once** and will create
your own copy of this boilerplate directory, customising it to the country you
want to work on. You will need to have [Git](https://git-scm.com) installed.

### Using GitHub (recommended for GitHub users)

1. Click on the
   [“Use this template” dropdown and select “Create a new repository”](https://github.com/new?template_name=extension-template&template_owner=openfisca).

2. Set the repository name to `openfisca-<your_city_name>`; use underscore `_`
   as separator if there are spaces in the city name. For example,
   `openfisca-ile_d-yeu` or `openfisca-valparaiso`.

3. After being redirected to your newly created repository, please allow a few
   minutes for the automatic setup to be executed. Once done, the title of the
   README file should be updated to `OpenFisca <your_city_name>`.

> If the automatic setup does not start within a few minutes, you can initiate
> it manually:
>
> - Navigate to the “Actions” tab.
> - Select the “First time setup” workflow.
> - Click on “Run workflow” to start the setup process manually.

4. Follow the instructions in the new repository's README.md.

### Manual setup (recommended for users of other Git hosts)

1. [Download a copy](https://github.com/openfisca/extension-template/archive/master.zip)
   of this repository, unzip it and `cd` into it in a Terminal window.

2. Create a new repository on your favourite git host (Bitbucket, GitLab, …)
   with the name `openfisca-<your_city_name>`. For example,
   `openfisca-vina_del_mar` or `openfisca-paris`.

3. Execute the `first-time-setup.sh` script to initialise the git repository.
   This performs numerous tasks including replacing all references to
   `openfisca-extension_template` with references to the new extension package.

   - To execute the script run `bash first-time-setup.sh` from the command line
   - After the `first-time-setup.sh` has run both it and these instructions are
     removed.

4. Follow the instructions in the new repository's `README.md.`

## Writing the Legislation

The city or jurisdiction whose law is modelled here has a very simple tax and
benefit system.

- It has a child allowance that only applies to your city.

This and other elements are described in different folders. All the modelling
happens within the `src/openfisca_<my_city>` folder.

- The rates are in the `parameters` folder.
- The formulas are in the `variables` folder.

The files that are outside from the `src/openfisca_<my_city>` folder are used
to set up the development environment.

## Packaging your Extension Package for Distribution

City packages are Python distributions. You can choose to distribute your
package automatically via the predefined continuous deployment system on GitHub
Actions, or manually.

### Automatic continuous deployment on GitHub

This repository is configured with a continuous deployment system to automate
the distribution of your package via `pip`.

#### Setting up continuous deployment

To activate the continuous deployment:

1. Create an account on [PyPI](https://pypi.org/) if you don't already have
   one.
2. Generate a token in your PyPI account. This token will allow GitHub Actions
   to securely upload new versions of your package to PyPI.
3. Add this token to your GitHub repository's secrets under the name
   `PYPI_TOKEN`.

Once set up, changes to the `main` branch will trigger an automated workflow to
build and publish your package to PyPI, making it available for `pip`
installation.

### Manual distribution

If you prefer to manually manage the release and distribution of your package,
follow the guidelines provided by the
[Python Packaging Authority](https://python-packaging-user-guide.readthedocs.io/tutorials/distributing-packages/#packaging-your-project).

This involves detailed steps on preparing your package, creating distribution
files, and uploading them to PyPI.

## Install Instructions for Users and Contributors

This package requires
[Python 3.9](https://www.python.org/downloads/release/python-390/). More recent
versions should work, but are not tested.

All platforms that can execute Python are supported, which includes GNU/Linux,
macOS and Microsoft Windows.

### Setting-up a Virtual Environment with venv

In order to limit dependency conflicts, we recommend using a
[virtual environment](https://www.python.org/dev/peps/pep-0405/) with
[venv](https://docs.python.org/3/library/venv.html).

- A [venv](https://docs.python.org/3/library/venv.html) is a project specific
  environment created to suit the needs of the project you are working on.

To create a virtual environment, launch a terminal on your computer, `cd` into
your directory and follow these instructions:

```sh
python3 -m venv .venv # create a new virtual environment in the “.venv” folder, which will contain all dependencies
source .venv/bin/activate # activate the venv
```

You can now operate in the venv you just created.

You can deactivate that venv at any time with `deactivate`.

:tada: You are now ready to install this OpenFisca Extension Package!

Two install procedures are available. Pick procedure A or B below depending on
how you plan to use this Extension Package.

### A. Minimal Installation (Pip Install)

Follow this installation if you wish to:

- run calculations on a large population;
- create tax & benefits simulations;
- serve your Extension Package with the OpenFisca Web API.

For more advanced uses, head to the
[Advanced Installation](#advanced-installation-git-clone).

#### Install this Extension Package with Pip Install

Inside your venv, check the prerequisites:

```sh
python --version  # should print at least "Python 3.9.xx".
```

```sh
pip --version  # should print at least 9.0.
# if not, run "pip install --upgrade pip"
```

Install the Extension Package:

```sh
pip install openfisca-<my_city>
```

:warning: Please beware that installing the Extension Package with `pip` is
dependent on its maintainers publishing said package.

:tada: This OpenFisca Extension Package is now installed and ready!

#### Next Steps

- To learn how to use OpenFisca, follow our
  [tutorials](https://openfisca.org/doc/).
- To serve this Extension Package, serve the
  [OpenFisca Web API](#serve-your-country-package-with-the-openFisca-web-api).

Depending on what you want to do with OpenFisca, you may want to install yet
other packages in your venv:

- To write on top of this Extension Package, head to the
  [Extensions documentation](https://openfisca.org/doc/contribute/extensions.html).
- To plot simulation results, try [matplotlib](http://matplotlib.org/).
- To manage data, check out [polars](https://pola.rs/).

### B. Advanced Installation (Git Clone)

Follow this tutorial if you wish to:

- create or change this Extension Package's legislation;
- contribute to the source code.

#### Clone this Extension Package with Git

First, make sure [Git](https://www.git-scm.com/) is installed on your machine.

Set your working directory to the location where you want this OpenFisca
Extension Package cloned.

> We recommend you to use an [isolated](https://pypi.org/project/pipx/)
> environment manager to manage build and extension dependencies separately:

```sh
pipx install poetry
```

`Poetry` will automatically manage a virtual environment for you. Nonetheless,
if you need to have more control over your dependencies, we recommend you to
use a [virtualenv](https://github.com/pyenv/pyenv-virtualenv):

```sh
poetry config settings.virtualenvs.create false
pyenv install 3.9.xx
pyenv virtualenv 3.9.xx openfisca
```

Clone this Extension Package on your machine:

```sh
git clone https://example.com/repository.git
cd repository_folder
```

Inside your venv, check the prerequisites:

```sh
pyenv local openfisca
python --version  # should print "Python 3.9.xx".
poetry install --all-extras --sync
```

You can make sure that everything is working by running the provided tests with
`poetry run openfisca test --country-package=openfisca_country_template --extensions=openfisca_extension_template tests/openfisca_extension_template`.

> [Learn more about tests](https://openfisca.org/doc/coding-the-legislation/writing_yaml_tests.html)

:tada: This OpenFisca Extension Package is now installed and ready!

#### Cleanup (optional)

To completely clean up your environment, run:

```sh
poetry env remove --all
pip freeze | grep -v "^-e" | sed "s/@.*//" | xargs pip uninstall -y
```

This will remove all pip package from current environment and remove all Poetry
environment in OpenFisca Extension-Template.

#### Next Steps

- To write new legislation, read the
  [Coding the legislation](https://openfisca.org/doc/coding-the-legislation/index.html)
  section to know how to write legislation.
- To contribute to the code, read our
  [Contribution Guidebook](https://openfisca.org/doc/contribute/index.html).

### C. Contributing

Follow this tutorial if you wish to:

- contribute to the source code.

_Note: This tutorial assumes you have already followed the instructions laid
out in section [B. Advanced Installation](#b-advanced-installation-git-clone)._

In order to ensure all published versions of this template work as expected,
new contributions are tested in an isolated manner on Github Actions.

Follow these steps to set up an isolated environment for testing your
contributions as Github Actions does.

#### Set up an isolated environment

First, make sur [Tox](https://tox.wiki/en/4.23.0/) is installed on your
machine.

We recommend using [pipx](<(https://pypi.org/project/pipx/)>) to install `tox`,
to avoid mixing isolated-testing dependencies testing with `virtualenv`.

```sh
pipx install tox
```

#### Testing your contribution in an isolated environment

You can make sure that your contributions will work as expected by running:

```sh
tox
```

You can also run these in parallel:

```sh
tox -p
```

:tada: Your contribution to OpenFisca Extension Package is now ready for prime
time!

#### Next Steps

- Open a pull request to the `main` branch of this repository.
- Announce your changes as described in [CONTRIBUTING](CONTRIBUTING.md).

## Serve this Extension Package with the OpenFisca Web API

If you are considering building a web application, you can use the packaged
OpenFisca Web API with your Extension Package.

To serve the Openfisca Web API locally, run:

```sh
openfisca serve --port 5000 --country-package openfisca_country_template --extensions openfisca_<my_city>
```

Or use the quick-start `task` command:

```
task serve
```

To read more about the `openfisca serve` command, check out its
[documentation](https://openfisca.org/doc/openfisca-python-api/openfisca_serve.html).

You can make sure that your instance of the API is working by requesting:

```sh
curl "http://localhost:5000/spec"
```

This endpoint returns the [Open API specification](https://www.openapis.org/)
of your API.

:tada: This OpenFisca Extension Package is now served by the OpenFisca Web API!
To learn more, go to the
[OpenFisca Web API documentation](https://openfisca.org/doc/openfisca-web-api/index.html).
