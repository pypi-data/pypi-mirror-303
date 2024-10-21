

import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
name="PySimpleGUI",
version="5.0.7",
author="PySimpleSoft Inc.",
install_requires=["rsa"],
description="Python GUIs for Humans! PySimpleGUI is the top-rated Python application development environment. Launched in 2018 and actively developed, maintained, and supported in 2024. Transforms tkinter, Qt, WxPython, and Remi into a simple, intuitive, and fun experience for both hobbyists and expert users.",
long_description=readme(),
long_description_content_type="text/markdown",
license='Proprietary',
keywords="GUI UI tkinter Qt WxPython Remi wrapper simple easy beginner novice student graphics",
url="https://www.PySimpleGUI.com",
packages=setuptools.find_packages(),
python_requires=">=3.6",
classifiers=[
"Intended Audience :: Developers",
"License :: Other/Proprietary License",
"Operating System :: OS Independent",
"Framework :: PySimpleGUI",
"Framework :: PySimpleGUI :: 5",
"Programming Language :: Python :: 3",
"Programming Language :: Python :: 3.6",
"Programming Language :: Python :: 3.7",
"Programming Language :: Python :: 3.8",
"Programming Language :: Python :: 3.9",
"Programming Language :: Python :: 3.10",
"Programming Language :: Python :: 3.11",
"Programming Language :: Python :: 3.12",
"Programming Language :: Python :: 3.13",
"Topic :: Multimedia :: Graphics",
],
package_data={"": 
["CONTRIBUTING.md","LICENSE.txt","README.md"]
        },
entry_points={'gui_scripts': [
"psgmain=PySimpleGUI.PySimpleGUI:_main_entry_point",
"psghome=PySimpleGUI.PySimpleGUI:_main_entry_point",
"psgupgrade=PySimpleGUI.PySimpleGUI:_upgrade_entry_point",
"psghelp=PySimpleGUI.PySimpleGUI:main_sdk_help",
"psgwatermarkon=PySimpleGUI.PySimpleGUI:main_watermark_on",
"psgwatermarkoff=PySimpleGUI.PySimpleGUI:main_watermark_off",
"psgver=PySimpleGUI.PySimpleGUI:main_get_debug_data",
    ]
    },
)

