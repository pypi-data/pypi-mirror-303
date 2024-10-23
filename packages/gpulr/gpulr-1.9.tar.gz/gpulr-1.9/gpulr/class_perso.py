import datetime
from typing import Optional

from .fonctions import get_connection,get_infos,decod
from .datas import *

class ConnectionError(Exception):
    pass

class RestructurationError(Exception):
    pass

class Event:
    """
    Classe représentant un événement iCalendar (RFC 5545).
    
    Attributs :
    - sequence : Nombre de modifications de l'événement depuis sa création.
    - uid : Identifiant unique de l'événement.
    - dtstamp : Date et heure de la dernière modification (ou création) de l'événement.
    - description : Description de l'événement.
    - summary : Titre de l'événement.
    - location : Lieu où l'événement a lieu.
    - dtstart : Date et heure de début de l'événement.
    - dtend : Date et heure de fin de l'événement.
    - priority : Niveau de priorité de l'événement.
    - event_class : Confidentialité de l'événement (PUBLIC ou PRIVATE).
    """

    def __init__(self, 
                 sequence: int, 
                 uid: str, 
                 dtstamp: datetime.datetime, 
                 description: str, 
                 summary: str, 
                 location: str, 
                 dtstart: datetime.datetime, 
                 dtend: datetime.datetime, 
                 priority: int, 
                 event_class: str) -> None:
        """
        Initialise un événement avec tous ses attributs.

        Paramètres :
        - sequence (int) : Le nombre de modifications apportées à l'événement.
        - uid (str) : Identifiant unique de l'événement.
        - dtstamp (datetime.datetime) : Date et heure de la dernière modification (ou création).
        - description (str) : Description de l'événement (peut être None).
        - summary (str) : Titre de l'événement.
        - location (str) : Lieu de l'événement (peut être None).
        - dtstart (datetime.datetime) : Date et heure de début de l'événement.
        - dtend (datetime.datetime) : Date et heure de fin de l'événement.
        - priority (int) : Niveau de priorité de l'événement (de 0 à 9).
        - event_class (str) : Classe de l'événement (ex : PUBLIC, PRIVATE).
        """
        self._sequence: int = sequence
        self._uid: str = uid
        self._dtstamp: datetime.datetime = dtstamp
        self._description: str = description
        self._summary: str = summary
        self._location: str = location
        self._dtstart: datetime.datetime = dtstart
        self._dtend: datetime.datetime = dtend
        self._priority: int = priority
        self._event_class: str = event_class
        self._restructured: bool = False

    @property
    def sequence(self) -> int:
        return self._sequence

    @sequence.setter
    def sequence(self, value: int) -> None:
        self._sequence = value

    @property
    def uid(self) -> str:
        return self._uid

    @uid.setter
    def uid(self, value: str) -> None:
        self._uid = value

    @property
    def dtstamp(self) -> datetime.datetime:
        return self._dtstamp

    @dtstamp.setter
    def dtstamp(self, value: datetime.datetime) -> None:
        self._dtstamp = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    @property
    def summary(self) -> str:
        return self._summary

    @summary.setter
    def summary(self, value: str) -> None:
        self._summary = value

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, value: str) -> None:
        self._location = value

    @property
    def dtstart(self) -> datetime.datetime:
        return self._dtstart

    @dtstart.setter
    def dtstart(self, value: datetime.datetime) -> None:
        self._dtstart = value

    @property
    def dtend(self) -> datetime.datetime:
        return self._dtend

    @dtend.setter
    def dtend(self, value: datetime.datetime) -> None:
        self._dtend = value

    @property
    def priority(self) -> int:
        return self._priority

    @priority.setter
    def priority(self, value: int) -> None:
        self._priority = value

    @property
    def event_class(self) -> str:
        return self._event_class

    @event_class.setter
    def event_class(self, value: str) -> None:
        self._event_class = value
        
    def __str__(self) -> str:
        """
        Retourne une chaîne lisible représentant l'événement.

        Retourne :
        - Une chaîne formatée avec les informations essentielles de l'événement.
        """
        return (f"Event(UID={self._uid}, Summary={self._summary}, Description= {self._description}"
                f"Location={self._location}, Start={self._dtstart}, End={self._dtend})")
    
    def format_datas(self) -> None:
        """
        Restructure les données de l'événement. Cette fonction ne peut être utilisée qu'une seule fois.

        Format le tritre de la facons suivante : COUR de TELCO4
        Et la description : R3.07-Réseaux d'accès\nProf: xxx
        """
        if self._restructured:
            raise Exception("Les données ont déjà été restructurées.")
        
        # Restructurer le titre et extraction du groupe pour se cour
        parts = self._summary.split(" / ")
        if len(parts) > 1:
            self._summary = f"{parts[1]} de {parts[0]}"

            groupe:int=0
            try:
                groupe=int(parts[2].split('-')[1].split(' ')[1])
            except IndexError:
                try:
                    groupe=int(parts[2].split('-')[1].split(' ')[0])
                except:
                    groupe=0
            if groupe//10>9:
                self._tp = groupe
            elif groupe//10>0:
                self._td = groupe

        # Restructurer la description
        desc_parts:list[str] = self._description.split(":")
        spe:str = decod(desc_parts[3].split('\\')[0])
        prof_abbr:str = desc_parts[2].split(' ')[0]
        if len(prof_abbr.split('/'))>1:
            prof_list:list[str]=[]
            for i in prof_abbr.split('/'):
                prof_list.append(asso_prof.get(i, i))
            self._description = f"{spe}\\nProfs : {', '.join(prof_list)}"
        else:
            prof_name:str = asso_prof.get(prof_abbr, prof_abbr)
            self._description = f"{spe}\\nProf : {prof_name}"

        self._restructured= True

    def ajouter_heure_si_hiver(self) -> None:
        """
        Rajoute une heure au début et à la fin d'un événement si celui-ci est dans l'heure d'hiver 
        """
        # Calculer le dernier dimanche de mars
        def dernier_dimanche_mars(year):
            for day in range(31, 24, -1):
                if datetime.datetime(year, 3, day).weekday() == 6:
                    return datetime.datetime(year, 3, day, 2, 0, 0)
        
        # Calculer le dernier dimanche d'octobre
        def dernier_dimanche_octobre(year):
            for day in range(31, 24, -1):
                if datetime.datetime(year, 10, day).weekday() == 6:
                    return datetime.datetime(year, 10, day, 3, 0, 0)
        
        # Obtenir les dates de début et de fin de l'heure d'été pour l'année de la date donnée
        debut_heure_ete = dernier_dimanche_mars(self._dtstart.year)
        fin_heure_ete = dernier_dimanche_octobre(self._dtstart.year)
        
        # Vérifier si la date est en heure d'hiver
        if not (debut_heure_ete <= self._dtstart < fin_heure_ete):
                # Ajouter une heure
                self._dtstart += datetime.timedelta(hours=1)
                self._dtend += datetime.timedelta(hours=1)
        


    @staticmethod
    def parse_datetime(ical_date: str) -> datetime.datetime:
        """
        Convertit une chaîne de date au format iCalendar (YYYYMMDDTHHMMSSZ) en objet datetime.

        Paramètre :
        - ical_date (str) : La date sous forme de chaîne iCalendar.

        Retourne :
        - Un objet datetime correspondant à la chaîne.
        """
        return datetime.datetime.strptime(ical_date, '%Y%m%dT%H%M%SZ')

    @classmethod
    def from_ical(cls, ical_data: dict[str, str]) -> 'Event':
        """
        Crée une instance d'Event à partir des données iCalendar.

        Paramètre :
        - ical_data (Dict[str, str]) : Les données iCalendar au format dictionnaire.

        Retourne :
        - Une instance d'Event remplie avec les informations extraites des données iCalendar.
        """
        return cls(
            sequence=int(ical_data.get("SEQUENCE", 0)),
            uid=ical_data.get("UID", ""),
            dtstamp=cls.parse_datetime(ical_data.get("DTSTAMP", "")),
            description=ical_data.get("DESCRIPTION;ENCODING=QUOTED-PRINTABLE", ""),
            summary=ical_data.get("SUMMARY", ""),
            location=ical_data.get("LOCATION", ""),
            dtstart=cls.parse_datetime(ical_data.get("DTSTART", "")),
            dtend=cls.parse_datetime(ical_data.get("DTEND", "")),
            priority=int(ical_data.get("PRIORITY", 0)),
            event_class=ical_data.get("CLASS", "PUBLIC")
        )
   
class Student:
    def __init__(self, num: int, nom: Optional[str] = None, td: Optional[int] = None, tp: Optional[int] = None) -> None:
        """
        Initialise un nouvel étudiant avec un numéro, et éventuellement un nom, un groupe de TD et un groupe de TP.

        :param num: Numéro de l'étudiant
        :param nom: Nom de l'étudiant (optionnel)
        :param td: Numéro du groupe de TD de l'étudiant (optionnel)
        :param tp: Numéro du groupe de TP de l'étudiant (optionnel)
        """
        self._num: int = num
        self._nom: Optional[str] = nom
        self._td: Optional[int] = td
        self._tp: Optional[int] = tp

        if nom is None or td is None or tp is None:
            self._completer_infos()

    def _completer_infos(self) -> None:
        """
        Complète les informations de l'étudiant en utilisant les fonctions get_connection et get_infos.
        """
        user_session = get_connection(self._num)
        infos_user = get_infos(user_session)
        self._nom = infos_user[0]
        self._td = int(infos_user[1])
        self._tp = int(infos_user[2])

    @property
    def num(self) -> int:
        return self._num

    @num.setter
    def num(self, value: int) -> None:
        self._num = value

    @property
    def nom(self) -> Optional[str]:
        return self._nom

    @nom.setter
    def nom(self, value: Optional[str]) -> None:
        self._nom = value

    @property
    def td(self) -> Optional[int]:
        return self._td

    @td.setter
    def td(self, value: Optional[int]) -> None:
        self._td = value

    @property
    def tp(self) -> Optional[int]:
        return self._tp

    @tp.setter
    def tp(self, value: Optional[int]) -> None:
        self._tp = value

    def __repr__(self) -> str:
        return f"{self._num};{self._nom};{self._td};{self._tp}"
    
    def __del__(self) -> None:
        pass

class Agenda:
    def __init__(self, student: Student) -> None:
        """
        Initialise un nouvel agenda pour un étudiant.

        :param student: Instance de la classe Student associée à l'agenda
        """
        self._student: Student = student
        self._events: list[Event] = []
    
    def __len__(self):
        """
        Renvoie le nombre d'events
        """
        return len(self._events)
    
    def ajouter_event(self, event: Event) -> None:
        """
        Ajoute un événement à l'agenda.

        :param event: Instance de la classe Event à ajouter
        """
        self._events.append(event)

    def ajouter_events(self, events: list[Event]) -> None:
        """
        Ajoute un événement à l'agenda.

        :param events: Liste d'nstance de la classe Event à ajouter
        """
        self._events+=events
   
    def __repr__(self) -> str:
        """
        Retourne une représentation sous forme de chaîne de l'agenda.
        """
        events_str = "\n".join([str(event) for event in self._events])
        return f"Agenda de {self._student.nom}:\n{events_str}"
    
    
    def restructuration(self):
        """
        Restructure les données des événements.
        """
        to_remove:list[Event]=[]
        for event in self._events:
            try:
                event.format_datas()
                event.ajouter_heure_si_hiver()
            except RestructurationError:
                pass
            if hasattr(event, '_td') and event._td == self._student._td:
                pass
            elif hasattr(event, '_tp') and event._tp == self._student._tp:
                pass
            elif hasattr(event, '_td') or hasattr(event, '_tp'):
                to_remove.append(event)
            else:
                pass
        for event in to_remove:
            self._events.remove(event)

    def export(self, filename: str) -> None:
        ics_content = "BEGIN:VCALENDAR\nPRODID:-//Paulin_DOYON//IUTRTLR//FR\nVERSION:2.0\nCALSCALE:GREGORIAN\nX-WR-CALNAME:Emploi du temps - IUT La Rochelle\nX-WR-TIMEZONE:Europe/Paris\nX-WR-CALDESC:Emploi du temps de l'IUT récupéré à partir de GPU LR\nBEGIN:VTIMEZONE\nTZID:Europe/Paris\nX-LIC-LOCATION:Europe/Paris\nBEGIN:DAYLIGHT\nDTSTART:19700329T020000\nTZNAME:CEST\nTZOFFSETFROM:+0100\nTZOFFSETTO:+0200\nRRULE:FREQ=YEARLY;INTERVAL=1;BYMONTH=3;BYDAY=-1SU\nTZNAME:CET\nEND:DAYLIGHT\nBEGIN:STANDARD\nDTSTART:19701025T030000\nTZOFFSETFROM:+0200\nTZOFFSETTO:+0100\nRRULE:FREQ=YEARLY;INTERVAL=1;BYMONTH=10;BYDAY=-1SU\nEND:STANDARD\nEND:VTIMEZONE\n"
        for event in self._events:
            ics_content += f"BEGIN:VEVENT\n"
            ics_content += f"UID:{event._uid}\n"
            ics_content += f"DTSTAMP:{datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')}\n"
            ics_content += f"DTSTART:{event._dtstart.strftime('%Y%m%dT%H%M%SZ')}\n"
            ics_content += f"DTEND:{event._dtend.strftime('%Y%m%dT%H%M%SZ')}\n"
            ics_content += f"SUMMARY:{event._summary}\n"
            ics_content += f"DESCRIPTION:{event._description}\n"
            ics_content += f"LOCATION:{event._location}\n"
            ics_content += f"PRIORITY:{event._priority}\n"
            ics_content += f"CLASS:{event._event_class}\n"
            ics_content += "END:VEVENT\n"
        ics_content += "END:VCALENDAR"

        with open(filename, 'w',encoding="utf-8") as file:
            file.write(ics_content)       