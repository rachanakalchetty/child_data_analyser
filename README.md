# child_data_analyser
It can be used to investigate the linguistic characteristics of children with some form of language disorders. The analyzer is able to perform basic statistical analysis on a number of linguistic features and also to present the analysis results using visualization. 

Introduction
The assignment is to build a basic language analyzer to examine the linguistic characteristics of children with language disorders. The analyzer should be able to perform the basic statistical analysis on a number of linguistic features and to present the analysis results using some form of visualization.
The dataset used for this assignment is ENNI. This dataset contains two types of language disorder transcripts. There are totally 10 transcripts for each type. The two types of language disorders are Specific Language Impairment (SLI) and typical development (TD).
These transcripts contain the record of story telling task performed by a child from each of the two groups under supervision of an investigator. The stories were evoked by presenting pictures of different animal characters to the children.
Since we have to do analysis on child language disorders only “*CHI:” statements in the transcript are extracted as these are the words spoken by the child.
Task 1: Handling with File Contents and Preprocessing
In this task, the contents from both group’s transcripts are read and preprocessing task is performed. The first step is to extract all “*CHI:” statements from 20 transcripts and apply filters to get only necessary statements for analysis in task 2 and task 3. Before applying the filtering process split each statement into a list of words or tokens.
The filtering tasks are:
1. Remove “*CHI:” from the transcript.
2. Remove those words that have either ‘[’ as prefix or ‘]’ as suffix but retain these three
symbols: [//], [/], and [*] including “[ “or “]” symbols.
3. Retain those words that have either ‘<’ as prefix or ‘>’ as suffix but these two symbols
should be removed.
4. Remove those words that have prefixes of ‘&’ and ‘+’
5. Retain those words that have either ‘(’ as prefix or ‘)’ as suffix but these two symbols
should be removed. But we should not remove the symbol of ‘(.)’ as this should be retained for data analysis.
The cleaned SLI transcripts are stored under a folder named “SLI_cleaned”, and the cleaned TD transcripts under another new folder named “TD_cleaned”.

Task 2: Building a Class for Data Analysis

In this task, a number of statistics for the two groups of children transcripts are produced. These statistics serve as features for differentiating between the children with SLI and the typically developed (TD) children.
The statistics for each of child transcript required are:
• Length of the transcript — indicated by the number of statements (? Or ! or .)
• Size of the vocabulary — indicated by the number of unique words
• Number of repetition for certain words or phrases — indicated by the CHAT symbol [/] •Number of retracing for certain words or phrases — indicated by the CHAT symbol [//] •Number of grammatical errors detected — indicated by the CHAT symbol [* m:+ed]
• Number of pauses made — indicated by the CHAT symbol (.)

Task 3: Building a Class for Data Visualization
 
