# determine if string has all unique characters
test_string_fail = "apples"
test_string_pass = "dkcote"

def check_string_unique(string):
    for letter in string:
        if string.count(letter) > 1:
            return "fails"

    return "passes"

# given two strings, determine if one is a permutation of another
test_string1_fail = "apples"
test_string2_fail = "dkcote"
test_string1_pass = "apples"
test_string2_pass = "selpap"

def check_string_permutation(string1, string2):
    string1_chars = {}

    for char in string1:
        string1_chars[char] = string1.count(char)

    for char in string2:
        if char not in string1_chars:
            return "fails"
        elif string2.count(char) != string1_chars[char]:
            return "fails"

    return "passes"

# replace all spaces with '%20'
urlify_test_string = "The quick brown fox jumps over the lazy dog."
urlify_solution_string = "The%%20quick%%20brown%%20fox%%20jumps%%20over%%20the%%20lazy%%20dog."

def urlify(string):
    i = 0

    while i < len(string):
        if string[i] == " ":
            string = string[0:i] + "%%20" + string[i + 1:]

        i += 1

    return string

# tests
# uniqueness
print "check string for uniqueness tests"
print "passing test string should print passes"
print check_string_unique(test_string_pass)
print "failing test string should print fails"
print check_string_unique(test_string_fail)

# permutations
print "check string for permutation tests"
print "passing test string should print passes"
print check_string_permutation(test_string1_pass, test_string2_pass)
print "failing test string should print fails"
print check_string_permutation(test_string1_fail, test_string2_fail)

# urlify
print "check urlify"
print "test case should print:"
print urlify_solution_string
print "urlify returns:"
print urlify(urlify_test_string)
