from mrjob.job import MRJob
import re, string
import unicodedata

def tildes(word):
   return ''.join((c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn'))

def signos (word):
    return re.sub('[%s]' % re.escape(string.punctuation), '', word)

def numeros (word):
   return ''.join([i for i in word if not i.isdigit()])
 
def limpiar (word):
   word = signos(word)
   word = tildes(word)
   word = numeros(word)
   word = word.lower()
   word = word+',';
   return word
 
class MRWordFrequencyCount(MRJob):
  def mapper(self, _, line):

       for w in line.decode('utf-8','ignore').split():
                w = limpiar(w)
                if w!=',':
	           yield w,1

  def reducer(self, key, values):
      yield key, sum(values)

if __name__ == '__main__':
    MRWordFrequencyCount.run()
