def get_ancestors(taxon):
##dictionary for taxonmony
	tax_dict = {'Subspecies' : 'Subseries', 'Subseries' : 'Series', 'Series' :'Subsectio', 'Subsectio' : 'Sectio', 'Sectio': 'Subgenus', 'Subgenus' : 'Genus', 'Genus': 'Tribus' , 'Tribus' : 'Subfamilia' , 'Subfamilia' : 'Familia'} 
##recursion
	result = [taxon]
	while taxon != 'Familia' :
		result.append(tax_dict.get(taxon))
		taxon = tax_dict.get(taxon)
	return result
	
a= get_ancestors('Subseries')
for i in a:
	print(i)

