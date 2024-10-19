# ozi/spec/meson.build
# Part of the OZI Project.
# See LICENSE.txt for license information.
# SPDX-License-Identifier: Unlicense
config_files = [
    '__init__.py',
    '__init__.pyi',
    '_license.py',
    '_license.pyi',
    '_spec.py',
    '_spec.pyi',
    'base.py',
    'base.pyi',
    'ci.py',
    'ci.pyi',
    'pkg.py',
    'pkg.pyi',
    'project.py',
    'project.pyi',
    'python.py',
    'python.pyi',
    'src.py',
    'src.pyi',
    'py.typed',
]
foreach file: config_files
    if not meson.is_subproject() or get_option('install-subprojects').enabled()
        python.install_sources(file, subdir: 'ozi_spec')
    endif
    fs.copyfile(file)
endforeach
if false
    executable('source_child_spec', config_files)
endif
