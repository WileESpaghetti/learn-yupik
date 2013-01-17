#!python
#encoding: utf-8
#columns
labials = ['p', 'v', 'vv', 'n', 'ń']
apicals = ['t', 'l', 'll', 'n', 'ń', 'c', 's', 'y', 'ss']
frontVelars = ['k', 'g', 'gg', 'ng', 'ńg', 'q', 'r', 'rr']
labializedFrontVelars = ['ug', 'w']
labializedbackVelars = ['ur', 'urr']

# rows
stops = ['p', 't', 'c', 'k', 'q']
voicedFricatives = ['v', 'l', 's', 'y', 'g', 'r']#, 'ug', 'ur']
voicelessFricatives = ['vv', 'll', 'ss', 'gg', 'rr']
fricatives = voicedFricatives + voicelessFricatives
voicedNasals = ['n', 'ng']
voicelessNasals = ['ń']#,'ńg']
nasals = voicedNasals + voicelessNasals

consonants = list(set(stops + fricatives +  nasals))

#vowel columns
frontVowels = ['i']
midVowels = ['e', 'a']
backVowels = ['u']

#rows
highVowels = ['i', 'e', 'u']
lowVowels = ['a']

primeVowels = ['a', 'i', 'u']

vowels = highVowels + lowVowels


# acegiklmnpqrstuvwy

vowels = ['a', 'e', 'i', 'u']
consonants = ['p', 't', 'c',]







