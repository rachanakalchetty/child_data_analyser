# Name: Rachana Kalachetty
# StudentID: 29562449
# Start date: 30th sep 2018
# Last modified date: 12th oct 2018
# In this task, preprocessing is done. The first step is to open the original file "SLI-1.txt" and read the contents of file.
# The second step is to extract "*CHI:" statements. This is done using regex and is written to the intermediate file "SLI_chi-1.txt".
# The third step is to apply all the filtering tasks to the SLI_chi.txt and the filtered version is written to a new file "SLI_cleaned-1.txt"
# The last step is to apply step 2 and 3 to all the 10 SLI and TD transcripts.
import re

# This function is used to extract "*CHI:" statements from the "SLI-1.txt"
def extract_CHI(filename1,filename2):
    # It takes two parameters filename1 is the name of the original file and
    # filename2 is the name of the intermediate file where extracted CHI statements needs to be written
    with open(filename1,'r') as file:  # opens the file in read mode
        input_file = file.read() # reads the contents of the file as string
        # re.findall() takes two parameters , 1st parameter - regex , 2nd parameter - the input file on which the regex needs to be applied
        result = re.findall('\*CHI:.*\n?[^%:]*[\.\!\?\]]', input_file) #This regex extracts th "*CHI:" statements including multiline statements
    # The re.findall() returns a list of words by splitting each statement into a list of words
    file.close() #closing the file
    with open(filename2, "w+") as file: #opens the intermediate file
        for line in result: # The regex is applied on the whole file contents
            file.write(line) # The extracted statements are written line by line
            file.write("\n") # Every line is written in new line
    file.close()

# This function is used for applying all the filters
def filtering(filename2,filename3):
    # It takes two parameters filename2 is the name of the  file where extracted CHI statements are present
    # filename3 - is the cleaned file where after applying filters , contents needs to be written here
    with open(filename2,'r') as file: #opens the intermediate file
        input_file = file.read()
        # re.sub() takes 3 parameters , 1st parameter - Regex to search for contents that are to be replaced
        # 2nd parameter - to be replaced with
        #3rd parameter - the input file or the contetnts on which this function is to be applied
        result = re.sub("\*CHI:", "", input_file.rstrip())  # to remove "*CHI:"
        result_a = re.sub("\[.[\*\w\s:?'\^\!\"]+\]", '', result) # to remove words that have prefix "[" or "]" as suffix and remove "[]" symbols as well.
        result_sp = re.sub("\[.[^\\][\s\/\w]+\]", '', result_a)  # for special cases where words don't match within [] and start with "^"
        result1_a = re.sub('\[[?!]\]', '', result_sp) # removes single symbol inside [] eg: [?] or [!]
        result2_a = re.sub('\[.\-\]', '', result1_a) # removes [/-]
        result_b = re.sub('[<>]', '', result2_a)  #removes the "<" and >" but retains words within it
        result_d = re.sub('\(([\w]*[^\.])\)', r'\1', result_b) # removes "(" and ")" but retains words inside it and also (.) but retains (..),(...)
        result_c = re.sub('[^* m: +ed][+&=][^\s]+', '', result_d) #removes words with prefix "&" or "+" but doesnt remove "[* m:+ed]
        result_c1 = re.sub('\+\/', '', result_c) #special case for removing "+/"
        result_c2 = re.sub('\+\/\/', '', result_c1) #special case for removing "+//"
    file.close()
    with open(filename3, "w+") as file:
        for line in result_c2:
            file.write(line)
    file.close()

# This function takes filename for all 10 transcripts of TD
def TD():
    for i in range(1,11): # It takes all the filenames from TD-1 to TD-10
        filename1 = "TD-" + str(i) + ".txt"
        filename2 = "TD_CHI/TD_CHI-" + str(i) + ".txt"
        filename3 = "TD_cleaned/TD_cleaned-" + str(i) + ".txt"
        extract_CHI(filename1,filename2) # calling the function to extract "*CHI:" statements for TD transcripts
        filtering(filename2,filename3) # calling the function to apply filters for TD transcripts to create a cleaned file
# This function takes filename for all 10 transcripts of SLI
def SLI():
    for i in range(1,11): # It takes all the filenames from SLI-1 to SLI-10
        filename1 = "SLI-" + str(i) + ".txt"
        filename2 = "SLI_CHI/SLI_CHI-" + str(i) + ".txt"
        filename3 = "SLI_cleaned/SLI_cleaned-" + str(i) + ".txt"
        extract_CHI(filename1, filename2) # calling the function to extract "*CHI:" statements for SLI transcripts
        filtering(filename2, filename3) # calling the function to apply filters for SLI transcripts to create a cleaned file
# This fuction is to show the contents of any file
def read_Cleaned(filename4):
    with open(filename4, "r") as file:
        input = file.read()
        print(input)
    file.close()

if __name__ == '__main__':

    filename4 = "SLI_cleaned/SLI_cleaned-1.txt"

    task1_SLI = SLI() # calling the function to create cleaned for all 10 transcripts of SLI
    task1_TD = TD() # calling the function to create cleaned for all 10 transcripts of TD

    read = read_Cleaned(filename4)
