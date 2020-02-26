
#!/bin/zsh

# A Script to generate the final README file including the utterances.

# There are NO parameters.

PID=$$

# Generate utterances from the model
python3 utter.py > utterances.tmp

# Relocate READMe.md file to local directory for processing
cp ../README.md $PID

# Replace the placeholder in the README.md file with the formatted content of the utterances
sed -e '/##DONOTREMOVE##/ {' -e 'r utterances.tmp' -e 'd' -e '}' $PID > ../README.md

# Remove the interim working file
rm $PID
rm utterances.tmp
