class Maxes(object):
	def __init__(self, squat_max, dl_max, bench_max, ohp_max):
		self.squat_max = squat_max
		self.dl_max = dl_max
		self.bench_max = bench_max
		self.ohp_max = ohp_max

		
#Estimate a 1 rep max for the user
def maxEstimate(workout):
	print "This will estimate your 1rm based on your max weight and reps"
	
	#Get the weight and reps from the user
	weight = raw_input("Enter in the max " + workout + " weight: ")
	int_weight = int(weight)
	reps = raw_input("Enter in the max " + workout + " reps: ")
	int_reps = int(reps)
	
	#use formula from wendler to get the one rep max estimate
	realMax = int_weight*int_reps*.0333+int_weight
	
	trainingMax = realMax*.9
	return trainingMax

#Print out a weekly schedule
def weekNumbers(squat, dl, bench, ohp):
	#workoutWeight = roundNumbers(workoutMax)
	
	#List for all of the workout names
	workouts = ["Over Head Press", "Deadlift", "Bench", "Squat"]
	#Dictionary with all of the workout totals
	workoutTotals = {"Over Head Press":ohp, "Deadlift":dl, "Bench":bench, "Squat":squat}
	
	weekNumber = 1
	setPercent = .65
	setWeeklyMultiplier = 0.00
	setPercentMultiplier = 0.00
	
	#iterate through the weeks, printing the weights and rep counts
	while weekNumber < 4:
		print "\nWeek " + str(weekNumber)
		
		#set a tuple to the set numbers based on the week number
		if weekNumber == 1:
			setNumbers = '5','5','5+'
		elif weekNumber == 2:
			setNumbers = '3','3','3+'
		elif weekNumber == 3:
			setNumbers = '5','3','1+'
		
		setPercent += setWeeklyMultiplier
		
		#iterate through all of the workouts and their totals in the list
		for workout in workouts:
			print workout
			workoutSets(workoutTotals[workout], setPercent, setPercentMultiplier, setNumbers)
		#reset the percentMultiplier for the next set
		setPercentMultiplier = 0.00
		#Increase the weekly multiplier
		setWeeklyMultiplier = 0.05
		weekNumber += 1


#calculate and print the workout totals	
def workoutSets(weight, setPercent, setPercentMultiplier, setNumbers):
	
	setCounter = 1
	
	while setCounter < 4:
			
		print str(roundNumbers(weight*(setPercent+setPercentMultiplier))) + " x "+setNumbers[setCounter-1]+" reps"
		#print setPercent+setPercentMultiplier
		setCounter += 1
		setPercentMultiplier += .10
	
#Take a number, round it up to the nearest multiple of five
def roundNumbers(weightNumber):
	remainder = weightNumber%5
	
	newWeight = weightNumber - remainder + 5
	"""
	if remainder > 3:
		newWeight = weightNumber - remainder + 5
	else:
		newWeight = weightNumber - remainder
	"""
	return newWeight
	
"""
#calculate the training max based on Wendler's 90% rule
def wendlerMax(max):
	trainingMax = max*.9
	return trainingMax
"""

def main():

	workoutMaxes = Maxes(maxEstimate("squat"), maxEstimate("deadlift"), maxEstimate("bench"), maxEstimate("overhead press"))
	
	print "Your squat training max is: " + str(workoutMaxes.squat_max)
	print "Your deadlift training max is: " + str(workoutMaxes.dl_max)
	print "Your bench training max is: " + str(workoutMaxes.bench_max)
	print "Your overhead press training max is: " + str(workoutMaxes.ohp_max)
	
	weekNumbers(workoutMaxes.squat_max, workoutMaxes.dl_max, workoutMaxes.bench_max, workoutMaxes.ohp_max)
	
	"""
	realMax = realMaxEstimate()
	trainingMax = wendlerMax(realMax)
	
	squat = Maxes(trainingMax)	
	print "Your real 1rm is: " + str(realMax)
	print "Your training max is: "+ str(squat.squat_max)
	"""
	
	


	
if __name__ == '__main__':
        main()