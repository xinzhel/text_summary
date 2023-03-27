
import matplotlib.pyplot as plt
from transformers import PreTrainedTokenizerFast, AutoTokenizer
from itertools import islice
import torch
import json
import pandas as pd



def read_json_into_list(file_path):
    lst_dict = []
    with open(file_path, "r") as f:
        lines = f.readlines()
    for line in lines:
        lst_dict.append(json.loads(line))
    return lst_dict

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-base")

def print_statitiscs(articles, summaries=None, target='word_lengths'):

    if target == 'word_lengths':
        # article and summary word lengths 
        article_lengths = [len(article.split()) for article in articles]
        if summaries is not None:
            summary_lengths = [len(summary.split()) for summary in summaries]
    elif target == 'token_lengths':
        # article and summary subword lengths
        
        article_lengths = []
        summary_lengths = []
        
        for batch_articles, batch_summaries in generate_batch(articles, summaries, bsz=32):
            indexed_articles = tokenizer(batch_articles, return_tensors="pt", padding="longest" )['input_ids']
            lengths = torch.sum(indexed_articles!=1, dim=-1) -2
            article_lengths.extend(lengths.tolist())

            if summaries is not None:
                indexed_summaries = tokenizer(batch_summaries, return_tensors="pt", padding="longest" )['input_ids']
                lengths = torch.sum(indexed_summaries!=1, dim=-1) -2
                summary_lengths.extend(lengths.tolist())
    else:
        raise Exception('Cannot print statistics for ', target )
    
    if summaries is not None:
        fig, axes = plt.subplots(2, 1)
        axes[0].hist(article_lengths)
        axes[1].hist(summary_lengths)
        plt.show()
        print("The statistics of article length:", pd.Series(article_lengths).describe())
        print("The statistics of summary (reference) length:",  pd.Series(summary_lengths).describe())
    else:
        plt.hist(article_lengths)
        plt.show()
        print("The statistics of article length:", pd.Series(article_lengths).describe())


def generate_batch(articles, summaries=None, bsz=32):
    
    if summaries is not None:
        summaries_iter = iter(summaries)
    articles_iter = iter(articles)

    while True:
        
        batch_articles = list(islice(articles_iter, bsz))
        if len(batch_articles) > 0:
            if summaries is not None:
                batch_summaries = list(islice(summaries_iter, bsz))
                yield batch_articles, batch_summaries
            else: 
                yield batch_articles
        else: 
            break

