# CSV-and-txt-dataset-processing

Assignment description:

Problem 1: Pokemon Box Dataset 

Given a CSV data file as represented by the sample file pokemonTrain.csv, perform the following operations on it.

Find out what percentage of "fire" type pokemons are at or above the "level" 40.

Percentage of fire type Pokemons at or above level 40 = ...

Percentage of fire type Pokemons at or above level 40 = 13

Print the value to a file named "pokemon1.txt"

Fill in the missing "type" column values (given by NaN) by mapping them from the corresponding "weakness" values. You will see that typically a given pokemon weakness has a fixed "type", but there are some exceptions. So, fill in the "type" column with the most common "type" corresponding to the pokemon’s "weakness" value.

Fill in the missing (NaN) values in the Attack ("atk"), Defense ("def") and Hit Points ("hp") columns as follows:
Set the pokemon level threshold to 40.

After performing #2 and #3, write the modified data to another csv file named "pokemonResult.csv".
This result file should have all of the rows from the input file - rows that were modified as well as rows that were not modified.

The following tasks (#4 and #5) should be performed on the pokemonResult.csv file that resulted above.

Create a dictionary that maps pokemon types to their personalities. This dictionary would map a string to a list of strings. For example:
     {"fire": ["docile", "modest", ...], "normal": ["mild", "relaxed", ...],  ...}
Your dictionary should have the keys ordered alphabetically, and also items ordered alphabetically in the values list, as shown in the example above.

Find out the average Hit Points ("hp") for pokemons of stage 3.0.


Problem 2: Covid-19 Dataset 

Given a Covid-19 data CSV file with 12 feature columns, perform the tasks given below. Use the sample file covidTrain.csv to test your code.

In the age column, wherever there is a range of values, replace it by the rounded off average value. E.g., for 10-14 substitute 12. (Rounding should be done like in 1.1). You might want to use regular expressions here, but it is not required.

Change the date format for the date columns - date_onset_symptoms, date_admission_hospital and date_confirmation from dd.mm.yyyy to mm.dd.yyyy. Again, you can use regexps here, but it is not required.

Fill in the missing (NaN) "latitude" and "longitude" values by the average of the latitude and longitude values for the province where the case was recorded. Round the average to 2 decimal places.

Fill in the missing “city” values by the most occurring city value in that province. In case of a tie, use the city that appears first in alphabetical order.

Fill in the missing "symptom" values by the single most frequent symptom in the province where the case was recorded. In case of a tie, use the symptom that appears first in alphabetical order.


Problem 3: Text Processing

For this problem, you are given a set of documents (text files) on which you will perform some preprocessing tasks, and then compute what is called the TF-IDF score for each word. The TF-IDF score for a word is measure of its importance within the entire set of documents: the higher the score, the more important is the word.

The input set of documents must be read from a file named "tfidf_docs.txt". This file will list all the documents (one per line) you will need to work with. For instance, if you need to work with the set "doc1.txt", "doc2.txt", and "doc2.txt", the input file "tfidf_docs.txt" contents will look like this:

     doc1.txt
     doc2.txt
     doc2.txt
     
Part 1: Preprocessing 
For each document in the input set, clean and preprocess it as follows:

Clean.
Remove all characters that are not words or whitespaces. Words are sequences of letters (upper and lower case), digits, and underscores.
Remove extra whitespaces between words. e.g., “Hello World! Let’s   learn    Python!”, so that there is exactly one whitespace between any pair of words.
Remove all website links. A website link is a sequence of non-whitespace characters that starts with either "http://" or "https://".
Convert all the words to lowercase.
The resulting document should only contain lowercase words separated by a single whitespace.

Remove stopwords.
From the document that results after #1 above, remove "stopwords". These are the non-essential (or "noise") words listed in the file stopwords.txt

Stemming and Lemmatization.
This is a process of reducing words to their root forms. For example, look at the following reductions: run, running, runs → run. All three words capture the same idea ‘run’ and hence their suffixes are not as important.

Use the following rules to reduce the words to their root form:

Words ending with "ing": "flying" becomes "fly"
Words ending with "ly": "successfully" becomes "successful"
Words ending with "ment": "punishment" becomes "punish"
These rules are not expected to capture all the edge cases of Stemming in the English language but are intended to give you a general idea of the preprocessing steps in NLP (Natural Language Processing) tasks.

After performing #1, #2, and #3 above for each input document, write the modified data to another text file with the prefix "preproc_". For instance, if the input document is "doc1.txt", the output should be "preproc_doc1.txt".

Part 2: Computing TF-IDF Scores
Once preprocessing is performed on all the documents, you need to compute the Term Frequency(TF) — Inverse Document Frequency(IDF) score for each word.

Steps:

For each preprocessed document that results from the preprocessing in Part 1, compute frequencies of all the distinct words in that document only. So if you had 3 documents in the input set, you will compute 3 sets of word frequencies, one per document.
Compute the Term Frequency (TF) of each distinct word (also called term) for each of the preprocessed documents:
    TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)
Note: The denominator, total number of terms, is the sum total of all the words, not just unique instances. So if a word occurs 5 times, and the total number of words in a document is 100, then TF for that word is 5/100.

Compute the Inverse Document Frequency (IDF) of each distinct word for each of the preprocessed documents.
IDF is a measure of how common or rare a word is in a document set (a set of preprocessd text files in this case). It is calculated by taking the logarithm of the following term:

   IDF(t) = log((Total number of documents) / (Number of documents the word is found in)) + 1
Note: The log here uses base e. And 1 is added after the log is taken, so that the IDF score is guaranteed to be non-zero.
Calculate TF-IDF score: TF * IDF for each distinct word in each preprocessed document. Round the score to 2 decimal places.
Print the top 5 most important words in each preprocessed document according to their TF-IDF scores. The higher the TF-IDF score, the more important the word. In case of ties in score, pick words in alphabetical order. You should print the result as a list of (word,TF-IDF score) tuples sorted in descending TF-IDF scores. See the Testing section below, in files tfidf_test1.txt and tfidf_test2.txt, for the exact output format.
