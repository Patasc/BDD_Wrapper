from Database import Database

from BDD_PSQL.PsqlDatabase import PsqlDatabase

handlers = {"psql": PsqlDatabase}


def initiate(systeme: str) -> Database:
    """
    Initialise la classe enfant de Database en fonction du type de base de donnée demandée et renvoie l'objet gérant
    La connection
    :param systeme: Type de la base de donnée
    :return:
    """
    if systeme.lower() not in handlers.keys():
        raise ValueError("Paramètre non reconnu")

    return handlers.get(systeme.lower())()
