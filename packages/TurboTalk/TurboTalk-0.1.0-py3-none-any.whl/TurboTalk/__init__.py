# R_AI/__init__.py

# Default values
bot_name = "Champ AI"
company_name = "Rango Productions"

def set_bot_name(name):
    global bot_name
    bot_name = name

def set_company_name(name):
    global company_name
    company_name = name

def main():
    from .main import main  # Ensure main function from main.py is accessible
    return main()
