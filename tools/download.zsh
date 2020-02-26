#!/bin/zsh

# A Script to download the Alexa Skill and prepare it for a git upload

# There are NO parameters.

#ID of the skill
SKILL=amzn1.ask.skill.d5aa471d-de4e-4f11-8ea4-486a9184bcc5

cd ../..

echo "[Starting to clone AWS Skill]"
ask clone --skill-id $SKILL

echo "[Staging changes ready for git capture]"
cd Space_X_Information
cp -r * ../SER
cd ../SER

echo "[Git tracking initiated]"
git add *

echo "[Git tracking complete]"
git status

echo "[Cleaning up.....]"
cd ..
yes | rm -r Space_X_Information

echo "[Completed downloading]"

