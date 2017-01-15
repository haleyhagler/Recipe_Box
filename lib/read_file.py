#################################################################################
# CREATOR:   HALEY HAGLER
# DATE:      JANUARY 2017
# TITLE:     read_file.py
# PURPOSE: 	TO USE REGEX TO SEARCH THE TEXT FILE FOR ELEMENTS OF A RECIPE
################################################################################
import re 									# The regex package
from helpful import remove_non_ascii 		# Removes  non-ascii elements for Regex
from helpful import next_important_line 	# Skips blank lines
from Recipe import Recipe 					# The format for what a recipe is 

def read_file(file_name, recipe):

	recipe = Recipe()
	f = open(file_name, 'r')
	title = remove_non_ascii(f.readline())
	print 'Title: {}'.format(title)
	comp = remove_non_ascii(f.readline())
	while comp:
		
		print 'comp:    {}'.format(comp)
		cook = re.search( r'Cook\s*time', comp, re.I)
		prep = re.search( r'Prep\s*time', comp, re.I)
		total = re.search( r'Total\s*time', comp, re.I)
		ingr = re.search(r'Ingredients', comp, re.I)

		if cook:
			cook_time = next_important_line(comp, f)
		if prep:
			prep_time = next_important_line(comp, f)
		elif total:
			total_time = next_important_line(comp, f)
		elif ingr:
			Ingredients = next_important_line(comp, f)
		
		comp = remove_non_ascii(f.readline())

	print 'Cook Time:  {}'.format(cook_time) 
	print 'Prep Time:  {}'.format(prep_time) 
	print 'Total Time: {}'.format(total_time)
	print 'Ingredients:{}'.format(Ingredients)