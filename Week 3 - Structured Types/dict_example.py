def most_common_words(freqs):
	values = freqs.values()
	best = max(values)
	words = []
	for k in freqs:
		if freqs[k] == best:
			words.append(k)
	return (words, best)


def words_often(freqs, minTimes):
	result = []
	done = Falase
	while not done:
		temp = most_common_words(freqs)
		if temp[1] >= minTimes:
			result.append(temp)
			for w in temp[0]:
				del freqs[w] # remove word from dict
		else:
			done = True
	return result

print(words_often(list_of_words, 5))