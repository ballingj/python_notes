# string strip
'   spacious   '.strip() # 'spacious'
'   spacious   '.strip(" s") # 'paciou'
'   spacious   '.lstrip() # 'spacious   '
'   spacious   '.rstrip()  # '   spacious'


# Replace
# str.replace(old. new, [count])
races = '3kilometers 5kilometers 10kilometers 41kilometers'

races.replace('kilometers', 'miles')  # '3miles 5miles 10miles 41miles'

races.replace('kilometers', 'km')  # '3km 5km 10km 41km'

prices = '$1.99 $9.99 $7.25'

prices.replace('$', '')  # '1.99 9.99 7.25'

prices.replace('$', '', 1)  # '1.99 $9.99 $7.25'

prices.replace('$', '', 2)  # '1.99 9.99 $7.25'

# Find
# str.find(sub[, start[, end]])

prices.find('$') # 0
prices.find('$', 1) # 6
prices.find('$', 7) # 12

# chaining methods together 
email = '  toGG@email.com  '
email.strip().lower()   # 'togg@email.com'

# len() to gives out the length of string
len("Hello World")  # 11
