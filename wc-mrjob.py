from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.compat import jobconf_from_env
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
                filename = jobconf_from_env('mapreduce.map.input.file')
                w = limpiar(w)
                if w!=',' and w:
	           yield (w,filename),1

  def reducer(self, key, values):
      l = list(key)
      yield l[0],(sum(values),l[1])

  def reducer2(self, key, pairs):
        l = list(pairs)
        l.sort(reverse=True)
        l = l[:10]
        l2 = list()
        for i in l:
           l2.append(i[1])
        yield key,l2


  def steps(self):
    		return [
    			MRStep(mapper = self.mapper, reducer = self.reducer),
    			MRStep(reducer = self.reducer2)
    		]

if __name__ == '__main__':
    MRWordFrequencyCount.run()
