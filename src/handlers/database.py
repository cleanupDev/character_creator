import mysql.connector as mysql
import os
from dotenv import load_dotenv
load_dotenv()

def connection():
    conn = mysql.connect(
        host=os.getenv("HOST_DB"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )

    return conn


def init_database():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        """ --sql
                   CREATE TABLE IF NOT EXISTS characters (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       level INTEGER NOT NULL,
                       experience INTEGER NOT NULL,
                       origin TEXT NOT NULL,
                   """
    )

    cursor.execute(
        """ --sql
                   CREATE TABEL IF NOT EXISTS attributes (
                       character_id INTEGER NOT NULL,
                       strength INTEGER NOT NULL,
                       perception INTEGER NOT NULL,
                       endurance INTEGER NOT NULL,
                       charisma INTEGER NOT NULL,
                       intelligence INTEGER NOT NULL,
                       agility INTEGER NOT NULL,
                       luck INTEGER NOT NULL,
                       FOREIGN KEY (character_id) REFERENCES characters (id)
                   """
    )

    cursor.execute(
        """ --sql
                   CREATE TABLE IF NOT EXISTS skills (
                       skill TEXT NOT NULL,
                       attribute TEXT NOT NULL,
                       details TEXT NOT NULL,
                   """
    )

    cursor.execute(
        """ --sql
                   CREATE TABLE IF NOT EXISTS character_skills (
                        character_id INTEGER NOT NULL,
                        skill_id INTEGER NOT NULL,
                        skill_level INTEGER NOT NULL,
                        tag_skill boolean NOT NULL,
                        FOREIGN KEY (character_id) REFERENCES characters (id),
                        FOREIGN KEY (skill_id) REFERENCES skills (id)
                   """
    )

    cursor.execute(
        """ --sql
                   CREATE TABLE IF NOT EXISTS perks (
                       name TEXT NOT NULL,
                       ranks INTEGER NOT NULL,
                       requirements TEXT NOT NULL,
                       description TEXT NOT NULL,
                   """
    )

    cursor.execute(
        """ --sql
                     CREATE TABLE IF NOT EXISTS character_perks (
                        character_id INTEGER NOT NULL,
                        perk_id INTEGER NOT NULL,
                        rank INTEGER NOT NULL,
                        FOREIGN KEY (character_id) REFERENCES characters (id),
                        FOREIGN KEY (perk_id) REFERENCES perks (id)
                    """
    )

    cursor.execute(
        """ --sql
                   CREATE TABLE IF NOT EXISTS weapon_types (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       skill_id INTEGER NOT NULL,
                       FOREIGN KEY (skill_id) REFERENCES skills (id)
                    """
    )

    cursor.execute(
        """ --sql
                   CREATE TABLE IF NOT EXISTS weapons (
                       
                   """
    )

    cursor.execute(
        """ --sql
                    CREATE TABLE IF NOT EXISTS items (
                        name TEXT NOT NULL,
                        
                    """
    )

    cursor.execute(
        """ --sql
                     CREATE TABLE IF NOT EXISTS inventory (
                        character_id INTEGER NOT NULL,
                        item_id TEXT NOT NULL,
                        amount INTEGER NOT NULL,
                        FOREIGN KEY (character_id) REFERENCES characters (id)
                    """
    )
    
    
    conn.commit()
    conn.close()

