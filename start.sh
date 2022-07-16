echo "Cloning Repo"
git clone https://github.com/DarkLord-99/LuciferMoringstar-Robot.git /LuciferMoringstar-Robot
cd /LuciferMoringstar-Robot
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot..."
python3 bot.py

