#!/bin/zsh

# A Script to generate the final README file including the utterances.

# There is only one parameter:

#  -D : display suspicious utterances
#  -V : display version information

# Work out how to determine if a -V flag is in the args, and just execute the python programme and nowt else.
CVERSION="0.1.0.20200228"
WVERSION="0.1.0.20200228"

if [[ "$*" == "-V"  ]]
then
	echo "Controller: V$CVERSION"
	echo "Worker:     V$WVERSION"
	exit
fi
PID=$$

# Generate utterances from the model
python3 utter.py $1 $2 $3 $4 $5  > utterances.tmp

# Relocate README.md file to local directory for processing
cp ../README.md $PID

# Replace the placeholder in the README.md file with the formatted content of the utterances
sed -e '/##DONOTREMOVE##/ {' -e 'r utterances.tmp' -e 'd' -e '}' $PID > ../README.md

# Remove the interim working file
rm $PID
rm utterances.tmp
