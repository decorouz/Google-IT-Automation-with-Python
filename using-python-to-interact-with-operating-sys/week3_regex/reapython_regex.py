import re

s = "foo123bar"
re.search("[0-9][0-9][0-9]", s)

re.search('[0-9][0-9][0-9]', 'foo456bar')
# <_sre.SRE_Match object; span=(3, 6), match='456'>

# the dot(.) metacharacter. Matching any character except a new line
result = re.search("1.3", s)

# Metacharacters That Match a Single Character

# The metacharacter sequence [artz] matches any single 'a', 'r', 't', or 'z' character
re.search('ba[artz]', 'foobarqux')

# A character class can also contain a range of characters separated by a hyphen (-)
re.search('[a-z]', 'FOObar')


re.search('[^0-9]', '12345foo')
# the first character that isnt a digit

re.search('[-abc]', '123-456')
# <_sre.SRE_Match object; span=(3, 4), match='-'>

# print(re.search(r'[\]]', 'foo[1]'))


# \w matches any alphanumeric word character. Word characters are uppercase and lowercase letters, digits, and the underscore (_) character, so \w is essentially shorthand for [a-zA-Z0-9_]:

re.search('\w', '#(.a$@&')
# return <_sre.SRE_Match object; span=(3, 4), match='a'>

# \W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]:

re.search('\W', 'a_13*Qb')
# return <_sre.SRE_Match object; span=(3, 4), match='*'>


# \d matches any decimal digit character. \D is the opposite. It matches any character that isn’t a decimal digit:
re.search('\d', 'abc4def')
# match <_sre.SRE_Match object; span=(3, 4), match='4'>
# \d is essentially equivalent to [0-9]


# \s matches any whitespace character:
re.search('\s', 'foo bar baz')

# Escaping Metacharacters
re.search('.', 'foo.bar')
# return <_sre.SRE_Match object; span=(0, 1), match='f'>
re.search('\.', 'foo.bar')


# Anchors: An achor dictates a particular location in the search string where a match must occur.

re.search('^foo', 'foobar')
# <_sre.SRE_Match object; span=(0, 3), match='foo'>
re.search('^foo', 'barfoo')
# return None


# $
re.search('bar$', 'foobar')
# return <_sre.SRE_Match object; span=(3, 6), match='bar'>


# Quantifiers : A quantifier metacharacter immediately follows a portion of a <regex> and indicates how many times that portion must occur for the match to succeed.

# *
# Matches zero or more repetitions of the preceding regex.
re.search('foo-*bar', 'foobar')  # Zero dashes
# return <re.Match object; span=(4, 5), match='*'>

re.search(r'foo-*bar', 'foo-bar')  # One dash

re.search('foo.*bar', '# foo $qux@grault % bar #')


# Grouping Constructs and Backreferences
print(re.search('(ba[rz]){2,3}(qux)?', 'bazbarbazqux'))

# The following example shows that you can nest grouping parentheses:

re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar')
# return <_sre.SRE_Match object; span=(0, 9), match='foofoobar'>

# Capturing Groups
