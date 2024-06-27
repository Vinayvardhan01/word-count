f = open(r"C:\python programmems simplicode\one.txt", "r") #file which contain the data
c = []         #empty list to shore individual elements

for x in f:
      c.extend(x.strip().split()) #storing individual word as a list

f.close()

print(c)    # Print the list of words

word_count = len(c) # the count will equal to the length

print("The number of words:", word_count) # Print the number of words

