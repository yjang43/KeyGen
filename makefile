create:
	python pickling_posts.py
	python key_generator.py

restart:
	rm *.pickle
	python pickling_posts.py
	python key_generator.py

input:
	python thread_control.py

clean:
	rm *.pickle
