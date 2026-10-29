"""
Python File Handling Basics
===========================
A hands-on practice project that walks through the essentials of working
with files in Python: reading, writing, analyzing data and deleting files.

Project parts
-------------
    Part 1 - Reading files     : open/close, the `with` statement, readlines()
    Part 2 - Writing files     : write mode, append mode, writelines()
    Part 3 - Sports analytics  : turn a CSV file into per-player statistics
    Part 4 - Removing files    : safely delete a file with the `os` module

Data files used (keep them in the same folder as this script)
-------------------------------------------------------------
    funny.txt  - a short joke, used for the reading exercises
    love.txt   - a sample text file, used for the writing exercises
    scores.csv - batting scores in the format  player,score
    dummy.txt  - created and deleted by the script (Part 4)
"""


# ===========================================================================
#   PART 1 OF 4  |  READING FILES
# ===========================================================================
#
#   Context:
#       Reading a file is the most common file operation. Python gives us
#       a few ways to do it; this part compares three of them using funny.txt.
#
#   File modes used here:
#       "r"  ->  read mode (the default). The file must already exist.
# ===========================================================================
 
# ---------------------------------------------------------------------------
# 1.1  Read a file line by line (manual open and close)
# ---------------------------------------------------------------------------
# open() returns a file object. Looping over it gives one line at a time,
# which is memory-friendly even for very large files.
print("=" * 60)
print("PART 1.1  |  Read a file line by line")
print("=" * 60)
 
f = open("funny.txt", "r")
for line in f:
    # Every line still ends with a newline character ("\n"), and print()
    # adds another one. That is why the output shows blank lines between
    # the lines. Use print(line, end="") to avoid the extra blank lines.
    print(line)
 
# We must close the file ourselves to release the system resource.
# Forgetting this line is a very common mistake, which is why the `with`
# statement below is the recommended approach.
f.close()
 
# Output:
# Teacher: Why are you late, raghu?
#
# Raghu: Because of the sign
#
# Teacher: What sign?
#
# Raghu: The one that says "School Ahead, Go slow"
 
 
# ---------------------------------------------------------------------------
# 1.2  The `with` statement (recommended)
# ---------------------------------------------------------------------------
# `with` is a context manager: it closes the file automatically when the
# block ends, even if an error occurs. No f.close() needed.
print("\n" + "=" * 60)
print("PART 1.2  |  The `with` statement")
print("=" * 60)
 
with open("funny.txt", "r") as f:
    for line in f:
        print(line)
 
# Output: (same as 1.1)
 
 
# ---------------------------------------------------------------------------
# 1.3  readlines(): load every line into a list
# ---------------------------------------------------------------------------
# readlines() reads the whole file at once and returns a list where each
# item is one line. Note that the "\n" at the end of each line is preserved.
print("\n" + "=" * 60)
print("PART 1.3  |  readlines()")
print("=" * 60)
 
with open("funny.txt", "r") as f:
    lines = f.readlines()
    print(lines)
 
# Output:
# ['Teacher: Why are you late, raghu?\n', 'Raghu: Because of the sign\n',
#  'Teacher: What sign?\n', 'Raghu: The one that says "School Ahead, Go slow"']
# (printed on a single line; wrapped here for readability)





# ===========================================================================
#   PART 2 OF 4  |  WRITING FILES
# ===========================================================================
#
#   Context:
#       Writing lets a program save its results. The file mode you choose
#       decides whether existing content is replaced or preserved.
#
#   File modes cheat sheet:
#       "r"  ->  Read    : file must exist; cannot write
#       "w"  ->  Write   : creates the file, or ERASES it if it exists
#       "a"  ->  Append  : creates the file, or adds to the END if it exists
#
#   This part uses love.txt.
# ===========================================================================
 
# ---------------------------------------------------------------------------
# 2.1  Write mode ("w")
# ---------------------------------------------------------------------------
# If love.txt already exists, its old content is erased before writing.
print("\n" + "=" * 60)
print("PART 2  |  Writing files")
print("=" * 60)
 
with open("love.txt", "w") as f:
    f.write("I love python")
 
# love.txt now contains:
# I love python
 
 
# ---------------------------------------------------------------------------
# 2.2  Write mode overwrites previous content
# ---------------------------------------------------------------------------
# Writing again in "w" mode replaces whatever was there before: the earlier
# line "I love python" disappears and only the new line remains.
with open("love.txt", "w") as f:
    f.write("I love javascript")
 
# love.txt now contains:
# I love javascript



# ---------------------------------------------------------------------------
# 2.3  Append mode ("a")
# ---------------------------------------------------------------------------
# Append mode keeps the existing content and adds new text at the end.
# Note: write() does not add a newline automatically, so the new text joins
# the previous line. Add "\n" yourself if you want it on a new line.
with open("love.txt", "a") as f:
    f.write("I love python")
 
# love.txt now contains:
# I love javascriptI love python
 
 
# ---------------------------------------------------------------------------
# 2.4  writelines(): write a list of strings
# ---------------------------------------------------------------------------
# writelines() writes every string in the list, one after another.
# It does NOT insert line breaks, so include "\n" where a new line is needed.
# This uses "w" mode, so it replaces the previous content as well.
with open("love.txt", "w") as f:
    f.writelines(["I love C++\n", "I love scala"])
 
# love.txt now contains:
# I love C++
# I love scala
 

