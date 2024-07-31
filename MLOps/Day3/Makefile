#docker Makefile in docker container
init:
	pip install -U pip
	pip install pandas scikit-learn joblib

dependency:
	make -C ../Day2-project/ server

dependency-clean:
	make -C ../Day2-project/ server-clean