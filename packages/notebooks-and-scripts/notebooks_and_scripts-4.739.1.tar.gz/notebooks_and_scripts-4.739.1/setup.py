from notebooks_and_scripts import NAME, VERSION, DESCRIPTION, REPO_NAME
from blueness.pypi import setup


setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.aws_batch",
        f"{NAME}.sagemaker",
        f"{NAME}.workflow",
        f"{NAME}.workflow.patterns",
        f"{NAME}.workflow.runners",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            "sample.env",
            ".abcli/**/*.sh",
            "assets/*.ipynb",
        ],
    },
)
