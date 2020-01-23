cd ..
yes | rm -r Space_X_Information
ask clone --skill-id amzn1.ask.skill.d5aa471d-de4e-4f11-8ea4-486a9184bcc5
echo "[Staging changes ready for git capture]"
cd Space_X_Information
cp -r * ../SER
cd ../SER
echo "[Git tracking initiated]"
git add *
echo "[Git tracking complete]"
git status

