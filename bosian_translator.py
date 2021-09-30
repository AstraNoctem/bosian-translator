def translate(string):
	string = string
	splitString = [char for char in string]
	endTranslation = ''
	indexNum = -1
	for v in splitString:
		indexNum += 1
		
		# lowercase
		if v == 'a':
			endTranslation = endTranslation + 'g'
		elif v == 'b':
			endTranslation = endTranslation + 'e'
		elif v == 'c':
			endTranslation = endTranslation + 's'
		elif v == 'd':
			endTranslation = endTranslation + 'h'
		elif v == 'e':
			endTranslation = endTranslation + 'l'
		elif v == 'f':
			endTranslation = endTranslation + 'j'
		elif v == 'g':
			endTranslation = endTranslation + 'r'
		elif v == 'h':
			endTranslation = endTranslation + 't'
		elif v == 'i':
			endTranslation = endTranslation + 'f'
		elif v == 'j':
			endTranslation = endTranslation + 'q'
		elif v == 'k':
			endTranslation = endTranslation + 'a'
		elif v == 'l':
			endTranslation = endTranslation + 'x'
		elif v == 'm':
			endTranslation = endTranslation + 'z'
		elif v == 'n':
			endTranslation = endTranslation + 'v'
		elif v == 'o':
			endTranslation = endTranslation + 'n'
		elif v == 'p':
			endTranslation = endTranslation + 'k'
		elif v == 'q':
			endTranslation = endTranslation + 'y'
		elif v == 'r':
			endTranslation = endTranslation + 'o'
		elif v == 's':
			endTranslation = endTranslation + 'p'
		elif v == 't':
			endTranslation = endTranslation + 'i'
		elif v == 'u':
			endTranslation = endTranslation + 'd'
		elif v == 'v':
			endTranslation = endTranslation + 'm'
		elif v == 'w':
			endTranslation = endTranslation + 'w'
		elif v == 'x':
			endTranslation = endTranslation + 'c'
		elif v == 'y':
			endTranslation = endTranslation + 'b'
		elif v == 'z':
			endTranslation = endTranslation + 'u'
		
		# uppercase
		elif v == 'A':
			endTranslation = endTranslation + 'G'
		elif v == 'B':
			endTranslation = endTranslation + 'E'
		elif v == 'C':
			endTranslation = endTranslation + 'S'
		elif v == 'D':
			endTranslation = endTranslation + 'H'
		elif v == 'E':
			endTranslation = endTranslation + 'L'
		elif v == 'F':
			endTranslation = endTranslation + 'J'
		elif v == 'G':
			endTranslation = endTranslation + 'R'
		elif v == 'H':
			endTranslation = endTranslation + 'T'
		elif v == 'I':
			endTranslation = endTranslation + 'F'
		elif v == 'J':
			endTranslation = endTranslation + 'Q'
		elif v == 'K':
			endTranslation = endTranslation + 'A'
		elif v == 'L':
			endTranslation = endTranslation + 'X'
		elif v == 'M':
			endTranslation = endTranslation + 'Z'
		elif v == 'N':
			endTranslation = endTranslation + 'V'
		elif v == 'O':
			endTranslation = endTranslation + 'N'
		elif v == 'P':
			endTranslation = endTranslation + 'K'
		elif v == 'Q':
			endTranslation = endTranslation + 'Y'
		elif v == 'R':
			endTranslation = endTranslation + 'O'
		elif v == 'S':
			endTranslation = endTranslation + 'P'
		elif v == 'T':
			endTranslation = endTranslation + 'I'
		elif v == 'U':
			endTranslation = endTranslation + 'D'
		elif v == 'V':
			endTranslation = endTranslation + 'M'
		elif v == 'W':
			endTranslation = endTranslation + 'W'
		elif v == 'X':
			endTranslation = endTranslation + 'C'
		elif v == 'Y':
			endTranslation = endTranslation + 'B'
		elif v == 'Z':
			endTranslation = endTranslation + 'U'

		# s p a c e s
		elif v == ' ':
			endTranslation = endTranslation + ' '
		else:
			endTranslation = endTranslation + v
	print(endTranslation)
		
translate("Bosia")
