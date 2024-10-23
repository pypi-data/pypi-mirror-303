from .class_perso import Event

def parse_multiple_events(ical_content: list[str]) -> list[Event]:
    """
    Analyse un contenu iCalendar contenant plusieurs événements et retourne une liste d'objets Event.

    Paramètre :
    - ical_content (str) : Le contenu du fichier iCalendar au format texte.

    Retourne :
    - List[Event] : Une liste d'instances Event représentant chaque événement trouvé dans le fichier iCalendar.
    """
    events: list[Event] = []  # Liste pour stocker les événements instanciés
    current_event_data: list[str] = []  # Liste temporaire pour stocker les lignes d'un événement
    inside_event = False  # Flag pour indiquer si on est à l'intérieur d'un événement

    # Parcourt chaque ligne du contenu iCalendar
    for line in ical_content:
        if line.startswith("BEGIN:VEVENT"):
            # Début d'un nouvel événement
            inside_event = True
            current_event_data = []  # Commence à stocker les lignes de l'événement
        elif line.startswith("END:VEVENT"):
            # Fin d'un événement, ajouter l'événement à la liste
            # Joindre les lignes pour en faire un bloc
            current_event_data = [i for i in current_event_data if i] #Supprimes les élements vide.
            dict_event_data:dict[str,str]={}
            for line in current_event_data:
                dict_event_data[line.split(':')[0]] = ':'.join(line.split(':')[1:])
            events.append(Event.from_ical(dict_event_data))  # Ajouter l'événement à la liste des événements
            inside_event = False  # Réinitialise le flag
        elif inside_event:
            # Si on est à l'intérieur d'un événement, on stocke chaque ligne
            current_event_data.append(line.strip()) #Ajoute la ligne en enlevant le \n
    return events   
