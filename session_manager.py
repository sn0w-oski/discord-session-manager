from blessed import Terminal
import os, time, requests
from getpass import getpass
from safe_data import get_token

selected_value = None
gray_blue = '\033[38;2;128;128;255m'
reset_color = '\033[0m'
void_spance0 ="          "
void_space ="                                  "
all_id_hash = []
choice        = [f"{void_space}yes",f"{void_space}no"]

token = get_token()
header = {"authorization": token,"x-super-properties": "ewogICJvcyI6ICJMaW51eCIsCiAgImNsaWVudF9idWlsZF9udW1iZXIiOiAxNTEzMzAKfQ=="}

banner = (gray_blue + """
                            ▄• ▄▌▄▄▌   ▐ ▄  ▄▄▄·     
                            █▪██▌██•  •█▌▐█▐█ ▀█     
                            █▌▐█▌██▪  ▐█▐▐▌▄█▀▀█     
                            ▐█▄█▌▐█▌▐▌██▐█▌▐█ ▪▐▌    
                            ▀▀▀ .▀▀▀ ▀▀ █▪ ▀  ▀     
""" + reset_color)

def get_password():
    password_ = getpas("Your password : ")
    return password_

def remove_session(id_hash, header):
    payload = {"session_id_hashes": [id_hash], "password": get_password()}
    requests.post("https://ptb.discord.com/api/v9/auth/sessions/logout",headers=header, json=payload)

def remove_all_session(header):
    payload = {"session_id_hashes": all_id_hash, "password": get_password()}
    requests.post("https://ptb.discord.com/api/v9/auth/sessions/logout",headers=header, json=payload)
    os.remove("./auth/token.txt")
    exit()
def sessions_get():
    session = []
    r = requests.get("https://ptb.discord.com/api/v10/auth/sessions", headers=header)
    if rst == 401:   
        print("Token is bad ")
        os.remove("./auth/token.txt")
        token = get_token()
        header = {"authorization": token,"x-super-properties": "ewogICJvcyI6ICJMaW51eCIsCiAgImNsaWVudF9idWlsZF9udW1iZXIiOiAxNTEzMzAKfQ=="}
    for data_session in r['user_sessions']:
        os_ = data_session['client_info']['os']
        platform = data_session['client_info']['platform']
        geo = data_session['client_info']['location']
        geo = geo.split(",")
        session.append((
            f"{void_spance0}{gray_blue}OS : {os_.ljust(7)} | Platform {platform.ljust(16)}| Geo : {geo[0].ljust(10)}{reset_color}",
            f"{data_session['id_hash']}"
        ))
        all_id_hash.append(data_session['id_hash'])
    session.append(("\n",""))
    session.append((
        f"{2*void_spance0}        {gray_blue}Close all session",
        f"All"    
    ))
    session.append((
        f"{void_space}{gray_blue}Quit",
        f"Quit"    
    ))
    return session

def afficher_menu(t, options, choix_utilisateur):
    for i, option_tuple in enumerate(options):
        option, value = option_tuple
        if choix_utilisateur == i:
            print(t.reverse(f"> {option.rjust(10)}"))
            selected_value = value
        else:
            print(f"  {option}")
    return selected_value

def afficher_choice(t, choice, choix_utilisateur):
    selected_value = None
    for i, option_tuple in enumerate(choice):
        value = option_tuple
        if choix_utilisateur == i:
            print(t.reverse(f"> {gray_blue}{value}"))
            selected_value = value
        else:
            print(f"  {value}")

    return selected_value

def main():
    while 1:
        t = Terminal()
        options = sessions_get()
        choix_utilisateur = 0

        while True:
            os.system("cls")

            print(banner) 
            with t.cbreak(), t.hidden_cursor():
                selected_value = afficher_menu(t, options, choix_utilisateur)

                key = t.inkey()
                if key.name == "KEY_UP" and choix_utilisateur > 0:
                    choix_utilisateur -= 1
                elif key.name == "KEY_DOWN" and choix_utilisateur < len(options) - 1:
                    choix_utilisateur += 1
                elif key.name == "KEY_ENTER" and choix_utilisateur == len(options) - 1:
                    break

                if key.name == "KEY_ENTER":
                    break
        if selected_value == "Quit":
            exit()
        elif selected_value == "All":
            remove_all_session(header)
        id_hash = selected_value
        while True:
            os.system("cls")
            print(banner) 
            print(gray_blue,"                       /!\ Remove this connection ? /!\ \n")
            with t.cbreak(), t.hidden_cursor():
                selected_value = afficher_choice(t, choice, choix_utilisateur)

                key = t.inkey()
                if key.name == "KEY_UP" and choix_utilisateur > 0:
                    choix_utilisateur -= 1
                elif key.name == "KEY_DOWN" and choix_utilisateur < len(choice) - 1:
                    choix_utilisateur += 1
                elif key.name == "KEY_ENTER" and choix_utilisateur == len(choice) - 1:
                    break

                if key.name == "KEY_ENTER":
                    break

        if selected_value.strip() == "yes":
            remove_session(id_hash, header)
        else:
            pass
if __name__ == "__main__":
    main()

