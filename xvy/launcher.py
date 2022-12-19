#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random,sys

from rich.console import Console
console = Console()

DATE = "19 December 2022"
VERSION = "0.3.0"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"
THISPROG = sys.argv[0].replace("./","")
WHATISTHIS_p1 = f"\n\t{THISPROG}: DEFINITION."
WHATISTHIS_p2 = "\t Use option '-h' for more glorification about this amazing project!\n"


# Bold colour list
colour_list =['\033[1;30m','\033[1;31m', '\033[1;32m','\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m', '\033[1;90m', '\033[1;91m', '\033[1;92m','\033[1;93m', '\033[1;94m', '\033[1;95m', '\033[1;96m', '\033[1;97m',]

colorWords_list = ["bold bright_black", "bold bright_red","bold bright_green","bold bright_yellow","bold bright_blue","bold bright_magenta", "bold bright_cyan","bold bright_white"]

banner0_str ="""
\t ████████████████████████████████████████████████████████████████████████████████
\t ███████████████████████████████&################(███████████████████████████████
\t ████████████████████████████########################&███████████████████████████
\t ██████████████████████████#############################█████████████████████████
\t ███████  ███████  ██████################################████████   ████████  .██
\t ████████  #██%  ███████####   #######   ###       #######&███████.  █████  #████
\t █████████     ████████(#####  ,#####.  ##  ,######  ######████████%  ██  ███████
\t █████████    █████████#######  (###(  ####    (###########██████████   █████████
\t ███████  ███  #███████########  ###  ##########()    ######██████████  █████████
\t ████*  ██████   ███████########  V  #####  #######  ######█████████   ██████████
\t ██   █████████.  ███████########   #######         ######██████████  ███████████
\t █████████████████████████##############################█████████████████████████
\t ███████████████████████████##########################███████████████████████████
\t ██████████████████████████████(###################██████████████████████████████
\t ████████████████████████████████████&(#####(████████████████████████████████████
"""


# banner ref: https://manytools.org/hacker-tools/convert-image-to-ansi-art/go/

banner1_str ="""
\t\t\t\t    ██╗  ██╗██╗   ██╗██╗   ██╗   
\t\t\t\t ██╗╚██╗██╔╝██║   ██║╚██╗ ██╔╝██╗
\t\t\t\t ╚═╝ ╚███╔╝ ██║   ██║ ╚████╔╝ ╚═╝
\t\t\t\t ██╗ ██╔██╗ ╚██╗ ██╔╝  ╚██╔╝  ██╗
\t\t\t\t ╚═╝██╔╝ ██╗ ╚████╔╝    ██║   ╚═╝
\t\t\t\t    ╚═╝  ╚═╝  ╚═══╝     ╚═╝      
                                
"""
# banner ref: https://manytools.org/hacker-tools/ascii-banner/

def get_platformType():
	"""Function to dermine the OS type."""
	platforms = {
	'darwin' : 'OSX',
	'win32'  : 'Windows',
	'linux1' : 'Linux',
	'linux2' : 'Linux'}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]
# end of get_platformType()


def helper():

	"""Cheap online help; how to use the program"""
	# h_str1 = "\t"+ BIBlue + DATE+" | version: "+VERSION + White
	# h_str2 = "\t"+ BIBlue + AUTHOR +"\n\tmail: "+AUTHORMAIL + White

	h_str1 = f"\t {DATE} | version: {VERSION}"
	h_str2 = f"\t {AUTHOR} | mail: {AUTHORMAIL}"


	print("\t "+len(h_str2) * "-")
	console.print(h_str1, style = "bold bright_green")
	print("\t "+len(h_str2) * "-")
	console.print(h_str2, style = "bold bright_green")
	print("\t "+len(h_str2) * "-")

	# console.print("\t :coffee:")
	console.print(banner0_str, style = random.choice(colorWords_list))
	console.print(banner1_str, style = random.choice(colorWords_list))

	console.print("\n\t XVY: A simple regression analysis tool", style = "bold bright_blue")
	platform_str = get_platformType()
	print("\n\t OS type: ",platform_str) # Print the OS type; useful for if keeping a log

	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		console.print("\t \U0001f5ff \U0001F608" * 10, style = "Green")
		
		console.print(f"\t [+] \U0001f600 USAGE:  poetry run {THISPROG} --data-file input/majors.csv", style= "bold bright_green")

	else:
		print("\n\t+ :-) ", command_str)

# end of helper()

