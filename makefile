default: setup

setup: setup.py
	python2 setup.py build_ext --inplace

clean:
	rm -rf *.c *.so *-prog.py *.dot *.svg *.pyc
