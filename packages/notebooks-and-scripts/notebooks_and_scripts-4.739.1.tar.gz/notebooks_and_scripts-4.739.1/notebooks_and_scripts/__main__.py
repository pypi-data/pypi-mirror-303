from blueness.argparse.generic import main

from notebooks_and_scripts import NAME, VERSION, DESCRIPTION, ICON, README
from notebooks_and_scripts.logger import logger

main(
    ICON=ICON,
    NAME=NAME,
    DESCRIPTION=DESCRIPTION,
    VERSION=VERSION,
    main_filename=__file__,
    tasks={
        "build_README": lambda _: README.build(),
    },
    logger=logger,
)
