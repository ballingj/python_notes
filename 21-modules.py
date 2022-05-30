"""
Modules: python files that contain codes that can
be re-used in other files.
Types:  built-ins, custom, 3rd party
"""

# importing built-in modules:
####################################

# import the specific module
#import random

# importing a specific object from a module
from translate import Translator
import art  # https://pypi.org/project/art/
from random import randint

from math import sin, cos, tan

# calling that specific object from a module
print(randint(1,6))

# renaming modules : creating an alias
import random as rand


# creating custom modules:
####################################
# create a separate file in the same directory
# create some variables and or function in that file
# import the module or the specific objects
#####################################################
from utils import brand_colors, mean
#import utils

print(brand_colors)
print(mean([2,4,5,7,22,45,99]))

#############################################################################
# third party modules
# https://packaging.python.org/en/latest/tutorials/installing-packages/
# https://pypi.org/
#
##############################################################################

# doc:  pypi.org/project/art 
# pip install art
###################################
import art    

print(art.art("woman"))
print(art.art("coffee"))
print(art.randart())

print(art.text2art("Jeff"))

# Return ASCII text with block font
Art = art.text2art("Jeff", font='block', chr_ignore=True)
print(Art)

# doc: pypi.org/project/translate/
####################################
# import translate
# pip install translate
#################################
from translate import Translator
translator = Translator(to_lang="fr")
translation = translator.translate("Hello World!")
print(translation)

print(art.text2art("Ministry of Work"))