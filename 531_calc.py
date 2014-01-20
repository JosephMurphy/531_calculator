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
	
def weekNumbers(workoutMax, workout):
	#workoutWeight = roundNumbers(workoutMax)
	print "Week 1"
	print str(workout) + ":"
	print str(roundNumbers(workoutMax*.65)) + " x 5 reps" 
	print str(roundNumbers(workoutMax*.75)) + " x 5 reps"
	print str(roundNumbers(workoutMax*.85)) + " x 5+ reps"

def roundNumbers(weightNumber):
	remainder = weightNumber%5
	
	if remainder > 3:
		newWeight = weightNumber - remainder + 5
	else:
		newWeight = weightNumber - remainder
	
	print weightNumber
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
	
	weekNumbers(workoutMaxes.squat_max, "Squat")
	
	"""
	realMax = realMaxEstimate()
	trainingMax = wendlerMax(realMax)
	
	squat = Maxes(trainingMax)	
	print "Your real 1rm is: " + str(realMax)
	print "Your training max is: "+ str(squat.squat_max)
	"""
	
	


	
if __name__ == '__main__':
        main()