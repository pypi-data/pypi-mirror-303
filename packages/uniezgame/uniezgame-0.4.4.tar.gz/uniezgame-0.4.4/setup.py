from setuptools import setup, Extension, find_packages
import os
import pybind11

# Ścieżki do SDL2
SDL2_INCLUDE_DIR = r'D:\dev\SDL2\include'
SDL2_LIB_DIR = r'D:\dev\SDL2\lib\x64'

module_name = 'uniezgame'

# Tworzenie rozszerzenia
unigame_module = Extension(
    module_name,
    sources=['uniezgame/mylib.cpp'],  # Upewnij się, że ścieżka do pliku źródłowego jest poprawna
    include_dirs=[SDL2_INCLUDE_DIR, pybind11.get_include()],
    library_dirs=[SDL2_LIB_DIR],
    libraries=['SDL2', 'SDL2main'],
)

if __name__ == "__main__":
    setup(
        name=module_name,
        version='0.4.4',
        description='Uniezgame - Python C++ bindings using pybind11',
        ext_modules=[unigame_module],
        include_package_data=True,
        package_data={module_name: ['*.pyd', 'SDL2.dll', 'uniezgame.dll']},  # Include DLLs and .pyd file
        zip_safe=False,
        author='Michał Lewandowski',
        author_email='michal.lewandowski.113@gmail.com',
        url='https://github.com/slawek1q2w3e4r/uniezgame',
        license='MIT',
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.6',
        packages=find_packages(),  # Dodaj to do znalezienia pakietów
    )
