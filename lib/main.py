#################################################################################
# CREATOR:   HALEY HAGLER
# DATE:      JANUARY 2017
# TITLE:     main.py
################################################################################

from helpful import convert_pdf_to_txt      # Converts the original PDF to a texts file 
from read_file import read_file 			# Output a Recipe



path = '../Recipes/Vegetable.pdf'
convert_pdf_to_txt(path)
recipe = 1
read_file("out_put.txt", recipe)

