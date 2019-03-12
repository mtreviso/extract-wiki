# extract-wiki

A simple tool to extract wiki articles, clean and save them in a single large .txt file.

Filter the output of [WikiExtractor.py](https://github.com/attardi/wikiextractor) to strip html tags,
remove newline marks, and keep only valid sentences. For example:

```
<doc id="220" url="https://pt.wikipedia.org/wiki?curid=220" title="Astronomia">
Astronomia

Astronomia é uma ciência natural que estuda corpos celestes (como estrelas, planetas, cometas, nebulosas, aglomerados de estrelas, galáxias) e fenômenos que se originam fora da atmosfera da Terra (como a radiação cósmica de fundo em micro-ondas). Preocupada com a evolução, a física, a química e o movimento de objetos celestes, bem como a formação e o desenvolvimento do universo.

A astronomia é uma das mais antigas ciências.
...
</doc>
```

Will be transformed to:

```
Astronomia
Astronomia é uma ciência natural que estuda corpos celestes (como estrelas, planetas, cometas, nebulosas, aglomerados de estrelas, galáxias) e fenômenos que se originam fora da atmosfera da Terra (como a radiação cósmica de fundo em micro-ondas). Preocupada com a evolução, a física, a química e o movimento de objetos celestes, bem como a formação e o desenvolvimento do universo.
A astronomia é uma das mais antigas ciências.
...
```
 


## Install

Clone this repo:
```bash
git clone https://github.com/mtreviso/extract-wiki.git
```

Install the only dependency (`selectolax`), which is used to safely strip HTML tagsy:
```
pip install selectolax
```


## Usage

Just run `clean_corpus.py` script by following these steps:

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
    python3 WikiExtractor.py ../ptwiki-latest-pages-articles.xml.bz2 -o ../ptwiki-in-parts
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
  -w, --min-nb-words    Min number of words in a sentence. Default: 1   
```

If an output path is not provided, the script will overwrite the original extracted files.
