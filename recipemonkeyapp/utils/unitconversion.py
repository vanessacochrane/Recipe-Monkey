
def convertToGrams(q,m):
	
	"""
		1 tablespoon = 3 teaspoons
		1 cup = 16 tablespoons
	"""
	
	weight_tablespoon=15
	
	m=m.lower().strip()
	
	if m=='teaspoon' or m=='teaspoons' or m=='tsp':
		return (q*weight_tablespoon)/3

	
	if m=='tablespoon' or m=='tablespoons' or m=='tbsp':
		return q*weight_tablespoon

	if m=='cups' or m=='cup':
		return q*weight_tablespoon*16

	return q
	
	