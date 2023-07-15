#!/usr/bin/env python
# pylint: disable=invalid-name
# Start of script
"""
BUILD_INFO.py
Build information file for this project
"""

# pylint: enable=invalid-name
# This file has not yet been tested
def englishBuildInfo():
    print('Build information')
    print('For: VadimDor/VadimDor')
    languageList = [
        'Python',
        'HTML5',
        'SHell',
        'CSV',
        'Makefile',
        'TeX/BibTeX',
        'INI',
        'Desktop',
        'JSON',
        'YAML',
        'Markdown',
        'Plain Text',
    ]
    print('\nLanguages: ' + str(languageList))
    print('\nPython version: 3.6 and up')
    print('BASH SHell verson: 5.0 and up (older versions may still work perfectly fine)')
    print(
        'Comma Seperated Value version: Any (recommended programs: LibreOffice' \
              'Calc, Kate, Notepad++, Gedit, any other text editor)'
    )
    print('Makefile (GNU Make) version: Unknown')
    print('LaTeX/BiBTeX version: 2.0 or higher')
    print('INI version: Windows 95 or newer')
    print('KDE Desktop file version: 1.0 or newer')
    print('JSON file version: 2001 or newer')
    print('Markdown version: 1.0 or newer')
    print('Plain text version: Any')
    print(
        '\nThese languages are in use for this project, and need to be installed to view the full project.'
    )
    print('\nEnd of info')


def spanish_build_info():
    # Coming soon
    """
    print("Build information")
    print("For: VadimDor/VadimDor")
    languageList = ["Python", "HTML5", "SHell", "CSV", "Makefile", 
        "TeX/BibTeX", "INI", "Desktop", "JSON", "YAML", "Markdown", "Plain Text"]
    print("\nLanguages: " + str(languageList))
    print("\nPython version: 3.6 and up")
    print("BASH SHell verson: 5.0 and up (older versions may still work perfectly fine)")
    print("Comma Seperated Value version: Any (recommended programs: "\
    "LibreOffice Calc, Kate, Notepad++, Gedit, any other text editor)")
    print("Makefile (GNU Make) version: Unknown")
    print("LaTeX/BiBTeX version: 2.0 or higher")
    print("INI version: Windows 95 or newer")
    print("KDE Desktop file version: 1.0 or newer")
    print("JSON file version: 2001 or newer")
    print("Markdown version: 1.0 or newer")
    print("Plain text version: Any")
    print("\nThese languages are in use for this project, "\
        "and need to be installed to view the full project.")
    print("\nEnd of info")
    """


def main():
    # Language selector
    langInput1 = str(input('Lang🌐 >> '))
    langInput1 == langInput1.upper()
    if langInput1 == 'EN' or 'ENGLISH':
        return englishBuildInfo()
        # break
    elif langInput1 == 'ES' or 'SPANISH':
        return spanish_build_info()
        # break
    else:
        print('That language is not available')
        noMore = input('❌')
        print('Goodbye')


if __name__ == '__main__':
    main()
"""
Problems
Language name inputs are not translated to the correct language
Exit function is not translated to a non-English language
The program may not yet be functional yet
Translations are needed for all languages except for English
List is out of order
Not all intended languages are supported yet
"""
# This project uses ISO 639-1 language codes
# End of script
