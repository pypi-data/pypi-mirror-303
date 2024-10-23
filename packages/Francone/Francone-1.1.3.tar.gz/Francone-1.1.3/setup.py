from setuptools import setup, find_packages

setup(
    name="Francone",            # Nome del pacchetto su PyPI
    version="1.1.3",                # Versione del pacchetto
    packages=find_packages(),       # Trova automaticamente tutti i moduli
    install_requires=[              # Dipendenze
        "nptdms",                   # Libreria per leggere file TDMS
        "matplotlib",               # Libreria per i grafici
        "pandas",                    # Libreria per la gestione dei dati
        "numpy"
    ],
    author="Franco De Angelis",
    author_email="fd23111991@gmail.com",
    description="Libreria per gestire TDMS e grafici",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuo_username/Francone",  # URL del progetto (es. GitHub)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
