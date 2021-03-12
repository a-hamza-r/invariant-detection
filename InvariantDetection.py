import sys;
import re;
from itertools import combinations;
from os.path import join;

states = [];
values = [];
invariants = set();

def getValuesFunc(funcScope, valuesCurrentFile, statesCurrentFile):
	valuesAtInstant = dict();
	x = 0;
	while True:
		if funcScope[x] == "":
			statesCurrentFile.append(valuesAtInstant);
			return (valuesCurrentFile, statesCurrentFile);
		if funcScope[x] not in valuesCurrentFile:
			valuesCurrentFile[funcScope[x]] = [];
		valuesCurrentFile[funcScope[x]].append(float(funcScope[x+1]));
		valuesAtInstant[funcScope[x]] = float(funcScope[x+1]);
		x += 3;


def parseFunction(funcScope):
	foundStart = False;
	valuesCurrentFile = dict();
	statesCurrentFile = [];
	for x in range(len(funcScope)):
		if not foundStart and funcScope[x].endswith('ENTER'):
			funcInfo = list(filter(None, re.split('[\.:\(\)]+', funcScope[x])));
			start = x+4;
			foundStart = True;
		if foundStart and funcInfo[0] in funcScope[x] and 'EXIT' in funcScope[x]:
			funcScope = funcScope[start:x-1];
			break;

	while len(funcScope) > 0:
		funcStart = funcScope[0];
		funcInfo = list(filter(None, re.split('[\.:\(\)]+', funcStart)));
		endFunc = [x for x in range(len(funcScope)) if funcInfo[0] in funcScope[x] and 'EXIT' in funcScope[x]][0];
		while endFunc < len(funcScope):
			#print(funcScope[endFunc]);
			if funcScope[endFunc] == "":
				#print(funcScope);	
				break;
			endFunc += 1;
		valuesCurrentFile, statesCurrentFile = getValuesFunc(funcScope[3:endFunc], valuesCurrentFile, statesCurrentFile);
		funcScope = funcScope[endFunc+1:];
	
	values.append(valuesCurrentFile);
	states.append(statesCurrentFile);


def checkSingleAlwaysSame(var):
	varValues = [];
	sameValues = True;
	for run in range(len(values)):
		sameValues = sameValues and values[run][var].count(values[run][var][0]) == len(values[run][var]);
		varValues.append(values[run][var][0]);
		if sameValues == False:
			return sameValues;
	if varValues.count(varValues[0]) != len(varValues):
		return False;
	
	invariants.add("{} == {}".format(var, varValues[0]));
	return sameValues;

def checkSingleSign(var):
	alwaysNonNeg = True;
	alwaysNonPos = True;
	for run in range(len(values)):
		alwaysNonNeg = alwaysNonNeg and all(elem >= 0 for elem in values[run][var]);
		alwaysNonPos = alwaysNonPos and all(elem <= 0 for elem in values[run][var]);
	if alwaysNonNeg:
		invariants.add("{} >= 0.0".format(var));
	elif alwaysNonPos:
		invariants.add("{} <= 0.0".format(var));

def checkSingleRange(var):
	maxFinal = values[0][var][0];
	minFinal = values[0][var][0];
	for run in range(len(values)):
		maxVal = max(values[run][var]);
		minVal = min(values[run][var]);
		if maxFinal < maxVal:
			maxFinal = maxVal;
		if minFinal > minVal:
			minFinal = minVal;
	invariants.add("{} <= {}".format(var, maxFinal));
	invariants.add("{} >= {}".format(var, minFinal));

def checkSingleFewValues(var):
	varValues = set();
	for run in range(len(values)):
		varValues |= set(values[run][var]);
	
	if len(varValues) <= 5:
		ors = " || ";
		inv = ors.join("{} == {}".format(var, s) for s in varValues);
		invariants.add(inv);
		return True;

	return False;

def checkMultipleRelations(varPair):
	alwaysLessFirst = True;
	alwaysLessSecond = True;
	alwaysLessEqualFirst = True;
	alwaysLessEqualSecond = True;
	alwaysEqual = True;
	for run in range(len(states)):
		for x in states[run]:
			if varPair[0] in x and varPair[1] in x:
				alwaysLessFirst = alwaysLessFirst and x[varPair[0]] < x[varPair[1]];
				alwaysLessSecond = alwaysLessSecond and x[varPair[1]] < x[varPair[0]];
				alwaysLessEqualFirst = alwaysLessEqualFirst and x[varPair[0]] <= x[varPair[1]];
				alwaysLessEqualSecond = alwaysLessEqualSecond and x[varPair[1]] <= x[varPair[0]];
				alwaysEqual = alwaysEqual and x[varPair[0]] == x[varPair[1]]
	
	if alwaysEqual:
		invariants.add("{} == {}".format(varPair[0], varPair[1]));
	elif alwaysLessFirst:
		invariants.add("{} < {}".format(varPair[0], varPair[1]));
	elif alwaysLessSecond:
		invariants.add("{} < {}".format(varPair[1], varPair[0]));
	elif alwaysLessEqualFirst:
		invariants.add("{} <= {}".format(varPair[0], varPair[1]));
	elif alwaysLessEqualSecond:
		invariants.add("{} <= {}".format(varPair[1], varPair[0]));


def findInvariants():
	# select only common variables in all runs of program
	variables = set(values[0]);
	for x in range(len(values)-1):
		variables = variables & set(values[x+1]);
	
	# single variable checks
	for var in variables:
		# if values of single variable always remains same
		sameValues = checkSingleAlwaysSame(var);

		# if values of a variable are only a set of values (<= 5) 
		checkSingleFewValues(var);

		# check for the range of values for the variable
		checkSingleRange(var);

		# check if the variable is either non-negative or non-positive
		checkSingleSign(var);

	# multiple variable checks
	for varPair in combinations(variables, 2):
		# check if any variable is less, less equal or equal to the other variable
		checkMultipleRelations(varPair);

def main(cmdLineArgs):
	daikonOutputDir = "daikon-output";
	if len(cmdLineArgs) <= 2:
		print("Usage: python3 parseDtrace.py benchmark_name num_of_traces");
		print("benchmark_name : name of the benchmark to run. look from directory names");
		print("")
		print("num_of_traces : number of traces you want to use for the algorithm");
		print("exiting...");
		exit(1);
	
	benchmarkName = cmdLineArgs[1];
	tracesDir = join(benchmarkName, daikonOutputDir);
	numTraces = int(cmdLineArgs[2]);
	if numTraces > 20:
		numTraces = 20;
	if numTraces < 1:
		numTraces = 1;


	# Parse the traces	
	files = ["{}{}.dtrace".format(join(tracesDir, benchmarkName), x+1) for x in range(numTraces)];
	for file in files:
		with open(file, 'r') as f:
			lines = [line.strip() for line in f];
		for x in range(len(lines)):
			if lines[x].endswith('ENTER'):
				parseFunction(lines[x:]);
				break;
	
	# Dump trace information to trace.txt file in the respective benchmark directory 
	with open(join(benchmarkName, "traces.txt"), "w+") as f:
		for traceNum in range(len(states)):
			f.write("TRACE #{}".format(traceNum+1) + "\n");
			f.write("--------------------------\n");
			for x in states[traceNum]:
				f.write(str(x)+"\n");
			f.write("\n\n");

		
	# Find invariants for the programs
	findInvariants();
	print("Invariants found:");
	print(invariants);
	assertions = ["assert({})".format(x) for x in invariants];
	
	# Output the found assertions to assertions.txt file in respective benchmark directory
	with open(join(benchmarkName, "assertions.txt"), "w+") as f:
		for assertt in assertions:
			f.write(assertt + "\n");

if __name__ == '__main__':
	main(sys.argv);
