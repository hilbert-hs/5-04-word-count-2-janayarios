###########################################################
###   Copy and paste your word frequency code here      ###
###   into two new functions:                           ###
###      text_to_word_list()                            ###
###      count_frequencies()                            ###
###   OR add your word frequency code to thie repo as   ###
###   a separate file and import it                     ###
###########################################################

import frequency

wordList = frequency.text_to_wordlist('sample.txt')
wordFreqDCT = frequency.count_frequencies(wordList)

###########################################################
###   Write your new functions here:                    ###
###      find_max_valued_key()                          ###
###########################################################

def find_max_valued_key(_wordDCT):
  max = 0
  frequentWord = ''
  for key in _wordDCT:
    if _wordDCT[key] > max:
      max = _wordDCT[key]
      frequentWord = key
  return [frequentWord, max]





###########################################################
###   Write your loop to find the top                   ###
###   five most frequent words                          ###
###########################################################

for i in range(5):
  wordResult = find_max_valued_key(wordFreqDCT)
  print(f"'{wordResult[0]}' appears {wordResult[1]} times")
  del wordFreqDCT[(find_max_valued_key(wordFreqDCT)[0])]

