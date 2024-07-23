main:
	pip3 install -r requirements.txt
	nohup python3 src/bot.py &

clean:
	pkill -f "python3 src/bot.py"
	find . -name "__pycache__" -type d -exec rm -r {} +
	
