# Meson build file for pymt_topography.
project('pymt_topography', version: '0.2.dev0')

py = import('python').find_installation(pure: false)

# Files get copied to <python directory>/site-packages/<subdir>
install_pkg_srcs = [
    meson.project_name() / '__init__.py',
    meson.project_name() / 'bmi.py',
]
py.install_sources(
    install_pkg_srcs,
    subdir: meson.project_name(),
)

install_subdir(
    'meta/Topography',
    install_dir: py.get_install_dir() / meson.project_name() / 'data',
)

# This is a temporary fix for editable installs.
run_command('cp', '-r', meson.project_name() / 'data', 'build')
