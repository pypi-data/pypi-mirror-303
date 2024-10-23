"""
Copies files from source folder to output folder preserving the path.
Example:

.. enclosed::

    demo.pdf
    images/test.png
"""

from pathlib import Path
import shutil
from sphinx.util.docutils import SphinxDirective

from sphinx.util import logging

logger = logging.getLogger(__name__)


class EnclosedDirective(SphinxDirective):
    has_content = True

    def run(self):
        for num, filename in enumerate(self.content, start=0):
            rst_folder = Path(self.content.info(num)[0]).parent
            sub_folder = rst_folder.relative_to(self.env.app.srcdir)

            source = rst_folder.joinpath(filename)
            target = Path(self.env.app.builder.outdir).joinpath(sub_folder, filename)

            if not source.is_file():
                logger.warning(
                    '%s:%d: file "%s" does not exist'
                    % (
                        self.content.info(num)[0],
                        self.content.info(num)[1] + 1,
                        filename,
                    )
                )
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
        return []
