# -*- python -*-
#
#       Copyright INRIA - CIRAD - INRA
#
#       File author(s):
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
# ==============================================================================
"""
"""
# ==============================================================================
from setuptools import setup, find_packages
# ==============================================================================

pkg_root_dir = 'src'
packages = [pkg for pkg in find_packages(pkg_root_dir)]
top_pkgs = [pkg for pkg in packages if len(pkg.split('.')) <= 2]
package_dir = dict([('', pkg_root_dir)] +
                   [(pkg, pkg_root_dir + "/" + pkg.replace('.', '/'))
                    for pkg in top_pkgs])

setup(
    name="vberry",
    version="0.0.1",
    description="",
    long_description="",

    author="* Phillipe Vivin\n",

    maintainer="Christian Fournier",
    maintainer_email="christian.fournier@inrae.fr",

    license="Cecill-C",
    keywords='',

    # package installation
    packages=packages,
    package_dir=package_dir,
    zip_safe=False,

    # See MANIFEST.in
    include_package_data=True,
    )
