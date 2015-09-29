from collections import Counter
import glob
import re
import math
class Review:
    words = ""
    def __init__(self, filepath):
        self.words = set((re.findall(r"[\w][\w]*'?\w?", open(filepath).read().lower())))


    def generate2Grams(self):
        for i in range(len(self.words)-1):
            self.words[i] = self.words[i]+"_"+self.words[i+1]
        self.words = set(self.words)
        return self.words






class Reviewer:
    negwords = {}
    poswords = {}
    stopwords = []
    pos_occurence = {}
    neg_occurence = {}
    def __init__(self):
        pass

    def train(self, files):

        posfiles = glob.glob("./alle/train/pos/*.txt")
        negfiles = glob.glob("./alle/train/neg/*.txt")
        self.stopwords = re.findall(r"[\w][\w]*'?\w?", open("stop_words.txt").read().lower())


        for index, file in enumerate(posfiles):
            rev = Review(file)
            self.poswords[index] = rev.words
        for index, file in enumerate(negfiles):
            rev = Review(file)
            self.negwords[index] = rev.words
        self.checkMostUsed()
        self.pruning()


    def checkMostUsed(self):
        reviews = len(self.poswords.keys()) + len(self.negwords.keys())
        positive_words = []
        negative_words = []
        for list in self.poswords.values():
            for word in list:
                positive_words.append(word)
        for list in self.negwords.values():
            for word in list:
                negative_words.append(word)
        positive_words = [word for word in positive_words if word not in self.stopwords]
        negative_words = [word for word in negative_words if word not in self.stopwords]
        common_neg = Counter(negative_words)
        common_pos = Counter(positive_words)
        for word, occ in common_pos.items():

            self.pos_occurence[word] = float(occ)/float(reviews)
        for word, occ in common_neg.items():
            self.neg_occurence[word] = float(occ)/float(reviews)


    def pruning(self):

        for word, occ in self.pos_occurence.items():
            if occ < 0.02:
                del self.pos_occurence[word]


        for word, occ in self.neg_occurence.items():
            if occ < 0.02:
                del self.neg_occurence[word]



    def goTroughFiles(self):
        posreviews = glob.glob("./alle/test/pos/*.txt")
        negreviews = glob.glob("./alle/test/neg/*.txt")
        correct = 0
        correctNeg = 0
        for i in range(len(posreviews)):
            if self.isPositive(Review(posreviews[i]).words):
                correct += 1

        for i in range(len(negreviews)):
             if not self.isPositive(Review(negreviews[i]).words):
                correctNeg += 1

        print("Found on positive reviews correct % amount of " + str(float(correct)/float(len(posreviews))*100)+"%")
        print("Found on negative reviews correct % amount of " + str(float(correctNeg)/float(len(negreviews))*100)+"%")


    def isPositive(self, review):
        posScore = 0
        negScore = 0
        for word in review:

            try:
                posScore += math.log(self.pos_occurence[word])
            except KeyError:
               pass
            try:
                negScore += math.log(self.neg_occurence[word])
            except KeyError:
                pass
        return posScore < negScore


ai = Reviewer()
ai.train("")
ai.goTroughFiles()




