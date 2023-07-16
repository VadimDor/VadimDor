#!/usr/bin/env python
# pylint: disable=invalid-name

# Start of script

"""
BUILD_INFO.py
Build information file for this project
"""

# pylint: enable=invalid-name

# 
def english_build_info():
    '''This file has not yet been tested'''
    print('Build information')
    print('For: VadimDor/VadimDor')
    language_list = [
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
    print('\nLanguages: ' + str(language_list))
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

"""
Problems
Language name inputs are not translated to the correct language
Exit function is not translated to a non-English language
The program may not yet be functional yet
Translations are needed for all languages except for English
List is out of order
Not all intended languages are supported yet
"""
def main():
    ''' Language selector '''
    lang_input1 = str(input('Lang🌐 >> '))
    lang_input1 == lang_input1.upper()
    if lang_input1 == ('EN' or 'ENGLISH'):
        return english_build_info()
        # break
    if lang_input1 in ('ES' , 'SPANISH'):
        return spanish_build_info()
        # break
    else:
        print('That language is not available')
        no_more = input('❌')
        print('Goodbye')
    return ""

if __name__ == '__main__':
    main()

# This project uses ISO 639-1 language codes
# End of script
