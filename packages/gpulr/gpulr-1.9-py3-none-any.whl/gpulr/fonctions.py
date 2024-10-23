import re, requests
from bs4 import BeautifulSoup

from .datas import *

def get_connection(login: int, password: str='123') -> requests.Session:
    """
    Connexion à GPU via une requête POST et retourne la session avec les cookies.

    Args:
        login (int): Le nom d'utilisateur pour la connexion.
        password (str): Le mot de passe pour la connexion.

    Returns:
        requests.Session: La session de connexion avec les cookies.
    """
    url = 'https://www.gpu-lr.fr/sat/index.php?page_param=accueilsatellys.php&cat=0&numpage=1&niv=0&clef=/'
    
    # Données pour la requête POST
    data = {
        "modeconnect": "connect",
        "util": login,
        "acct_pass": password
    }

    # Session pour gérer les cookies
    session = requests.Session()

    # Envoie de la requête POST
    response = session.post(url, data=data)

    # Vérifie s'il y a des cookies dans la session
    try:
        response.cookies.get_dict()['util']
    except KeyError:
        raise ConnectionError(login)

    # Retourne la session qui contient les cookies
    return session

def get_infos(session: requests.Session) -> tuple[str, int, int]:
    """
    Récupère les informations de l'étudiant en utilisant la session active.

    Args:
        session (requests.Session): La session active contenant les cookies de connexion.

    Returns:
        tuple[str, int, int]: Les informations de l'étudiant sous la forme (nom, td, tp).
    """
    # URL de la page de l'étudiant
    url = 'https://www.gpu-lr.fr/gpu/index.php?page_param=fpetudiant.php&cat=0&numpage=1&niv=2&clef=/10192/10194/'

    # Envoie une requête GET avec la session active
    response = session.get(url)
    response.raise_for_status()  # Vérifie si la requête a réussi

    # Parse le HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Récupère le nom de l'étudiant
    nom_span = soup.find_all('span', class_='Police1')[0]
    nom = nom_span.text.strip().split(' ', 1)[1]  # Supprime le numéro devant le nom

    # Récupère le TD et le TP
    td_span = soup.find_all('span', class_='Police1')[-1]
    td = td_span.text.split(':')[1].split('-')[3].split(' ')[1].strip()
    tp = td_span.text.split(':')[1].split('-')[5].strip()

    # Retourne les informations de l'étudiant
    return (str(nom), int(td), int(tp))

def list_semaine(session: requests.Session) -> list[int]:
    """
    Récupère la liste des semaines disponibles à partir de la page d'agenda étudiant.

    Args:
        session (requests.Session): La session active contenant les cookies de connexion.

    Returns:
        list: Liste des numéros de semaine disponibles.
    """
    url_agenda = 'https://www.gpu-lr.fr/gpu/index.php?page_param=fpetudiant.php&cat=0&numpage=1&niv=2&clef=/10192/10194/'

    # Envoie une requête GET avec la session active
    response = session.get(url_agenda)
    response.raise_for_status()  # Vérifie si la requête a réussi


    fichier_html = response.text
    liste_semaines = []

    # Recherche les instances du pattern "ActionSemaine('edt',xx)"
    for match in re.finditer(r"OnClick=\"ActionSemaine\('edt',(\d+)\);\"", fichier_html):
        liste_semaines.append(int(match.group(1)))

    return liste_semaines

def get_Semaine(num_etu:int, week:int, session:requests.Session, directory:str) -> None:
    """
    Télécharge les données d'une semaine donnée et les enregistre dans un fichier VCS.

    Args:
        num_etu (int): Numéro de l'étudiant.
        week (int): Numéro de la semaine.
        session (requests.Session): La session active contenant les cookies de connexion.
        directory (str): Dossier où les fichiers VCS seront sauvegardés.
    """
    url_agenda = f"https://www.gpu-lr.fr/gpu/gpu2vcs.php?semaine={week}&prof_etu=ETU&etudiant={num_etu}"

    # Envoie une requête GET avec la session active
    response = session.get(url_agenda)
    response.raise_for_status()  # Vérifie si la requête a réussi

    # Sauvegarde les données dans le fichier VCS
    file_path = f"{directory}/week_{week}.vcs"
    with open(file_path, 'w') as f:
        f.write(response.text)

def get_Semaine_Pdf(num_etu:int, week:int, year:int,session:requests.Session, directory:str) -> None:
    """
    Télécharge les données d'une semaine donnée et les enregistre dans un fichier PDF.

    Args:
        num_etu (int): Numéro de l'étudiant.
        week (int): Numéro de la semaine.
        year (int): Année de la seamine.
        session (requests.Session): La session active contenant les cookies de connexion.
        directory (str): Dossier où les fichiers VCS seront sauvegardés.
    """
    url_pdf = f"https://www.gpu-lr.fr/gpu/imp_edt_pdf.php?type=etudiant&codef=RT-S3&coder={num_etu}&semaine={week}&ansemaine={year}&ispdf=1"
    
    # Envoie une requête GET avec la session active
    response = session.get(url_pdf)
    response.raise_for_status()  # Vérifie si la requête a réussi

    # Sauvegarde les données dans le fichier PDF
    file_path = f"{directory}/week_{week}.pdf"
    with open(file_path, 'wb') as f:
        f.write(response.content)


def decod(text):
    # Remplace les séquences =XX par \xXX pour indiquer un caractère hexadécimal
    modified_text = re.sub(r'=(..)', r'\\x\1', text)
    
    # Convertit la chaîne modifiée en bytes, puis la décode en UTF-8
    decoded_text = bytes(modified_text, "utf-8").decode("unicode_escape").encode("latin1").decode("utf-8")
    
    return decoded_text
