# maltese-word-lists
A collection of word lists in the Maltese language.

Word lists are constructed by automatically extracting a word list from some corpus and then manually removing undesirable words from it.
Each automatically extracted list is put into a different folder and the manually curated lists are given version numbers (each version is an improvement of some kind).

## [dash_apostrophe-lowercase-km4.2](dash_apostrophe-lowercase-km4.2)

A lowercased word list consisting of (case-insensitive) frequent words extracted from the Korpus Malti (KM) v4.2 corpus.
The words are actually strings consisting of alphabetical letters, dashes (-), and apostrophes (').
This makes the list consist of stand alone tokens such as 'kelb' and 'ħdax' but also tokens together with their 'dashed' articles and prepositions such as 'il-kelb', 'tal-kelb', 'ħdax-il' and 'b'ħdax'.
This can be basicly thought of as a space separated list of tokens without punctuation marks, similar to what an English tokeniser would extract from Maltese text.

It is useful for systems designed for English that treat dashes and apostrophes as parts of tokens.
By including dashes and apostrophes in the 'words', such systems will avoid putting spaces around these symbols.
Example applications for this are making synthetic data for pretraining optical character recognition models as well as text prediction models that predict the word being typed.
