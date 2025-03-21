def remove_duplicet(items):
  unique = []
  for item in items:
      if item not in unique :
        unique.append(item)
  return unique 
      
number =[12,2,4,7,9,78,20,2,12]
print (remove_duplicet(number))
