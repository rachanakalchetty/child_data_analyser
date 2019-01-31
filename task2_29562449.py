# Name: Rachana Kalachetty
# StudentID: 29562449
# Start date: 30th sep 2018
# Last modified date: 12th oct 2018
import re
from tabulate import tabulate
# In this task, we need to find the 6 statistics by getting a count of all 6 statistics for each transcript
class childdataanalyser:
    #  In this function, all the 6 statistics count is initialized to zero and the list suppose to store them is initialised
    def __init__(self):
        self.length_count = 0
        self.unique_words_count = 0
        self.repetition_count = 0
        self.retracing_count = 0
        self.grammer_errors_count = 0
        self.pause_count = 0
        self.statistics = []

    def get_length_of_transcripts(self): # returns length of trancript
        return self.length_count

    def get_size_of_vocabulary(self): # returns number of unique words in the transcript
        return self.unique_words_count

    def get_num_of_repetition(self): # returns number of "[/]" in the transcript
        return self.repetition_count

    def get_num_of_retracing(self): # returns the number of "[//]" in the transcript
        return self.retracing_count

    def get_num_of_grammatical_errors(self): # returns the number of "[* m:+ed]" in the transcript
        return self.grammer_errors_count

    def get_num_of_pauses(self): # returns the number of "(.)" in the transcript
        return self.pause_count

    def get_statistics(self): # returns the list of 6 statistics for each transcript
        return self.statistics


    def __str__(self): # displays the 6 statistics for each transcript in the required format
        return "Length of Transcript:\t" + str(self.length_count) + '\n' + "Size of Vocabulary:\t" + str(
            self.unique_words_count) + '\n' + "Number of repetition for certain words or phrases or [/]:\t" + str(
            self.repetition_count) + '\n' + "Number of retracing for certain words or phrases or [//]:\t" + str(
            self.retracing_count) + '\n' + "Number of grammatical errors detected or [* m:+ed]:\t" + str(
            self.grammer_errors_count) + '\n' + "Number of pauses made or (.):\t" + str(self.pause_count) + '\n'

    # This function is used to get the count of each statistics for each transcript
    def analyse_script(self, cleaned_file):
        with open(cleaned_file) as f: # the cleaned file is opened
            inp = f.read()
            count_length = re.findall('[.?!][^(.)]', inp)  # This regex finds all occurences of ".", "?" and "!" in the cleaned transcript
            self.length_count = len(count_length) # this returns the count of all the occurences found in the above cleaned transcript
            words = re.findall('\w+', inp.lower())  # The regex finds all the words in the cleaned transcript
            unique_words = set(words) # The words are stored in the list when re.findall() is ran , by converting the list of those words into a set
            #All the duplicate words are removed in the set, hence it contains only set of unique words
            self.unique_words_count = len(unique_words) # this returns the count of unique words in the set
            self.repetition_count = inp.count("[/]")  # The count() function finds the occurence of the pattern "[/]" in the cleaned transcript
            # and returns the count of it
            self.retracing_count = inp.count("[//]")  # The count() function finds the occurence of the pattern "[//]" in the cleaned transcript
            # and returns the count of it
            self.grammer_errors_count = inp.count("[* m:+ed]")  # The count() function finds the occurence of the pattern "[* m:+ed]" in the cleaned transcript
            # and returns the count of it
            self.pause_count = inp.count("(.)")  # The count() function finds the occurence of the pattern "(.)" in the cleaned transcript
            # and returns the count of it
            self.statistics.append(self.length_count) # appends the 6 statistics to the list
            self.statistics.append(self.unique_words_count)
            self.statistics.append(self.repetition_count)
            self.statistics.append(self.retracing_count)
            self.statistics.append(self.grammer_errors_count)
            self.statistics.append(self.pause_count)
            #self.statistics_array = array(statistics)
            #print(statistics_array)
        f.close()
        return self
if __name__ == '__main__':
    # creating object for each transcript of SLI
    child_analyser_SLI1 = childdataanalyser()
    child_analyser_SLI2 = childdataanalyser()
    child_analyser_SLI3 = childdataanalyser()
    child_analyser_SLI4 = childdataanalyser()
    child_analyser_SLI5 = childdataanalyser()
    child_analyser_SLI6 = childdataanalyser()
    child_analyser_SLI7 = childdataanalyser()
    child_analyser_SLI8 = childdataanalyser()
    child_analyser_SLI9 = childdataanalyser()
    child_analyser_SLI10 = childdataanalyser()
    child_analyser_TD1 = childdataanalyser()
    child_analyser_TD2 = childdataanalyser()
    child_analyser_TD3 = childdataanalyser()
    child_analyser_TD4 = childdataanalyser()
    child_analyser_TD5 = childdataanalyser()
    child_analyser_TD6 = childdataanalyser()
    child_analyser_TD7 = childdataanalyser()
    child_analyser_TD8 = childdataanalyser()
    child_analyser_TD9 = childdataanalyser()
    child_analyser_TD10 = childdataanalyser()

    # change file names n folders
    # calls analyse_script() for each SLI transcript
    print("SLI child data analysis-\n")
    print("SLI-1 data analysis")
    child_analyser_SLI1 = child_analyser_SLI1.analyse_script("SLI_cleaned/SLI_cleaned-1.txt")
    print(child_analyser_SLI1)
    print("SLI-2 data analysis")
    child_analyser_SLI2 = child_analyser_SLI2.analyse_script("SLI_cleaned/SLI_cleaned-2.txt")
    print(child_analyser_SLI2)
    print("SLI-3 data analysis")
    child_analyser_SLI3 = child_analyser_SLI3.analyse_script("SLI_cleaned/SLI_cleaned-3.txt")
    print(child_analyser_SLI3)
    print("SLI-4 data analysis")
    child_analyser_SLI4 = child_analyser_SLI4.analyse_script("SLI_cleaned/SLI_cleaned-4.txt")
    print(child_analyser_SLI4)
    print("SLI-5 data analysis")
    child_analyser_SLI5 = child_analyser_SLI5.analyse_script("SLI_cleaned/SLI_cleaned-5.txt")
    print(child_analyser_SLI5)
    print("SLI-6 data analysis")
    child_analyser_SLI6 = child_analyser_SLI6.analyse_script("SLI_cleaned/SLI_cleaned-6.txt")
    print(child_analyser_SLI6)
    print("SLI-7 data analysis")
    child_analyser_SLI7 = child_analyser_SLI7.analyse_script("SLI_cleaned/SLI_cleaned-7.txt")
    print(child_analyser_SLI7)
    print("SLI-8 data analysis")
    child_analyser_SLI8 = child_analyser_SLI8.analyse_script("SLI_cleaned/SLI_cleaned-8.txt")
    print(child_analyser_SLI8)
    print("SLI-9 data analysis")
    child_analyser_SLI9 = child_analyser_SLI9.analyse_script("SLI_cleaned/SLI_cleaned-9.txt")
    print(child_analyser_SLI9)
    print("SLI-10 data analysis")
    child_analyser_SLI10 = child_analyser_SLI10.analyse_script("SLI_cleaned/SLI_cleaned-10.txt")
    print(child_analyser_SLI10)
    # This calls the get_statistics function to get 6 statistics of each SLI transcript
    stats_SLI1 = child_analyser_SLI1.get_statistics()
    #print(stats_SLI1)
    stats_SLI2 = child_analyser_SLI2.get_statistics()
    #print(stats_SLI2)
    stats_SLI3 = child_analyser_SLI3.get_statistics()
    #print(stats_SLI3)
    stats_SLI4 = child_analyser_SLI4.get_statistics()
    #print(stats_SLI4)
    stats_SLI5 = child_analyser_SLI5.get_statistics()
    #print(stats_SLI5)
    stats_SLI6 = child_analyser_SLI6.get_statistics()
    #print(stats_SLI6)
    stats_SLI7 = child_analyser_SLI7.get_statistics()
    #print(stats_SLI7)
    stats_SLI8 = child_analyser_SLI8.get_statistics()
    #print(stats_SLI8)
    stats_SLI9 = child_analyser_SLI9.get_statistics()
    #print(stats_SLI9)
    stats_SLI10 = child_analyser_SLI10.get_statistics()
    #print(stats_SLI10)
    #change filenames and folder
    print("TD child data analysis-\n")
    print("TD-1 data analysis")
    child_analyser_TD1 = child_analyser_TD1.analyse_script("TD_cleaned/TD_cleaned-1.txt")
    print(child_analyser_TD1)
    print("TD-2 data analysis")
    child_analyser_TD2 = child_analyser_TD2.analyse_script("TD_cleaned/TD_cleaned-2.txt")
    print(child_analyser_TD2)
    print("TD-3 data analysis")
    child_analyser_TD3 = child_analyser_TD3.analyse_script("TD_cleaned/TD_cleaned-3.txt")
    print(child_analyser_TD3)
    print("TD-4 data analysis")
    child_analyser_TD4 = child_analyser_TD4.analyse_script("TD_cleaned/TD_cleaned-4.txt")
    print(child_analyser_TD4)
    print("TD-5 data analysis")
    child_analyser_TD5 = child_analyser_TD5.analyse_script("TD_cleaned/TD_cleaned-5.txt")
    print(child_analyser_TD5)
    print("TD-6 data analysis")
    child_analyser_TD6 = child_analyser_TD6.analyse_script("TD_cleaned/TD_cleaned-6.txt")
    print(child_analyser_TD6)
    print("TD-7 data analysis")
    child_analyser_TD7 = child_analyser_TD7.analyse_script("TD_cleaned/TD_cleaned-7.txt")
    print(child_analyser_TD7)
    print("TD-8 data analysis")
    child_analyser_TD8 = child_analyser_TD8.analyse_script("TD_cleaned/TD_cleaned-8.txt")
    print(child_analyser_TD8)
    print("TD-9 data analysis")
    child_analyser_TD9 = child_analyser_TD9.analyse_script("/Users/rachnak/ENNI Dataset/TD_cleaned/TD_cleaned-9.txt")
    print(child_analyser_TD9)
    print("TD-10 data analysis")
    child_analyser_TD10 = child_analyser_TD10.analyse_script("/Users/rachnak/ENNI Dataset/TD_cleaned/TD_cleaned-10.txt")
    print(child_analyser_TD10)
    # stats
    stats_TD1 = child_analyser_TD1.get_statistics()
    #print(stats_TD1)
    stats_TD2 = child_analyser_TD2.get_statistics()
    #print(stats_TD2)
    stats_TD3 = child_analyser_TD3.get_statistics()
    #print(stats_TD3)
    stats_TD4 = child_analyser_TD4.get_statistics()
    #print(stats_TD4)
    stats_TD5 = child_analyser_TD5.get_statistics()
    #print(stats_TD5)
    stats_TD6 = child_analyser_TD6.get_statistics()
    #print(stats_TD6)
    stats_TD7 = child_analyser_TD7.get_statistics()
    #print(stats_TD7)
    stats_TD8 = child_analyser_TD8.get_statistics()
    #print(stats_TD8)
    stats_TD9 = child_analyser_TD9.get_statistics()
    #print(stats_TD9)
    stats_TD10 = child_analyser_TD10.get_statistics()
    #print(stats_TD10)

    # stored
    list_SLI = []
    list_SLI.append(stats_SLI1)
    list_SLI.append(stats_SLI2)
    list_SLI.append(stats_SLI3)
    list_SLI.append(stats_SLI4)
    list_SLI.append(stats_SLI5)
    list_SLI.append(stats_SLI6)
    list_SLI.append(stats_SLI7)
    list_SLI.append(stats_SLI8)
    list_SLI.append(stats_SLI9)
    list_SLI.append(stats_SLI10)
    list_TD = []
    list_TD.append(stats_TD1)
    list_TD.append(stats_TD2)
    list_TD.append(stats_TD3)
    list_TD.append(stats_TD4)
    list_TD.append(stats_TD5)
    list_TD.append(stats_TD6)
    list_TD.append(stats_TD7)
    list_TD.append(stats_TD8)
    list_TD.append(stats_TD9)
    list_TD.append(stats_TD10)

    print("SLI average data:")
    print(tabulate(list_SLI, headers=['Length', 'Unique words','Repetition','Retracing','Grammer','Pauses']))
    print("TD average data:")
    print(tabulate(list_TD, headers=['Length', 'Unique words','Repetition','Retracing','Grammer','Pauses']))