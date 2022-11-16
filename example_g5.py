from representations.sequentialembedding import SequentialEmbedding
#from __future__ import print_function

"""
Example showing how to load a series of historical embeddings and compute similarities over time.
Warning that loading all the embeddings into main memory can take a lot of RAM
"""

class SimCalc():
    def __init__(self, embeddings_path="embeddings/eng-fiction-all_sgns"):
        self.embeddings = SequentialEmbedding.load(embeddings_path, range(1950, 2000, 10))

    def calc_similarity(self, word1, word2):
        fiction_embeddings = self.embeddings
        time_sims = fiction_embeddings.get_time_sims(word1, word2)
        print("\nSimilarity between: {} & {}".format(word1, word2))
        for year, sim in time_sims.iteritems():
            print "{year:d}, cosine similarity={sim:0.2f}".format(year=year,sim=sim)


if __name__ == "__main__":
    calc = SimCalc()

    word1, word2 = "gay", "homosexual"
    calc.calc_similarity(word1, word2)

    word1, word2 = "gay", "cheerful"
    calc.calc_similarity(word1, word2)
