#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('post_gen_project')


def move_files(src, dest):
    logger.info('Moving files from {} to {}'.format(src, dest))

    for f in os.listdir(src):
        shutil.move(os.path.join(src, f), dest)

    shutil.rmtree(src)

move_files('pkg_files', '{{cookiecutter.package_name|replace(":","/")}}')
