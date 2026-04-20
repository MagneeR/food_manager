cd food_manager
python -m venv .venv
source \.venv\Scripts\Activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
export REFLEX_LOGLEVEL=default
reflex init
# Add my backend api url 
#REFLEX_API_URL=https://api.moure.dev reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate