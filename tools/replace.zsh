
python3 utter.py > utterances.txt

cp ../README.md X
sed -e '/##DONOTREMOVE##/ {' -e 'r utterances.txt'  -e 'd' -e '}'  X > README.md 
rm X
