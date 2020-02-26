
#!/bin/zsh

# A Script to generate the final README file including the utterances.

# There are NO parameters.

PID=$$

# Generate utterances from the model
python3 utter.py > utterances.$PID

# Relocate READMe.md file to local directory for processing
cp ../README.md $PID

sed -e '/##DONOTREMOVE##/ {' -e 'r utterances.$PID' -e 'd' -e '}' $PID
# Replace the placeholder in the README.md file with the formatted content of the utterances

# Remove the interim working file
#rm $PID
#rm utterances.$PID
