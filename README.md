# extract-wiki

A simple tool to extract wiki articles, clean and save them in a single large .txt file.

## Install

Clone this repo. 
```bash
git clone https://github.com/mtreviso/extractwiki.git
```

Automatically create a Python virtualenv and install all dependencies 
using `pipenv install`. And then activate the virtualenv with `pipenv shell`:
```sh
pip install pipenv
pipenv install
pipenv shell
```

If it is taking too long to install all dependencies, add `--skip-lock` flag for `pipenv install`.


## Steps

1. Download wiki dump:

    You can always download the lastest dump from wikipedia [here](https://dumps.wikimedia.org/ptwiki/latest/). 
    For other languages, just replace the short prefix in `ptwiki` in the URL, such as `enwiki` for english.
    
    ```bash
    wget -c https://dumps.wikimedia.org/ptwiki/latest/ptwiki-latest-pages-articles.xml.bz2
    ```

2. Extract articles in a text format from bz2 file:
    
    ```bash
    git clone https://github.com/attardi/wikiextractor.git
    cd wikiextractor/
    python3 WikiExtractor.py ../ptwiki-latest-pages-articles.xml.bz2 -o ../ptwiki-in-parts -b 
    ```
 
3. Apply preprocessing methods to clean the articles:
    
    - And combine them in a single large file:
    ```bash
    python3 clean_corpus.py ptwiki-in-parts/ -o ptwiki.txt --merge
    ```
    
    - Or save them in a different directory: 
    ```bash
    python3 clean_corpus.py ptwiki-in-parts/ -o ptwiki-in-parts-cleaned/
    ```



## Args

```bash
usage: clean_corpus.py input [-h] [-o OUTPUT] [-m]

positional arguments:
  input                 Path to an input directory containing dirs of
                        extracted articles

optional arguments:
  -h, --help            Show this help message and exit
  -o, --output OUTPUT   Path to an output directory or path to a single file
  -m, --merge           Whether to merge all files in a single txt file
```

If an output path is not provided, the script will overwrite the original extracted files.