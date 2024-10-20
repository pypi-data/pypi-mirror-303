#!/usr/bin/env python3
import setuptools
from pathlib import Path

try:
    import docutils.core
    from docutils.writers import manpage
except ImportError:
    docutils = None
    manpage = None


def compile_documentation():
    if docutils is None or manpage is None:
        return

    dst = Path('pter/docs')
    dst.mkdir(exist_ok=True)
    docpath = Path('doc')
    
    Path('man').mkdir(exist_ok=True)

    for fn in ['pter.rst', 'qpter.rst', 'pter.config.rst']:
        fn = docpath / fn
        if not fn.is_file():
            continue
        dstfn = str(dst / (fn.stem + '.html'))
        docutils.core.publish_file(source_path=str(fn),
                                   destination_path=dstfn,
                                   writer_name='html')

        if fn.stem == 'pter.config':
            docutils.core.publish_file(source_path=str(fn),
                                       destination_path='man/pter.config.5',
                                       writer_name='manpage')
        elif fn.stem in ['pter', 'qpter']:
            docutils.core.publish_file(source_path=str(fn),
                                       destination_path='man/' + fn.stem + '.1',
                                       writer_name='manpage')


if __name__ == '__main__':
    compile_documentation()
    setuptools.setup()
