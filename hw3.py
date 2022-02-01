#Homework 3 
#Created by Nathan Heckman

#Code sources found in hw3.txt

import math #Need to get approximation of pi
import os.path   #Needed for integration with operating system
import csv #Neeed to read CSV into program

current_directory = os.path.join(os.getcwd(), 'hw3') #Specify the current working directory for the program
os.chdir(current_directory) #Change the current working directory for the remainder of the program

vowels = "aeiou"
constonants = "bcdfghjklmnpqrstvwxyz"
pi = math.pi

def main():
  #Question 1
  print(consonants("ohio")) #More vowels than constonants. True
  print(consonants("fourty")) #More constonants than vowels. False
  print(consonants("book")) #Equal number of vowels and constonants. None

  #Question 2
  print(volume(10,10))

  #Question 3
  print(combine_string_list(['these','are','seperated','by','comma']))

  #Question 4  
  print("List of Lists Added to the Following File:", 
  string_lists_to_csv([['these','are'],['going','to'],['the','seperate'],['CSV', 'file']]))

  #Question 5
  print(csv_to_string_lists("strings.csv"))
  #Question 6
  print(divide(16,4)) #Returns the division of the numbers
  print(divide(10,0)) #Returns exception due to 0 being the divisor

  #Question 7
  print(no_duplicates([1,1,1,1,1])) # Should be [1]
  print(no_duplicates([1,2,3,4,5,5,4,3,2,1])) # Should be [1,2,3,4,5]

  #Question 8
  create_directory("hw3-folder") #Creates the hw3-folder directory within hw3 unless it already exists

#Question 1
def consonants(word):
  vowelCount = 0 #Initialize vowel and constonant counting
  constonantCount = 0
  for letter in word: #For each letter in the word, increment vowelCount or constonantCount
    if letter in vowels:
      vowelCount += 1
    if letter in constonants:
      constonantCount += 1
  if constonantCount == vowelCount: #Return appropriate values based on requested conditions
    return None
  if constonantCount > vowelCount:
    return False
  else:
    return True
#Question 2
def volume(radius,height):
  return (pi * radius * radius * height) #Followed formula from homework page
#Question 3
def combine_string_list(strings):
    return ','.join(strings)
#Question 4
def string_lists_to_csv(list_of_lists):
    file = open("strings.csv","w") #Create strings.csv file if it doesn't already exist
    for list in list_of_lists: #For each list within the list...
        file.write(combine_string_list(list)) #Write each list to the given file
        file.write("\n") #Ensures each list is on its own row
    return os.path.realpath("strings.csv") #Return the location of strings.csv    
#Question 5
def csv_to_string_lists(csv_file):
    file = open(csv_file) #Open the CSV file
    reader = csv.reader(file) #Begin reading the CSV file
    strings = [] #Initialize the list of lists
    for row in reader: #For each row that was read...
        strings.append(row) #Append the row to the list of lists
    return strings
#Question 6
def divide(a,b):
  try:
    return a / b
  except: #Only impossible division is if the divisor is 0
    return "Divisor cannot be 0"
#Question 7
def no_duplicates(list):
  nums = []
  [nums.append(x) for x in list if x not in nums] #For each number in the given list, add it to nums if it doesn't already exist in nums
  return nums
#Question 8
def create_directory(name):
    global current_directory #Use the globally defined current working directory
    new_directory = os.path.join(current_directory, name) #Specify the desired directory to be created
    if not os.path.exists(new_directory): #If the directory doesn't already exist...
        os.mkdir(new_directory) #Create the directory with the given name
        print(name, "created inside present working directory")
    else:
        print(name, "already exists inside present working directory")

if __name__ == "__main__": #Run main function after everything is initialized
  main()

# Sources used to complete HW3:
# https://stackoverflow.com/questions/14125781/new-folder-that-is-created-inside-the-current-directory
# https://note.nkmk.me/en/python-string-concat/#:~:text=The%20string%20method%20join(),strings%20into%20a%20single%20string.&text=Call%20join()%20method%20from,makes%20a%20comma%2Ddelimited%20string.
# https://flexiple.com/python-get-current-directory/
# https://www.w3schools.com/python/python_file_write.asp
# https://www.tutorialkart.com/python/python-write-string-to-text-file/
# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
# https://stackoverflow.com/questions/423379/using-global-variables-in-a-function