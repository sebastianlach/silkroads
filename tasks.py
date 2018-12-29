from logging import getLogger

from invoke import task


logger = getLogger(__name__)


@task
def tests(context, coverage=True, pycodestyle=True, verbose=True):
    """Run test suit."""
    logger.info("Running test suit")
    context.run("pip install -q -r tests/requirements.txt")
    context.run("nosetests -v {coverage}".format(
        coverage=("--with-coverage" if coverage else "")
    ))
    context.run("pycodestyle --benchmark")


@task
def docs(context, docs=False):
    """Generate documentation."""
    logger.info("Building documentation {}".format(docs))


@task
def clean(context, git=False):
    """Clean up ignored files and caches."""
    logger.info("Cleaning cache files")
    context.run("find . -type f -name \"*.py[co]\" -delete")
    context.run("find . -type d -name \"__pycache__\" -exec rm -r {} +")
    if git:
        context.run("git clean -f -d")  # remove directories
        context.run("git clean -f -X")  # remove ignored files


@task
def setup(context):
    """Setuop application."""
    logger.info("Setting up application")
    context.run("virtualenv venv")
    context.run("source venv/bin/activate")
    context.run("pip install -r requirements.txt")
    context.run("pip install -e .")


@task
def migrate(context):
    """Migrate application database."""
    context.run("python manage.py migrate")
