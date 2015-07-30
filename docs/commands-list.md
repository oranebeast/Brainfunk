Basic Documentation (view raw)
==========

Brainfuck-to-Brainfunk
----------


Traditional Brainfuck to Brainfunk
----------

	> 	Toot	Move the pointer to the right
	< 	Doot 	Move the pointer to the left
	+ 	TootToot 	Increment the memory cell under the pointer
	- 	DootDoot 	Decrement the memory cell under the pointer
	. 	Parp 	Output the character signified by the cell at the pointer
	, 	Honk 	Input a character and store it in the cell at the pointer
	[ 	Plap 	Jump past the matching Blap if the cell under the pointer is 0
	] 	Blap 	Jump back to the matching Plap

Brainfunk-only commands
----------

	TootTootToot 	adds ten to cell
	TootTootTo	adds five to cell
	DootDootDoot    removes ten from cell
	DootDootDo	removes five from cell
	Brap		Sets cell to 0
	Prap		Sets cell to 255
