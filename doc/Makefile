tracefmt.pdf : tracefmt.tex
	@@for ITERATIONS in `seq 3` ; do   \
            pdflatex ${<}           ;      \
          done

all      : tracefmt.pdf

clean    :
	@rm -f $(addprefix tracefmt, .aux .log)

spotless : clean
	@rm -f $(addprefix tracefmt,      .pdf)

