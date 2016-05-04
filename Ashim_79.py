#opening the file to read data
# assumption made every word is a valid word: So , I did not used regular expression to filter out whether it is valid word or not

import numpy as np #module that helps to work with arrays, Here it helps to plot the x-axis of my graph
import matplotlib.pyplot as plt #patplotlib module for plotting the graphs

#opening the file that we are evaluating, no need to provide full directory as the sample text is in our 
my_file = open('Sample.text')


my_dict = {}    #initializing the dictionary that stores the word as key and it's frequency as value

everylines = my_file.readlines() # reading everyline( i.e. line by line) and storing in variable called everylines

for i in range(len(everylines)):  #looping through the each line
    each_line = everylines[i].split()  # each_line stores the the array of words in each line
    for word in each_line: # going over each word in of the array each_line
        if word not in my_dict: # cheking to see if the word is in dictionary my_dict or not
            my_dict[word] =1   # if word is not already in dictionary, assign its value to 1
        else:
            current_value = my_dict.get(word) # if word is already in dictionary, first get the value of that key
            my_dict[word] = current_value+1  # now increase the value of that word by 1
            
        
# after the end of this loop every word in the text file will be assigned as a key of  my_dict and frequency as the value of my_dict



words = []   #initializing list that will store the words that we are about to plot
freq = []  #initializing list that will store the frequency of the given words

counter = 0 # initializing the counter, this counter will determine how many times the following loop will run
for w in sorted(my_dict, key=my_dict.get, reverse=True): #this will loop throught the sorted dictionary according to its value. "Reverse = True" will loop in descending order
  print w, my_dict[w]  # prints the words and respective frequency in descending order; i.e. the word with higest frequency gets printed first and the word with second highest frequency gets printed second and so on..
  words.append(w) # appending the respective word in list of words that we wish to plot
  freq.append(my_dict[w]) # appending the respective frequency in list of frequency that we wish to plot
  counter += 1 # increasing counter by 1 each time the iteration of loop increases
  if counter == 15: # this sets how many words we want to plot
      break     # break helps to break from the loop once the desired words are achieved
    
my_length = len(words)  # it stores the length of words that we want to plot
y_pos = np.arange(my_length) #  this gives the array of evenly spaced values within a given interval, so that to get evenly spaced points in y axis
 

plt.barh(y_pos, freq, align='center') #this plots the horizontal bar plot
plt.yticks(y_pos, words)
plt.xlabel('Frequency')
plt.ylabel('Words --> decreasing order of frequency')
plt.title('Words vs. Frequncy graph')

plt.show() 




