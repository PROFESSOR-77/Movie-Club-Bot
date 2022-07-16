echo "Cloning Repo"
git clone https://github.com/PROFESSOR-77/LuciferMoringstar-Robot.git /LuciferMoringstar-Robot
cd /LuciferMoringstar-Robot
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot..."
python3 bot.py

