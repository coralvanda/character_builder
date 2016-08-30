#! python3

import os
import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from race import *

	
class character(object):
	'''Sets up an object called character which will contain all the relevant info
	needed to build the character, such as name, race, level, stats, and stat points.'''
	def __init__(self):
		self.name = ''
		self.level = 1
		self.race = human()
		self.strength = self.race.base_strength
		self.dexterity = self.race.base_dexterity
		self.constitution = self.race.base_constitution
		self.intelligence = self.race.base_intelligence
		self.wisdom = self.race.base_wisdom
		
		# The following base values will be updated by the method update_stats()
		self.health = 50
		self.mana = 50
		self.available_stat_points = 0
		
		# Spent_stat_points is updated by the stat incrementors primarily
		self.spent_stat_points = 0
		
	def print_stats(self):
		'''Allows for neater printing of the character's various stats.'''
		return ('Str: ' + str(self.strength) + " "
			'Dex: ' + str(self.dexterity) + " "
			'Con: ' + str(self.constitution) + " "
			'Int: ' + str(self.intelligence) + " "
			'Wis: ' + str(self.wisdom))
	
	def print_char(self):
		'''Displays a window neatly showing the various character info.'''
		char_printout = ('Name: ' + str(self.name) + '\n' 
						'Level: ' + str(self.level) + '\n' 
						'Race: ' + str(self.race.print_race()) + '\n' 
						'Health: ' + str(self.health) + '\n' 
						'Mana: ' + str(self.mana) + '\n' 
						'Available stat points: ' + str(self.available_stat_points) + '\n' 
						'Stats: ' + str(self.print_stats()))
		messagebox.showinfo('Your character', char_printout)
		
	def update_stats(self):
		'''Updates the character's health, mana, and stat points based on current
		race, level, and entered stat points.'''
		self.health = 50 + (self.constitution * self.race.base_constitution * 5) + \
					((self.level - 1) * 20)
		if self.intelligence > self.wisdom:
			self.mana = 50 + ((self.wisdom + self.intelligence * 
						self.race.base_intelligence + ((self.level-1) * 20)) // 2)
		else:
			self.mana = 50 + ((self.intelligence + self.wisdom * 
						self.race.base_wisdom + ((self.level-1) * 20)) // 2)
		self.available_stat_points = ((self.level - 1) * 5) - self.spent_stat_points

	
def assign_race(race):
	'''Takes a string as input and assigns the character's race accordingly'''
	if race == 'Human':
		my_first_character.race = human()
	elif race == 'Elf':
		my_first_character.race = elf()
	elif race == 'Dwarf':
		my_first_character.race = dwarf()
	else:
		my_first_character.race = orc()

		
my_first_character = character()
		
		
# *** Main window ***
window = tkinter.Tk()
window.title('RPG character builder')
width = 150     # controls how wide the window is
height = 200    # controls how tall the window is
window.geometry(str(int(width * 1.75)) + "x" + str(int(height * 1.65))) # sizes the window


# *** Status bar ***
status = tkinter.Label(window, text="Building a character...", bd=1, 
					   relief=tkinter.SUNKEN, anchor=tkinter.W)
status.pack(side=tkinter.BOTTOM, fill='x')


#*** Frames ***
top_frame = tkinter.Frame(window)
top_frame.pack(side=tkinter.TOP, fill='both', expand=True)

top_left_frame = tkinter.Frame(top_frame)
top_left_frame.pack(side=tkinter.LEFT, fill='both')

top_right_frame = tkinter.Frame(top_frame)
top_right_frame.pack(side=tkinter.RIGHT, fill='both')

bottom_frame = tkinter.Frame(window)
bottom_frame.pack(side=tkinter.BOTTOM, fill='both', expand=True)
	

# *** Dropdown menu ***
def new_char():
	'''Resets and clears all fields, allowing user to start over.'''
	global level
	global char_name
	global race_var
	char_name.set("")
	level.set(1)
	race_var.set('Human')
	my_first_character.name = ''
	my_first_character.level = 1
	select_level()
	my_first_character.race = human()
	my_first_character.strength = 10
	my_first_character.dexterity = 10
	my_first_character.constitution = 10
	my_first_character.intelligence = 10
	my_first_character.wisdom = 10
	my_first_character.spent_stat_points = 0
	my_first_character.available_stat_points = 0
	reload_stats()
	update_char()

	
def save_char():
	'''Writes character info to a .txt. file, saved by character name.'''
	def save_to_file(file):
		file.write(my_first_character.name + '\n')
		file.write(str(my_first_character.level) + '\n')
		file.write(my_first_character.race.print_race() + '\n')
		file.write(str(my_first_character.strength) + '\n')
		file.write(str(my_first_character.dexterity) + '\n')
		file.write(str(my_first_character.constitution) + '\n')
		file.write(str(my_first_character.intelligence) + '\n')
		file.write(str(my_first_character.wisdom) + '\n') 
		file.write(str(my_first_character.spent_stat_points)) # no more lines needed
	
	cwd = os.getcwd()
	if os.path.exists(cwd + '\\character'):
		pass # no need to create the folder if it exists already, pass on to next step
	else:
		os.makedirs(cwd + '\\character')
		print("Created new directory to store character files")
	if os.path.exists(cwd + '\\character\\' + my_first_character.name + '.txt'):
		overwrite = messagebox.askquestion('Overwrite character?',
							'Character already exists.  Overwrite?')
		if overwrite == 'yes': 
			char_file = open(cwd + '\\character\\' + my_first_character.name + '.txt', 'w+') 
			save_to_file(char_file)
			char_file.close()
		else:
			messagebox.showinfo('Did not save', 
								'Did not save, did not overwrite existing file.')
	else:
		char_file = open(cwd + '\\character\\' + my_first_character.name + '.txt', 'w+')
		save_to_file(char_file)
		char_file.close()
	

def load_char():
	'''Loads character info from a .txt file based on character name.'''
	file_name = askopenfilename()
	char_file = open(file_name)
	char_data = char_file.readlines()
	
	global char_name
	char_name.set(char_data[0][:-1])
	my_first_character.name = char_data[0][:-1]
	
	global level
	level.set(int(char_data[1][:-1]))
	my_first_character.level = int(char_data[1][:-1])
	select_level()
	
	global race_var
	race_var.set(char_data[2][:-1])
	assign_race(char_data[2][:-1])
		
	my_first_character.strength = int(char_data[3][:-1])
	my_first_character.dexterity = int(char_data[4][:-1])
	my_first_character.constitution = int(char_data[5][:-1])
	my_first_character.intelligence = int(char_data[6][:-1])
	my_first_character.wisdom = int(char_data[7][:-1])
	reload_stats()
	my_first_character.spent_stat_points = int(char_data[8])
	update_char()
	
	char_file.close()

my_menu = tkinter.Menu(window)
window.config(menu=my_menu)

sub_menu = tkinter.Menu(my_menu)
my_menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New character", command=new_char)
sub_menu.add_command(label="Load character", command=load_char)
sub_menu.add_command(label="Save character", command=save_char)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=window.destroy)


#*** Character name entry ***
def confirm_char_name(event):
	'''Locks in the text entered as the character's name.'''
	my_first_character.name = name_entry.get()

char_name = tkinter.StringVar()
name_lbl = tkinter.Label(top_left_frame, text="Enter character name")
name_entry = tkinter.Entry(top_left_frame, textvariable=char_name)
confirm_name_button = tkinter.Button(top_left_frame, text='Confirm name')
confirm_name_button.bind("<Button-1>", confirm_char_name) # when the button is left clicked

name_lbl.pack()
name_entry.pack()
confirm_name_button.pack(pady=2)


# *** Race option menu ***
races = ['Human', 'Elf', 'Dwarf', 'Orc']

race_var = tkinter.StringVar()
race_var.set(races[0]) # sets default value

race_drop_down = tkinter.OptionMenu(top_left_frame, race_var, *races)
race_drop_down.pack()

def confirm_race():
	'''Reassigns the character's race, and resets all stats to the new race's
	base numbers, as well as updating the stat incrementors.'''
	change_race = messagebox.askquestion("Change race", 
										"Changing race will reset stat points. Proceed?")
	if change_race == 'yes':
		assign_race(race_var.get())
		my_first_character.strength = my_first_character.race.base_strength
		my_first_character.dexterity = my_first_character.race.base_dexterity
		my_first_character.constitution = my_first_character.race.base_constitution
		my_first_character.intelligence = my_first_character.race.base_intelligence
		my_first_character.wisdom = my_first_character.race.base_wisdom
		my_first_character.spent_stat_points = 0
		update_char()
		reload_stats()
	else:
		pass

confirm_race_button = tkinter.Button(top_left_frame, text="Confirm race", 
									 command=confirm_race)
confirm_race_button.pack()


# *** Level selector ***
def select_level():
	'''Takes the number value from the level slider, assigns it to the character,
	and then runs the update_char function.  If reducing the character's level would
	result in negative available stat points, it returns an error instead.'''
	if level.get() < my_first_character.level \
	and my_first_character.available_stat_points < 5:
		messagebox.showinfo('Error', 'Refund stat points before decreasing level')
	else:
		selected_level = "Level " + str(level.get())
		level_label.config(text = selected_level)
		my_first_character.level = level.get()
		update_char()

level = tkinter.IntVar()
level_scale = tkinter.Scale(top_left_frame, variable=level, sliderlength=10, 
							from_=1, to=60, orient=tkinter.HORIZONTAL)
level_scale.pack()

level_confirm_button = tkinter.Button(top_left_frame, 
									  text="Confirm level", command=select_level)
level_confirm_button.pack()

level_label = tkinter.Label(top_left_frame)
level_label.pack()


#*** Stat incrementors ***
class stat_incrementor(object): 
	'''Sets up the basic bones for the various stat incrementors.'''
	def __init__(self, frame, stat, row):
		self.frame = frame
		self.stat = stat
		self.row = row
		pady_num = 5
		
		self.stat_name = tkinter.Label(self.frame, text=self.stat)
		self.stat_name.grid(row=self.row, column=0, sticky=tkinter.E, pady=pady_num)
		self.stat_minus_btn = tkinter.Button(self.frame, text='-', command=self.minus_stat)
		self.stat_minus_btn.grid(row=self.row, column=1, pady=pady_num)
		if self.stat == 'Strength':
			self.stat_display = tkinter.Label(self.frame, text=str(my_first_character.strength))
		elif self.stat == 'Dexterity':
			self.stat_display = tkinter.Label(self.frame, text=str(my_first_character.dexterity))
		elif self.stat == 'Constitution':
			self.stat_display = tkinter.Label(self.frame, text=str(my_first_character.constitution))
		elif self.stat == 'Intelligence':
			self.stat_display = tkinter.Label(self.frame, text=str(my_first_character.intelligence))
		else:
			self.stat_display = tkinter.Label(self.frame, text=str(my_first_character.wisdom))
		self.stat_display.grid(row=self.row, column=2, pady=pady_num)
		self.stat_plus_btn = tkinter.Button(self.frame, text='+', command=self.plus_stat)
		self.stat_plus_btn.grid(row=self.row, column=3, pady=pady_num)
		
	def minus_stat(self):
		'''Each call reduces the stat by 1, if the stat isn't already at min,
		and the character has spent stat points to refund, and updates the char info.'''
		change_stat = True
		if my_first_character.spent_stat_points == 0:
			messagebox.showinfo("Error", "No spent stat points to return.")
			change_stat = False
		elif self.stat == 'Strength':
			if my_first_character.strength == my_first_character.race.base_strength:
				messagebox.showinfo("Error", "Stat already at minimum.")
				change_stat = False
			else:
				my_first_character.strength -= 1
				self.stat_display.config(text = str(my_first_character.strength))
		elif self.stat == 'Dexterity':
			if my_first_character.dexterity == my_first_character.race.base_dexterity:
				messagebox.showinfo("Error", "Stat already at minimum.")
				change_stat = False
			else:
				my_first_character.dexterity -= 1
				self.stat_display.config(text = str(my_first_character.dexterity))
		elif self.stat == 'Constitution':
			if my_first_character.constitution == my_first_character.race.base_constitution:
				messagebox.showinfo("Error", "Stat already at minimum.")
				change_stat = False
			else:
				my_first_character.constitution -= 1
				self.stat_display.config(text = str(my_first_character.constitution))
		elif self.stat == 'Intelligence':
			if my_first_character.intelligence == my_first_character.race.base_intelligence:
				messagebox.showinfo("Error", "Stat already at minimum.")
				change_stat = False
			else:
				my_first_character.intelligence -= 1
				self.stat_display.config(text = str(my_first_character.intelligence))
		else:
			if my_first_character.wisdom == my_first_character.race.base_wisdom:
				messagebox.showinfo("Error", "Stat already at minimum.")
				change_stat = False
			else:
				my_first_character.wisdom -= 1
				self.stat_display.config(text = str(my_first_character.wisdom))
		
		if change_stat:
			my_first_character.spent_stat_points -= 1
			my_first_character.available_stat_points += 1
			update_char()
		
	def plus_stat(self):
		'''Each call increases the stat by 1, if the character has stat points
		to spend, and the stat isn't already at max, and updates the char info.'''
		max_stat = 255
		change_stat = True
		if my_first_character.available_stat_points < 1:
			messagebox.showinfo("Error", "Insufficient stat points.")
			change_stat = False
		elif self.stat == 'Strength':
			if my_first_character.strength == max_stat:
				messagebox.showinfo("Error", "Stat already at maximum.")
				change_stat = False
			else:
				my_first_character.strength += 1
				self.stat_display.config(text = str(my_first_character.strength))
		elif self.stat == 'Dexterity':
			if my_first_character.dexterity == max_stat:
				messagebox.showinfo("Error", "Stat already at maximum.")
				change_stat = False
			else:
				my_first_character.dexterity += 1
				self.stat_display.config(text = str(my_first_character.dexterity))
		elif self.stat == 'Constitution':
			if my_first_character.constitution == max_stat:
				messagebox.showinfo("Error", "Stat already at maximum.")
				change_stat = False
			else:
				my_first_character.constitution += 1
				self.stat_display.config(text = str(my_first_character.constitution))
		elif self.stat == 'Intelligence':
			if my_first_character.intelligence == max_stat:
				messagebox.showinfo("Error", "Stat already at maximum.")
				change_stat = False
			else:
				my_first_character.intelligence += 1
				self.stat_display.config(text = str(my_first_character.intelligence))
		else:
			if my_first_character.wisdom == max_stat:
				messagebox.showinfo("Error", "Stat already at maximum.")
				change_stat = False
			else:
				my_first_character.wisdom += 1
				self.stat_display.config(text = str(my_first_character.wisdom))
		
		if change_stat:
			my_first_character.spent_stat_points += 1
			my_first_character.available_stat_points -= 1
			update_char()
		

str_incrementor = stat_incrementor(top_right_frame, 'Strength', 0)
dex_incrementor = stat_incrementor(top_right_frame, 'Dexterity', 1)
con_incrementor = stat_incrementor(top_right_frame, 'Constitution', 2)
int_incrementor = stat_incrementor(top_right_frame, 'Intelligence', 3)
wis_incrementor = stat_incrementor(top_right_frame, 'Wisdom', 4)


def reload_stats():
	'''Resets the stats display to the most current character numbers'''
	str_incrementor.stat_display.config(text=str(my_first_character.strength))
	dex_incrementor.stat_display.config(text=str(my_first_character.dexterity))
	con_incrementor.stat_display.config(text=str(my_first_character.constitution))
	int_incrementor.stat_display.config(text=str(my_first_character.intelligence))
	wis_incrementor.stat_display.config(text=str(my_first_character.wisdom))
	

#*** Health and Mana totals ***
health_label = tkinter.Label(bottom_frame, text="Health")
health_label.grid(row=0, column=0, sticky=tkinter.E)
health_total = tkinter.Label(bottom_frame, text=str(my_first_character.health),
							relief=tkinter.SUNKEN)
health_total.grid(row=0, column=1, sticky=tkinter.W)

mana_label = tkinter.Label(bottom_frame, text="Mana")
mana_label.grid(row=1, column=0, sticky=tkinter.E)
mana_total = tkinter.Label(bottom_frame, text=str(my_first_character.mana),
						relief=tkinter.SUNKEN)
mana_total.grid(row=1, column=1, sticky=tkinter.W)


#*** Stat points available ***
stat_points_label = tkinter.Label(bottom_frame, text="Avaiable stat points")
stat_points_label.grid(row=2, column=0, sticky=tkinter.E)
stat_points_count = tkinter.Label(bottom_frame, 
								text=str(my_first_character.available_stat_points),
								relief=tkinter.SUNKEN)
stat_points_count.grid(row=2, column=1, sticky=tkinter.W)


pady_num = 5

#*** Print race bonuses ***
def print_race_bonus():
	'''Opens a message window with additional racial traits.'''
	messagebox.showinfo('Race traits', str(my_first_character.race.print_other_bonuses()))

race_bonuses_btn = tkinter.Button(bottom_frame, text='Racial bonuses',
									command=print_race_bonus)
race_bonuses_btn.grid(row=3, column=0, pady=pady_num)



#*** Update and Print char ***
def update_char():
	'''Runs the character.update_stats method, then redraws displays for hp, 
	mana, and stat points.'''
	my_first_character.update_stats()
	health_total.config(text = str(my_first_character.health))
	mana_total.config(text = str(my_first_character.mana))
	stat_points_count.config(text = str(my_first_character.available_stat_points))

print_char_button = tkinter.Button(bottom_frame, text='Print Character',
								   command=my_first_character.print_char)
print_char_button.grid(row=3, column=1, pady=pady_num)


# *** Messagebox ***
answer = messagebox.askquestion('Begin building?', 'Use this program to build '
								+ 'your character.\n Are you ready to get started?')
if answer == 'yes':
    print("Let's begin")
else:
	window.destroy()


window.mainloop()