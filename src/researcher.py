from itertools import count
import pandas as pd
import json

class Researcher:
    def __init__(self, df):
        self.df = df
        self.df["Words_num"] = self.df["Text"].apply(lambda n: len(n.split()))
        self.df["Letters_num"] = self.df["Text"].str.len()

        self.antisemitic_df = self.df[self.df['Biased'] == 1].copy()
        self.non_antisemitic_df = self.df[self.df['Biased'] == 0].copy()
        self.total_tweets = self.tweets_count()


    def tweets_count(self):
        tweets_counts = self.df['Biased'].value_counts().to_dict()
        total = self.df['Biased'].count()
        total_tweets = {'antisemitic': tweets_counts[1],
                        'non_antisemitic': tweets_counts[0],
                        'total': int(total)}
        return total_tweets

    def average_words_calculation(self):
        antisemitic = sum(self.antisemitic_df["Words_num"]) / self.total_tweets['antisemitic']
        non_antisemitic = sum(self.non_antisemitic_df["Words_num"]) / self.total_tweets['non_antisemitic']
        total = sum(self.df["Words_num"]) / self.total_tweets['total']
        average_length = {'antisemitic': antisemitic,
                        'non_antisemitic': non_antisemitic,
                        'total': total}
        return average_length

    def longest_tweets_calculation(self):
        total = self.df.nlargest(3, "Letters_num")['Text'].to_list()
        antisemitic = self.antisemitic_df.nlargest(3, "Letters_num")['Text'].to_list()
        non_antisemitic = self.non_antisemitic_df.nlargest(3, "Letters_num")['Text'].to_list()
        longest_3_tweets = {'antisemitic': antisemitic,
                        'non_antisemitic': non_antisemitic,
                        'total': total}
        return longest_3_tweets

    def common_words_count(self):
        all_words = ' '.join(self.df['Text']).lower().split()
        common_words_dict = pd.Series(all_words).value_counts().to_dict()
        common_words_list = [word for word in common_words_dict.keys()]
        common_words = {'total':  common_words_list[:10]}
        return common_words

    def upper_count(self):
        all_words = ''.join(self.df['Text']).split()
        total = len([word for word in all_words if word.isupper() and word.isalpha()])
        antisemitic_all_words = ''.join(self.antisemitic_df['Text']).split()
        antisemitic = len([word for word in antisemitic_all_words if word.isupper() and word.isalpha()])
        non_antisemitic_all_words = ''.join(self.non_antisemitic_df['Text']).split()
        non_antisemitic = len([word for word in non_antisemitic_all_words if word.isupper() and word.isalpha()])
        uppercase_words = {'antisemitic': antisemitic,
                        'non_antisemitic': non_antisemitic,
                        'total': total}
        return uppercase_words

    def write_results_to_json(self):
        average_length = self.average_words_calculation()
        longest_3_tweets = self.longest_tweets_calculation()
        common_words = self.common_words_count()
        uppercase_words = self.upper_count()
        result = {'total_tweets': self.total_tweets,
                  'average_length': average_length,
                  'longest_3_tweets': longest_3_tweets,
                  'common_words': common_words,
                  'uppercase_words': uppercase_words
        }
        with open("C:/Users/israel/Desktop/data/antisemitism/results/results.json", "w") as j:
            json.dump(result, indent=4)






