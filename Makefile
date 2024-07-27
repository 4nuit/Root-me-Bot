main:
	nohup python3 bot.py &

clean:
	rm -f nohup.out
	find . -name "__pycache__" -type d -exec rm -r {} +
	pkill -f "python3 bot.py"
