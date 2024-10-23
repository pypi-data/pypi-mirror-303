include document.mk
TEMPORARY_DIR=tmp
RELEASE_BUILD_DIR=${TEMPORARY_DIR}/release
DEBUG_BUILD_DIR=${TEMPORARY_DIR}/debug
VERBOSE_BUILD_DIR=${TEMPORARY_DIR}/verbose

COMMON_FLAGS=-bibtex -lualatex -interaction=nonstopmode -logfilewarnings- -shell-escape -gg -cd -makeindexfudge-
all: release

.SILENT: release debug

release:	${DOCTITLE}.tex
	mkdir -p ${RELEASE_BUILD_DIR}
	latexmk -outdir=${RELEASE_BUILD_DIR} -auxdir=${RELEASE_BUILD_DIR} \
		-quiet ${COMMON_FLAGS}	${DOCTITLE}.tex > /dev/null
	cp ${RELEASE_BUILD_DIR}/${DOCTITLE}.pdf ${DOCTITLE}.pdf

debug:	${DOCTITLE}.tex
	mkdir -p ${DEBUG_BUILD_DIR}
	latexmk -outdir=${DEBUG_BUILD_DIR} -auxdir=${DEBUG_BUILD_DIR} \
		-quiet ${COMMON_FLAGS}	${DOCTITLE}.tex
	cp ${DEBUG_BUILD_DIR}/${DOCTITLE}.pdf ${DOCTITLE}.pdf

verbose:	${DOCTITLE}.tex
	mkdir -p ${VERBOSE_BUILD_DIR}
	latexmk -outdir=${VERBOSE_BUILD_DIR} -auxdir=${VERBOSE_BUILD_DIR} \
		-verbose ${COMMON_FLAGS}	${DOCTITLE}.tex
	cp ${VERBOSE_BUILD_DIR}/${DOCTITLE}.pdf ${DOCTITLE}.pdf

clean:
	rm ${DOCTITLE}.pdf

