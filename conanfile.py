# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import shutil

from conans import ConanFile
from conans.tools import download, unzip


class GslConan(ConanFile):
    """Donwload GSL from github and copy to include."""

    name = 'gsl'
    url = 'https://github.com/anonymouzz/conan-gsl'
    license = "MIT"
    version = '2016-01-04'

    revision = 'fb1a89fb14b0af0caf47f6afeb1ec800abc4b551'

    def source(self):
        """Download sources."""
        zip_name = '{}.zip'.format(self.revision)
        download(
            'https://github.com/Microsoft/GSL/archive/{}'.format(zip_name),
            zip_name
        )
        unzip(zip_name)
        shutil.move('GSL-{}'.format(self.revision), 'gsl')
        os.unlink(zip_name)

    def package(self):
        """Copy headers to include."""
        self.copy(pattern='*', src='gsl/gsl/', dst='include/gsl/')
