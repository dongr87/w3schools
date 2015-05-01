## Vim Note
this file is written by vim and to help me remember the basic use of vim.
let's start from the basic.

i'll use --> to represent an arrow.
[filename] to represent the filename without '[]'.
### about files (open, save, running on the background)
- vim --> open vim in the terminal.
- vim filename --> open file with selected filename
- vim + n filename --> open the [n]th line of file with filename and
- vim -R filename --> open file in READ-ONLY mode
- vimdiff fileA fileB --> find the difference of A and B
- :wq / :x --> write and quit
- ZZ --> save and quit
- :w filename --> save as
- :w /tmp/1 --> save to the temp file
- :saveas <path/to/file> --> save to the path
- :q! --> force quit
- ZQ --> force quit
- :e filename --> open filename, quit the current and jump in the filename
- :e! --> give up the modifies, reopen the current file
- :e --> reload the file
- ctrl-z / fg --> switch back to terminal
- :f / ctrl-g --> show file name, line number and current percentage.
- :!command --> quit vi and implement command, and switch back to vim
- :r!command --> put the output of the command line to current line
- :sh --> go back to terminal, *ctrl-d* to come back
- :X --> encrypt the file
- :version --> show vim version
- :f filename --> change the file name, create a duplicate file

### motion
- w --> next word
- W --> next word, without punctuation
- b --> previous word
- B --> previous word, without punctuation
- e --> end of word
- E --> end of word, without punctuation
- 0 --> begging of current line
- $ --> end of current line
- ^ --> move to the beginning of current line (unblank)
- g_ --> move to the end of current line (unblank)
- n+ --> move down [n]th line
- n- --> move up [n]th line
- G --> move to last line
- gg --> move to the first line
- nG / :n --> move to the [n]th line
- [[ --> beginning line
- ]] --> ending line
- H --> move cursor to the top line of screen
- M --> move cursor to the middle line of screen
- L --> move cursor to the last line of screen
- ( --> move to beginning of the sentence
- ) --> move to end of the sentence
- { --> move to beginning of the paragraph
- } --> move to end of the paragraph
- % --> move to the paired parenthesis
- * / # --> pair words, * for next and # for previous
- zf --> fold(with direction keys)
- zo --> unfold

