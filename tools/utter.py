#!/usr/local/bin python3

# include standard modules
import argparse
import json


def initParser():
	# initiate the parser
	parser = argparse.ArgumentParser()
	parser.add_argument("-D", "--display", help="Show suspicious utterances", action="store_true")
	parser.add_argument("-V", "--version", help="Display version information", action="store_true")

	# read arguments from the command line
	args = parser.parse_args()
	return args
	

def get_model(model):
	with open('../models/' + model) as json_file:
		return json.load(json_file)

def get_pysource(req_source):
	modules = []

	with open(req_source,'rt') as pysource:
		for line in pysource:
			if ("#@" in line):
				modules.append(line)

	completes="{"
	for module in modules:
		imp_start=module.find("import")
		r=' '.join(module[imp_start+7:].split())+'\n'
		completes=completes + "\"" + r.split(" #@ ")[0].replace("Handler","") + "\":\"" + r.split(" #@ ")[1][0:-1] +"\","
	completes=completes[0:-1] + "}"
	return json.loads(completes)


# Begin main program


args=initParser()


# check for --display or -D
show_suspicious=False
if args.display:
	show_suspicious=True

model=get_model('en-GB.json')
cintents = get_pysource('../lambda/lambda_function.py')

intents=model["interactionModel"]["languageModel"]["intents"]
for intent in  intents:
	if (intent["samples"] != []):
		# Skip any AMAZON built-in intents for now
		if (intent["name"].startswith('AMAZON')):
			continue
		
		print ("\n")
		
		if (cintents[intent["name"]]):
			print(cintents[intent["name"]] + "\n")
		for sample in intent["samples"]:
			# Flag any "space ex" occurrances
			if ("space ex" not in sample.lower()):
				pass
			else:
				if show_suspicious:
					print("*\t" + sample + "\n")
				continue
			# Flag any "sxi" occurrences
			if ("sxi" not in sample.lower()):
				pass
			else:
				if show_suspicious:
					print("+\t" + sample + "\n")
				continue
				
			print("\t" + sample + "\n")
		x=str(intent["slots"])
		if (x!="[]"):
			print(x)
		#if (str(intent["slots"]) != "[]"): 
		#	pass
		#else:
		#print("\t"+str(intent["slots"])+"\n")
