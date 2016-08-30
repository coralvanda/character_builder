class race(object):
	pass


class human(race):
	def __init__(self):
		self.base_strength = 10
		self.base_dexterity = 10
		self.base_constitution = 10
		self.base_intelligence = 10
		self.base_wisdom = 10
		
	def print_race(self):
		return 'Human'

	def print_other_bonuses(self):
		return 'Standard jack of all trades.'

	

class elf(race):
	def __init__(self):
		self.base_strength = 7
		self.base_dexterity = 15
		self.base_constitution = 7
		self.base_intelligence = 15
		self.base_wisdom = 6
		
	def print_race(self):
		return 'Elf'

	def print_other_bonuses(self):
		return 'Moves silently over any terrain.'


class dwarf(race):

	def __init__(self):
		self.base_strength = 15
		self.base_dexterity = 5
		self.base_constitution = 15
		self.base_intelligence = 4
		self.base_wisdom = 11
	
	def print_race(self):
		return 'Dwarf'

	def print_other_bonuses(self):
		return 'Innate sense for locating minerals and ore.'
		
		
class orc(race):

	def __init__(self):
		self.base_strength = 15
		self.base_dexterity = 7
		self.base_constitution = 15
		self.base_intelligence = 2
		self.base_wisdom = 11
	
	def print_race(self):
		return 'Orc'

	def print_other_bonuses(self):
		return 'High natural resistance to poisons.'