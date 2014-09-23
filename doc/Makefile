SHELL := /bin/bash

tracefmt.pdf : tracefmt.tex
	@@for ITERATIONS in `seq 3` ; do   \
            pdflatex ${<}           ;      \
          done

all      : tracefmt.pdf

clean    :
	@rm -f tracefmt.{aux,bbl,blg,log}

spotless : clean
	@rm -f tracefmt.pdf

