import pandas as pd


def save_series_list():
    print('Reading IMDB data')
    imdb_titles = None
    try:
        imdb_titles = pd.read_table('../../data/imdb_entries.tsv', low_memory=False)
    except:
        print('Please download dataset from https://datasets.imdbws.com/title.basics.tsv.gz')
    series = imdb_titles[(imdb_titles.titleType == 'tvSeries') | (imdb_titles.titleType == 'tvMiniSeries')]
    series = series[series.startYear.apply(lambda x: x.isnumeric())]
    series = series[pd.to_numeric(series.startYear).apply(lambda x: 1970 < x < 2019)]
    series = series[series.genres != r'\N'][['primaryTitle', 'startYear', 'genres']]
    print('Writing to data/series.csv')
    series.to_csv('../../data/series.csv')


save_series_list()
