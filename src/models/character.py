class Character:
    def __init__(self, name, level, experience, origin, attributes, skills, perks):
        self.name = name
        self.level = level
        self.experience = experience
        self.origin = origin
        self.attributes: Attributes = attributes
        self.skills: list[Skills] = skills
        self.perks: list[Perks] = perks

    def __str__(self):
        return f'Character(name={self.name}, level={self.level}, experience={self.experience}, origin={self.origin}, attributes={self.attributes}, skills={self.skills}, perks={self.perks})'

    def __repr__(self):
        return f'Character(name={self.name}, level={self.level}, experience={self.experience}, origin={self.origin}, attributes={self.attributes}, skills={self.skills}, perks={self.perks})'
    
    
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
    

class Skills:
    def __init__(self, skill, attribute, details):
        self.skill = skill
        self.attribute = attribute
        self.details = details

    def __str__(self):
        return f'Skills(skill={self.skill}, attribute={self.attribute}, details={self.details})'

    def __repr__(self):
        return f'Skills(skill={self.skill}, attribute={self.attribute}, details={self.details})'
    
    
class Perks:
    def __init__(self, name, rank, description):
        self.name = name
        self.rank = rank
        self.description = description

    def __str__(self):
        return f'Perks(name={self.name}, description={self.description})'

    def __repr__(self):
        return f'Perks(name={self.name}, description={self.description})'