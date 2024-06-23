from pathlib import Path
import re
from json import loads
import variables
from typing import ClassVar


class Highlighter:
	class Database:
		path = Path(variables.full_path + "/cogs/message_commands/database.json")
		database_content = loads(path.read_text())
		color_codes = database_content["color_codes"]
		commands = database_content["commands"]
		regexes: ClassVar[dict] = {
			"general": {
				"link-comment": r'(?m)^# ?[#~>].*$',
				"comment": r'(?m)^#.*$',
				"string": r'(?<!\\)(?:"(?:\\.|[^"])*"|\'(?:\\.|[^\'])*\')',
				"macro": r'\$\([a-zA-Z0-9_-]*\)',
				"path": r'[\.\-_A-Za-z]+:[\.\-_A-Za-z]+',
				"selector": r'[#@$][a-zA-Z0-9]+',
				"number": r'[~^|0-9]+\.?[0-9]*[bdfs]?(?=[^%])',
				"text": r'[A-Za-z_\-\.]+'
			},
			"extended": {
				"nbt_parts": r'(\\\n|\$\([a-zA-Z0-9_-]*\)|string[0-9]+|[a-zA-Z_]\w*|[0-9]+.?[0-9]*[bdfs]?|[\[\]{},:;])'
			}
		}
	root_command = ""

	def remove_duplicates(list):
		unique_list = []
		for item in list:
			if item not in unique_list:
				unique_list.append(item)
		return unique_list

	def highlight(function):
		function_elements = Highlighter.general_lexer(function)
		return Highlighter.colorizer(function, function_elements)

	def brackets_slice(brackets_type, slice_string, replace_slices, replace_string=""):
		slices = []
		current_slice = ""
		brackets_count = 0
		strings = []
		for index, char in enumerate(slice_string[0]):
			if len(strings) >= 1:
				if char == strings[-1] and slice_string[0][index-1: index] != "\\":
					strings.pop(-1)
				current_slice += char
			elif char in "\"'":
				strings.append(char)
				current_slice += char
			elif char == brackets_type[0]:
				brackets_count += 1
				current_slice += char
			elif char == brackets_type[1]:
				brackets_count -= 1
				current_slice += char
				if brackets_count == 0:
					slices.append(current_slice)
					if replace_slices:
						slice_string[0] = slice_string[0].replace(current_slice, replace_string.format(len(slices) - 1))
					current_slice = ""
			elif brackets_count >= 1:
				current_slice += char
		return slices

	def general_lexer(function):
		Highlighter.function_copy = function + " "
		regexes = Highlighter.Database.regexes["general"]
		function_elements = {
			"link-comment": [],
			"comment": [],
			"selector_filter": [],
			"nbt": [],
			"string": [],
			"macro": [],
			"path": [],
			"number": [],
			"selector": [],
			"text": [],
			"command": [],
			"subcommand": [],
			"backslash": ["\\\n"]
		}
		def cut_by_regex(matches_list, regex):
			function_elements[matches_list] = Highlighter.remove_duplicates(re.findall(regex, Highlighter.function_copy))
			for match in function_elements[matches_list]:
				Highlighter.function_copy = Highlighter.function_copy.replace(match, "")
		# Lexing
		temp = [Highlighter.function_copy]
		function_elements["nbt"] = Highlighter.brackets_slice("{}", temp, True)
		function_elements["selector_filter"] = Highlighter.brackets_slice("[]", temp, True)
		for name, regex in regexes.items():
			cut_by_regex(name, regex)
		return function_elements

	def colorizer(function, function_elements):
		# Shortcuts
		colors = Highlighter.Database.color_codes
		possible_commands = Highlighter.Database.commands
		multiple_colors_types = Highlighter.Database.multiple_colors_types
		# Extending command_elements with commands and subcommands
		possible_subcommands = []
		for word in list(function_elements["text"]):
			if word in possible_commands:
				function_elements["command"].append(word)
				function_elements["text"].remove(word)
				possible_subcommands += possible_commands[word]["subcommands"]
			elif word in possible_subcommands:
				function_elements["subcommand"].append(word)
				function_elements["text"].remove(word)
		# ✨ Colorizing
		raw_nbt_thing = '|(?=\u001b)'
		for type, tokens in function_elements.items():
			for token in tokens:
				if type not in multiple_colors_types:
					function = re.sub(f"(?m)(?:(?<=\\s)|(?<=^)){token}(?:(?=\\s)|(?=$){raw_nbt_thing if type in 'text selector' else ''})", f"{colors[type]}{token}", function)
				else:
					function = function.replace(token, multiple_colors_types[type](token))
		return function

	def selector_filter(filters):
		# Shortcut
		colors = Highlighter.Database.color_codes
		# Main
		temp = [filters]
		nbts = Highlighter.brackets_slice("{}", temp, True, "%%%nbt{0}%%%")
		highlighted = temp[0].replace("[", f"{colors['bracket0']}[{colors['key']}")\
			.replace("]", f"{colors['bracket0']}]")\
			.replace("=", f"{colors['delimiter']}={colors['value']}")\
			.replace(",", f"{colors['delimiter']},{colors['key']}")\
			.replace("!", f"{colors['delimiter']}!{colors['value']}")\
			.replace("..", f"{colors['bracket1']}..{colors['value']}")\
			.replace("#", f"{colors['selector']}#")
		for index, tag in enumerate(nbts):
			highlighted = highlighted.replace(f"%%%nbt{index}%%%", tag)
		return highlighted

	def nbt(tag, brackets_depth=-1):
		colors = Highlighter.Database.color_codes
		# Strings are highlighted separately bc they has really hard regex and idk
		# if there a way to put it into nbt regex
		string_re = Highlighter.Database.regexes["general"]["string"]
		strings = re.findall(string_re, tag)
		for index, string in enumerate(strings):
			tag = tag.replace(string, f"string{index}")
		def lexer(tag, brackets_depth):
			tokens = []
			nbt_re = Highlighter.Database.regexes["extended"]["nbt_parts"]
			for match in re.finditer(nbt_re, tag):
				token = match.group()
				if token[0].isdigit() or token in "BIL":
					tokens.append((token, "value"))
				elif token[:6] == "string":
					tokens.append((token, "string"))
				elif token in "[{":
					brackets_depth += 1
					brackets_depth %= 3
					tokens.append((token, f"bracket{brackets_depth}"))
				elif token in "}]":
					tokens.append((token, f"bracket{brackets_depth}"))
					brackets_depth -= 1
					brackets_depth %= 3
				elif token in ':,;':
					tokens.append((token, "delimiter"))
				elif token[:2] == "$(":
					tokens.append((token, f"bracket{(brackets_depth + 1) % 3}"))
				elif token == "\\\n":
					tokens.append((token, "backslash"))
				else:
					tokens.append((token, "key"))
			return tokens
		lexed = lexer(tag, brackets_depth)
		highlighted = ''
		for token, type in lexed:
			if token[:2] == "$(":
				highlighted += f"{colors['macro']}${colors[type]}({colors['text']}{token[2:-1]}{colors[type]})"
			elif type == "string":
				highlighted += f"{colors['string']}{strings[int(token.replace('string', ''))]}"
			else:
				highlighted += colors[type] + token
				if type == "delimiter":
					highlighted += " "
		return highlighted

	def macro(macro):
		colors = Highlighter.Database.color_codes
		return f"{colors['macro']}${colors['bracket0']}({colors['text']}{macro[2:-1]}{colors['bracket0']})"

Highlighter.Database.multiple_colors_types = {"selector_filter": Highlighter.selector_filter, "nbt": Highlighter.nbt, "macro": Highlighter.macro}