from setuptools import setup, find_packages
import os
import sys
import shutil
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        self.post_install()

    def post_install(self):
        """Platforma özgü yükleme işlemleri."""
        if sys.platform.startswith('linux'):
            self.install_desktop_file_linux()  # Linux için masaüstü dosyası
            self.install_icon_linux()           # Linux için simge yükleme
        elif sys.platform == 'darwin':
            self.install_icon_mac()             # macOS için simge yükleme
        elif sys.platform == 'win32':
            self.install_icon_windows()          # Windows için simge yükleme

    def install_desktop_file_linux(self):
        """Linux için masaüstü dosyasını yükle."""
        desktop_src = os.path.join(os.path.dirname(__file__), 'resources', 'desktop', 'crl-browser.desktop')
        desktop_dest_dir = os.path.expanduser('/usr/local/share/applications/')
        desktop_dest = os.path.join(desktop_dest_dir, 'crl-browser.desktop')
        os.makedirs(desktop_dest_dir, exist_ok=True)
        shutil.copy(desktop_src, desktop_dest)
        os.chmod(desktop_dest, 0o755)
        print(f".desktop file installed to {desktop_dest}")

    def install_icon_linux(self):
        """Linux için simgeyi yükle."""
        icon_src = os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'crl-browser.png')
        icon_dest_dir = os.path.expanduser('/usr/local/share/icons/hicolor/256x256/apps/')
        os.makedirs(icon_dest_dir, exist_ok=True)
        shutil.copy(icon_src, os.path.join(icon_dest_dir, 'crl_browser.png'))
        print(f"Icon installed to {icon_dest_dir}")

    def install_icon_mac(self):
        """macOS için simgeyi yükle."""
        icon_src = os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'crl_browser.png')
        app_bundle = os.path.join(os.path.dirname(__file__), 'dist', 'crl-browser.app', 'Contents', 'Resources', 'crl_browser.png')
        os.makedirs(os.path.dirname(app_bundle), exist_ok=True)
        shutil.copy(icon_src, app_bundle)
        print(f"macOS icon installed to {app_bundle}")

    def install_icon_windows(self):
        """Windows için simgeyi yükle."""
        icon_src = os.path.join(os.path.dirname(__file__), 'resources', 'icons', 'crl_browser.png')
        icon_dest_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'crl-browser', 'crl_browser.png')
        os.makedirs(os.path.dirname(icon_dest_dir), exist_ok=True)
        shutil.copy(icon_src, icon_dest_dir)
        print(f"Icon installed to {icon_dest_dir}")

# README.md dosyasını oku
def read_readme():
    """README.md dosyasının içeriğini oku."""
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

setup(
    name='crl-advanced',
    version='1.5',
    description='Pyqt6 based browser',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='Zaman',
    author_email='zamanhuseynli23@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyQt6',
        'PyQt6-WebEngine',
    ],
    entry_points={
        'console_scripts': [
            'crl-browser=crl_browser.crl_browser:main',
        ],
    },
    cmdclass={
        'install': PostInstallCommand,
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
