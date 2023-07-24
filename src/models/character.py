class Character:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id') or None
        self.name = kwargs.get('name')
        self.level = kwargs.get('level') or 1
        self.experience = kwargs.get('experience') or 1
        self.origin = kwargs.get('origin')
        self.attributes: Attributes = kwargs.get('attributes') or Attributes(5, 5, 5, 5, 5, 5, 5)
        self.skills: list[Skills] = kwargs.get('skills') or []
        self.perks: list[Perks] = kwargs.get('perks') or []

    def __str__(self):
        return f'Character(name={self.name}, level={self.level}, experience={self.experience}, origin={self.origin}, attributes={self.attributes}, skills={self.skills}, perks={self.perks})'

    def __repr__(self):
        return f'Character(name={self.name}, level={self.level}, experience={self.experience}, origin={self.origin}, attributes={self.attributes}, skills={self.skills}, perks={self.perks})'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'level': self.level,
            'experience': self.experience,
            'origin': self.origin,
            'attributes': self.attributes.to_dict(),
            'skills': [skill.to_dict() for skill in self.skills],
            'perks': [perk.to_dict() for perk in self.perks]
        }
    
class Attributes:
    def __init__(self, strength, perception, endurance, charisma, intelligence, agility, luck):
        self.strength = strength
        self.perception = perception
        self.endurance = endurance
        self.charisma = charisma
        self.intelligence = intelligence
        self.agility = agility
        self.luck = luck

    def __str__(self):
        return f'Attributes(strength={self.strength}, perception={self.perception}, endurance={self.endurance}, charisma={self.charisma}, intelligence={self.intelligence}, agility={self.agility}, luck={self.luck})'

    def __repr__(self):
        return f'Attributes(strength={self.strength}, perception={self.perception}, endurance={self.endurance}, charisma={self.charisma}, intelligence={self.intelligence}, agility={self.agility}, luck={self.luck})'
    
    def to_dict(self):
        return {
            'strength': self.strength,
            'perception': self.perception,
            'endurance': self.endurance,
            'charisma': self.charisma,
            'intelligence': self.intelligence,
            'agility': self.agility,
            'luck': self.luck
        }
    

class Skills:
    def __init__(self, id, skill, attribute, details):
        self.id = id
        self.skill = skill
        self.attribute = attribute
        self.details = details

    def __str__(self):
        return f'Skills(skill={self.skill}, attribute={self.attribute}, details={self.details})'

    def __repr__(self):
        return f'Skills(skill={self.skill}, attribute={self.attribute}, details={self.details})'
    
    def to_dict(self):
        return {
            'id': self.id,
            'skill': self.skill,
            'attribute': self.attribute,
            'details': self.details
        }
        
    
class Perks:
    def __init__(self, perk_id, name, rank, description):
        self.perk_id = perk_id
        self.name = name
        self.rank = rank or 1
        self.description = description

    def __str__(self):
        return f'Perks(perk_id={self.perk_id}, name={self.name}, description={self.description})'

    def __repr__(self):
        return f'Perks(perk_id={self.perk_id}, name={self.name}, description={self.description})'
    
    def to_dict(self):
        return {
            'perk_id': self.perk_id,
            'name': self.name,
            'rank': self.rank,
            'description': self.description
        }