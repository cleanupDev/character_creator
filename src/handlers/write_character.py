from src.handlers.database import connection
from src.models.character import Character, Attributes, Skills, Perks
import logging

logging.basicConfig(level=logging.INFO)


def create_new_character(char: Character) -> bool:
    logging.info(f"create_new_character called with {char}")
    print("______________________________")
    try:
        conn = connection()
        cursor = conn.cursor()
        # check the cursor
        logging.info(f"cursor is {cursor}")

        logging.info(f"char.name is {char.name}")
        logging.info(f"char.level is {char.level}")
        logging.info(f"char.experience is {char.experience}")
        logging.info(f"char.origin is {char.origin}")
        cursor.execute(
            """INSERT INTO characters (name, level, experience, origin)
                    VALUES (%s, %s, %s, %s)
                """,
            (char.name, char.level, char.experience, char.origin),
        )
        logging.info(f"inserted into characters table")

        cursor.execute(
            """SELECT id FROM characters WHERE name = %s AND level = %s AND experience = %s AND origin = %s
                """,
            (char.name, char.level, char.experience, char.origin),
        )
        logging.info(f"selected from characters table")

        character_id = cursor.fetchone()[0]

        logging.info(f"character_id is {character_id}")

        cursor.execute(
            """INSERT INTO attributes (character_id, strength, perception, endurance, charisma, intelligence, agility, luck)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
            (
                character_id,
                char.attributes.strength,
                char.attributes.perception,
                char.attributes.endurance,
                char.attributes.charisma,
                char.attributes.intelligence,
                char.attributes.agility,
                char.attributes.luck,
            ),
        )

        logging.info(
            f"inserted into attributes table with {character_id}, {char.attributes.strength}, {char.attributes.perception}, {char.attributes.endurance}, {char.attributes.charisma}, {char.attributes.intelligence}, {char.attributes.agility}, {char.attributes.luck}"
        )

        for skill in char.skills:
            cursor.execute(
                """SELECT id FROM skills WHERE skill = %s AND attribute = %s AND details = %s
                    """,
                (skill.skill, skill.attribute, skill.details),
            )

            skill_id = cursor.fetchone()[0] if cursor.fetchone() else None

            cursor.execute(
                """INSERT INTO character_skills (character_id, skill_id, skill_level, tag_skill)
                        VALUES (%s, %s, %s, %s)
                    """,
                (character_id, skill_id, skill.skill_level, skill.tag_skill),
            )

        for perk in char.perks:
            cursor.execute(
                """INSERT INTO character_perks (character_id, perk_id, perk_rank)
                        VALUES (%s, %s, %s)
                    """,
                (char.name, perk.perk_id, perk.rank),
            )

        conn.commit()
        conn.close()

        return True

    except Exception as e:
        logging.critical(f"Error creating character: {e}")
        print(e)
        return False
