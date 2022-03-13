import time

def countdownTimer():
	no_of_secs = int(input('How many seconds for timer?: '))
	while no_of_secs:
		if no_of_secs < 60:
			# calculate the number of hours, minutes and seconds
			hrs = no_of_secs // 3600
			mins = no_of_secs // 60
			secs = no_of_secs % 60
			timer = '%02d:%02d:%02d' %(hrs, mins, secs)
			print(timer, end='\r')
			time.sleep(1)
			no_of_secs -= 1
		elif 60 <= no_of_secs < 3600:
			hrs = no_of_secs // 3600
			mins = no_of_secs // 60
			secs = no_of_secs % 60
			timer = '%02d:%02d:%02d' %(hrs, mins, secs)
			print(timer, end='\r')
			time.sleep(1)
			no_of_secs -= 1
		elif 3600 <= no_of_secs <= 86400:
			hrs = no_of_secs // 3600
			mins = (no_of_secs % 3600) // 60
			secs = (no_of_secs % 3600) % 60
			timer = '%02d:%02d:%02d' %(hrs, mins, secs)
			print(timer, end='\r')
			time.sleep(1)
			no_of_secs -= 1
	print('Time Up!')

countdownTimer()
