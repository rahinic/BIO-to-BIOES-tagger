# BIO-to-BIOES NER Tagging Scheme

_this work is adapted from the repo github.com/taasmoe/BIO-to-BIOLU.  

The [CoNLL 2003 NER dataset](http://www.aclweb.org/anthology/W03-0419) is annotated using the BIO labeling scheme. Each word is labelled in accordance with its location relative to a named entity (NE), using the three following markers:

* **B-**   for the first token of a chunk phrase/NE, 
* **I-**   for tokens inside chunk phrase/NE's, 
* **O-**   for tokens outside/other any chunk phrase/NE. 
* **E-**   for the end tokens of chunk phrase/NE's, 
* **S-**   for unit/single length chunk phrase/NE's.

This Python script converts a BIO-encoded file to BIOES.

## Usage
Run the following in the command line, where you specify the path of the original BIO encoded file and the name of your converted file.

```shell
python bioes_encode.py ConLL2003-test.txt ConLL2003-bioes-test.txt
```

Tested for Python 3.6.

## Examples
_ConLL2003-bioes-test.txt_ is the result when converting _ConLL2003-test.txt_
