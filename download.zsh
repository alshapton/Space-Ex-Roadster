cd ..
yes | rm -r Space_X_Information
ask clone --skill-id amzn1.ask.skill.6d22b908-9fdd-458b-b0db-33141641aad1
echo "[Staging changes ready for git capture]"
cd Space_X_Information
cp -r * ../SER
cd ../SER
echo "[Git tracking initiated]"
git add *
echo "[Git tracking complete]"
git status
