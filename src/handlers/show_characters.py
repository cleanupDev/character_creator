from src.handlers.database import connection
from src.models.character import Character, Attributes, Skills, Perks
import logging

logging.basicConfig(level=logging.INFO)


def get_characters():
    logging.info(f"get_characters called")
    
    try:
        conn = connection()
        cursor = conn.cursor()
        # check the cursor
        logging.info(f"cursor is {cursor}")
        
        cursor.execute(
            """SELECT * FROM characters"""
        )
        logging.info(f"selected from characters table")
        
        characters = cursor.fetchall()
        
        characters = [Character(id=character[0], name=character[1], level=character[2], experience=character[3], origin=character[4]) for character in characters]
        
        for char in characters:
            cursor.execute("""
                SELECT * FROM attributes WHERE character_id = %s
            """, (char.id,))  # Pass char.id as an argument

            attributes = cursor.fetchone()

            char.attributes = Attributes(
                strength=attributes[1],
                perception=attributes[2],
                endurance=attributes[3],
                charisma=attributes[4],
                intelligence=attributes[5],
                agility=attributes[6],
                luck=attributes[7]
            )

            
            cursor.execute("""
                SELECT * FROM character_skills
                LEFT JOIN skills ON character_skills.skill_id = skills.id
                WHERE character_id = %s
            """, (char.id,))  # Pass char.id as an argument

            skills = cursor.fetchall()
            
            
            # Skill(id, skill, attribute, details)
            char.skills = [Skills(id=skill[1], skill=skill[5], attribute=skill[6], details=skill[7]) for skill in skills]
                        
            cursor.execute("""
                SELECT * FROM character_perks
                LEFT JOIN perks ON character_perks.perk_id = perks.id
                WHERE character_id = %s
            """, (char.id,))  # Pass char.id as an argument

            perks = cursor.fetchall()
            char.perks = [Perks(id=perk[1], name=perk[4], rank=perk[2], description=perk[7]) for perk in perks]
            
        return characters
    
    except Exception as e:
        logging.error(f"Error getting characters: {e}")
        return None
    
    finally:
        conn.close()
        logging.info(f"Connection closed")