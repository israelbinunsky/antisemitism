import pandas as pd
class Researcher:
    def __init__(self, df):
        self.df = df
        self.df["Words_num"] = self.df["Text"].apply(lambda n: len(n.split()))
        self.df["Letters_num"] = self.df["Text"].str.len()
        self.antisemitic_df = self.df[self.df['Biased'] == 1].copy()
        self.non_antisemitic_df = self.df[self.df['Biased'] == 0].copy()
        self.total_tweets = self.tweets_counts()

    def tweets_counts(self):
        tweets_counts = self.df['Biased'].value_counts().to_dict()
        total = self.df['Biased'].count()
        total_tweets = {'antisemitic': tweets_counts[1],
                        'non_antisemitic': tweets_counts[0],
                        'total': int(total)}
        return total_tweets

    def average_calculation(self):
        antisemitic = sum(self.antisemitic_df["Words_num"]) / self.total_tweets['antisemitic']
        non_antisemitic = sum(self.non_antisemitic_df["Words_num"]) / self.total_tweets['non_antisemitic']
        total = sum(self.df["Words_num"]) / self.total_tweets['total']
        average_length = {'antisemitic': antisemitic,
                        'non_antisemitic': non_antisemitic,
                        'total': total}
        return average_length



