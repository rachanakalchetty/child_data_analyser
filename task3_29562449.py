# Name: Rachana Kalachetty
# StudentID: 29562449
# Start date: 30th sep 2018
# Last modified date: 12th oct 2018
# This task is used to display 2 graphs and calculate the averages of each of the 6 transcripts for 10 transcripts of SLI and TD
# It is also used to calculate the mean difference
from task2_29562449 import childdataanalyser
import matplotlib.pyplot as plt
import numpy as np
class visualiser:
    def __init__(self,data_SLI,data_TD):
        self.data_SLI = data_SLI
        self.data_TD = data_TD
        self.avg_length_SLI = []
        self.avg_unique_SLI = []
        self.avg_rep_SLI = []
        self.avg_ret_SLI = []
        self.avg_grammer_SLI = []
        self.avg_pause_SLI = []
        self.avg_length_TD = []
        self.avg_unique_TD = []
        self.avg_rep_TD = []
        self.avg_ret_TD = []
        self.avg_grammer_TD = []
        self.avg_pause_TD = []
        self.avg_SLI = []
        self.avg_TD = []
        self.mean =[]

# This function is used to find the average of each statistic of 10 trancripts for SLI and TD
    def compute_averages(self):
        self.avg_length_SLI = (self.data_SLI[0][0]+self.data_SLI[1][0]+self.data_SLI[2][0]+self.data_SLI[3][0]+self.data_SLI[4][0]+self.data_SLI[5][0]+self.data_SLI[6][0]+self.data_SLI[7][0]+self.data_SLI[8][0]+self.data_SLI[9][0])/10
        self.avg_unique_SLI = (self.data_SLI[0][1] + self.data_SLI[1][1] + self.data_SLI[2][1] + self.data_SLI[3][1] +
                              self.data_SLI[4][1] + self.data_SLI[5][1] + self.data_SLI[6][1] + self.data_SLI[7][1] +
                              self.data_SLI[8][1] + self.data_SLI[9][1]) / 10
        self.avg_rep_SLI = (self.data_SLI[0][2] + self.data_SLI[1][2] + self.data_SLI[2][2] + self.data_SLI[3][2] +
                              self.data_SLI[4][2] + self.data_SLI[5][2] + self.data_SLI[6][2] + self.data_SLI[7][2] +
                              self.data_SLI[8][2] + self.data_SLI[9][2]) / 10
        self.avg_ret_SLI = (self.data_SLI[0][3] + self.data_SLI[1][3] + self.data_SLI[2][3] + self.data_SLI[3][3] +
                              self.data_SLI[4][3] + self.data_SLI[5][3] + self.data_SLI[6][3] + self.data_SLI[7][3] +
                              self.data_SLI[8][3] + self.data_SLI[9][3]) / 10
        self.avg_grammer_SLI = (self.data_SLI[0][4] + self.data_SLI[1][4] + self.data_SLI[2][4] + self.data_SLI[3][4] +
                              self.data_SLI[4][4] + self.data_SLI[5][4] + self.data_SLI[6][4] + self.data_SLI[7][4] +
                              self.data_SLI[8][4] + self.data_SLI[9][4]) / 10
        self.avg_pause_SLI = (self.data_SLI[0][5] + self.data_SLI[1][5] + self.data_SLI[2][5] + self.data_SLI[3][5] +
                              self.data_SLI[4][5] + self.data_SLI[5][5] + self.data_SLI[6][5] + self.data_SLI[7][5] +
                              self.data_SLI[8][5] + self.data_SLI[9][5]) / 10
        self.avg_SLI.append(self.avg_length_SLI)
        self.avg_SLI.append(self.avg_unique_SLI)
        self.avg_SLI.append(self.avg_rep_SLI)
        self.avg_SLI.append(self.avg_ret_SLI)
        self.avg_SLI.append(self.avg_grammer_SLI)
        self.avg_SLI.append(self.avg_pause_SLI)
        print("Averages of 6 statistics for all SLI:",self.avg_SLI)
          #TD
        self.avg_length_TD = (self.data_TD[0][0] + self.data_TD[1][0] + self.data_TD[2][0] + self.data_TD[3][0] +
                              self.data_TD[4][0] + self.data_TD[5][0] + self.data_TD[6][0] + self.data_TD[7][0] +
                              self.data_TD[8][0] + self.data_TD[9][0]) / 10
        self.avg_unique_TD = (self.data_TD[0][1] + self.data_TD[1][1] + self.data_TD[2][1] + self.data_TD[3][1] +
                              self.data_TD[4][1] + self.data_TD[5][1] + self.data_TD[6][1] + self.data_TD[7][1] +
                              self.data_TD[8][1] + self.data_TD[9][1]) / 10
        self.avg_rep_TD = (self.data_TD[0][2] + self.data_TD[1][2] + self.data_TD[2][2] + self.data_TD[3][2] +
                           self.data_TD[4][2] + self.data_TD[5][2] + self.data_TD[6][2] + self.data_TD[7][2] +
                           self.data_TD[8][2] + self.data_TD[9][2]) / 10
        self.avg_ret_TD = (self.data_TD[0][3] + self.data_TD[1][3] + self.data_TD[2][3] + self.data_TD[3][3] +
                           self.data_TD[4][3] + self.data_TD[5][3] + self.data_TD[6][3] + self.data_TD[7][3] +
                           self.data_TD[8][3] + self.data_TD[9][3]) / 10
        self.avg_grammer_TD = (self.data_TD[0][4] + self.data_TD[1][4] + self.data_TD[2][4] + self.data_TD[3][4] +
                               self.data_TD[4][4] + self.data_TD[5][4] + self.data_TD[6][4] + self.data_TD[7][4] +
                               self.data_TD[8][4] + self.data_TD[9][4]) / 10
        self.avg_pause_TD = (self.data_TD[0][5] + self.data_TD[1][5] + self.data_TD[2][5] + self.data_TD[3][5] +
                             self.data_TD[4][5] + self.data_TD[5][5] + self.data_TD[6][5] + self.data_TD[7][5] +
                             self.data_TD[8][5] + self.data_TD[9][5]) / 10
        self.avg_TD.append(self.avg_length_TD)
        self.avg_TD.append(self.avg_unique_TD)
        self.avg_TD.append(self.avg_rep_TD)
        self.avg_TD.append(self.avg_ret_TD)
        self.avg_TD.append(self.avg_grammer_TD)
        self.avg_TD.append(self.avg_pause_TD)
        print("Average of 6 statistics for all TD:",self.avg_TD)

        return self.avg_SLI,self.avg_TD
# This function is used to calculate the mean difference for each of 6 statistics of SLI and TD
    def mean_difference(self):
        mean_length =abs(self.avg_TD[0]-self.avg_SLI[0])
        mean_unique = abs(self.avg_TD[1]-self.avg_SLI[1])
        mean_rep = abs(self.avg_TD[2] - self.avg_SLI[2])
        mean_ret = abs(self.avg_TD[3] - self.avg_SLI[3])
        mean_grammer = abs(self.avg_TD[4] - self.avg_SLI[4])
        mean_pause = abs(self.avg_TD[5] - self.avg_SLI[5])
        self.mean.append(mean_length)
        self.mean.append(mean_unique)
        self.mean.append(mean_rep)
        self.mean.append(mean_ret)
        self.mean.append(mean_grammer)
        self.mean.append(mean_pause)
        print("Mean difference:", self.mean)
        return self.mean

# This function is used to display graph for 6 statistics of SLI vs TD and another graph for mean difference
    def visualise_statistics(self):
#graph for 6 statistics average
        n_groups = 6
        means_SLI = (self.avg_SLI)
        means_TD = (self.avg_TD)

        # create plot
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        rects1 = plt.bar(index, means_SLI, bar_width,
                         alpha=opacity,
                         color='b',
                         label='SLI')

        rects2 = plt.bar(index + bar_width, means_TD, bar_width,
                         alpha=opacity,
                         color='g',
                         label='TD')

        plt.xlabel('Statistics')
        plt.ylabel('Average')
        plt.title('SLI vs TD')
        plt.xticks(index + bar_width, ('Length', 'Unique words', 'repetition', 'retracing','grammer_errors','pause'))
        plt.legend()
# graph for mean difference
        plt.tight_layout()
        plt.show()
        objects = ('Length', 'Unique words', 'Repetition', 'Retracing', 'grammer_errors', 'Pause')
        y_pos = np.arange(len(objects))
        performance = self.mean

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Mean difference')
        plt.title('Mean difference between SLI and TD')

        plt.show()



if __name__ == '__main__':
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

    print("SLI child data analysis-\n")
    child_analyser_SLI1 = child_analyser_SLI1.analyse_script("SLI_cleaned/SLI_cleaned-1.txt")
    print(child_analyser_SLI1)
    child_analyser_SLI2 = child_analyser_SLI2.analyse_script("SLI_cleaned/SLI_cleaned-2.txt")
    print(child_analyser_SLI2)
    child_analyser_SLI3 = child_analyser_SLI3.analyse_script("SLI_cleaned/SLI_cleaned-3.txt")
    print(child_analyser_SLI3)
    child_analyser_SLI4 = child_analyser_SLI4.analyse_script("SLI_cleaned/SLI_cleaned-4.txt")
    print(child_analyser_SLI4)
    hild_analyser_SLI5 = child_analyser_SLI5.analyse_script("SLI_cleaned/SLI_cleaned-5.txt")
    print(child_analyser_SLI5)
    child_analyser_SLI6 = child_analyser_SLI6.analyse_script("SLI_cleaned/SLI_cleaned-6.txt")
    print(child_analyser_SLI6)
    child_analyser_SLI7 = child_analyser_SLI7.analyse_script("SLI_cleaned/SLI_cleaned-7.txt")
    print(child_analyser_SLI7)
    child_analyser_SLI8 = child_analyser_SLI8.analyse_script("SLI_cleaned/SLI_cleaned-8.txt")
    print(child_analyser_SLI8)
    child_analyser_SLI9 = child_analyser_SLI9.analyse_script("SLI_cleaned/SLI_cleaned-9.txt")
    print(child_analyser_SLI9)
    child_analyser_SLI10 = child_analyser_SLI10.analyse_script("SLI_cleaned/SLI_cleaned-10.txt")
    print(child_analyser_SLI10)
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
    print("TD child data analysis-\n")
    child_analyser_TD1 = child_analyser_TD1.analyse_script("TD_cleaned/TD_cleaned-1.txt")
    print(child_analyser_TD1)
    child_analyser_TD2 = child_analyser_TD2.analyse_script("TD_cleaned/TD_cleaned-2.txt")
    print(child_analyser_TD2)
    child_analyser_TD3 = child_analyser_TD3.analyse_script("TD_cleaned/TD_cleaned-3.txt")
    print(child_analyser_TD3)
    child_analyser_TD4 = child_analyser_TD4.analyse_script("TD_cleaned/TD_cleaned-4.txt")
    print(child_analyser_TD4)
    child_analyser_TD5 = child_analyser_TD5.analyse_script("TD_cleaned/TD_cleaned-5.txt")
    print(child_analyser_TD5)
    child_analyser_TD6 = child_analyser_TD6.analyse_script("TD_cleaned/TD_cleaned-6.txt")
    print(child_analyser_TD6)
    child_analyser_TD7 = child_analyser_TD7.analyse_script("TD_cleaned/TD_cleaned-7.txt")
    print(child_analyser_TD7)
    child_analyser_TD8 = child_analyser_TD8.analyse_script("TD_cleaned/TD_cleaned-8.txt")
    print(child_analyser_TD8)
    child_analyser_TD9 = child_analyser_TD9.analyse_script("TD_cleaned/TD_cleaned-9.txt")
    print(child_analyser_TD9)
    child_analyser_TD10 = child_analyser_TD10.analyse_script("TD_cleaned/TD_cleaned-10.txt")
    print(child_analyser_TD10)
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

    testing1 = visualiser(list_SLI,list_TD)
    test = testing1.compute_averages()
    means = testing1.mean_difference()
    graph1 = testing1.visualise_statistics()





