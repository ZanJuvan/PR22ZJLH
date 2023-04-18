import pandas as pd
from sklearn.linear_model import LinearRegression
import random
pesmi = pd.read_csv('tcc_ceds_music.csv')

def predlagaj_pesem(pesmi_training):
    predict_max = 0
    pesem = pesmi.sample().iloc[0]
    xp = np.array(pesem[['len', 'dating', 'violence', 'world/life', 'night/time',
                            'shake the audience', 'family/gospel', 'romantic', 'communication', 'obscene',
                            'music', 'movement/places', 'light/visual perceptions', 'family/spiritual',
                            'like/girls', 'sadness', 'feelings', 'danceability', 'loudness', 'acousticness',
                            'instrumentalness', 'valence', 'energy', 'age']])
    pesem_max=pesem
    i = 0
    while (i < 100):
        i += 1
        x = pesmi_training[['len', 'dating', 'violence', 'world/life', 'night/time',
                            'shake the audience', 'family/gospel', 'romantic', 'communication', 'obscene',
                            'music', 'movement/places', 'light/visual perceptions', 'family/spiritual',
                            'like/girls', 'sadness', 'feelings', 'danceability', 'loudness', 'acousticness',
                            'instrumentalness', 'valence', 'energy', 'age']]
        y = pesmi_training['ocena']
        y = np.array(y).reshape(-1, 1)
        x = np.array(x).reshape(-1,24)

        lr = LinearRegression()
        lr.fit(x, y)

        pesem = pesmi.sample().iloc[0]

        xp = np.array(pesem[['len', 'dating', 'violence', 'world/life', 'night/time',
                              'shake the audience', 'family/gospel', 'romantic', 'communication', 'obscene',
                              'music', 'movement/places', 'light/visual perceptions', 'family/spiritual',
                              'like/girls', 'sadness', 'feelings', 'danceability', 'loudness', 'acousticness',
                              'instrumentalness', 'valence', 'energy', 'age']])
        predict = lr.predict(xp.reshape(1, -1))
        if(predict_max<predict):
            predict_max=predict
            pesem_max=pesem
    return pesem_max
    

pesem=pesmi.sample().iloc[0]
print(pesem['artist_name'], "-", pesem['track_name'])
ocena=input("Oceni pesem:")
pesem["ocena"]=ocena
pesmi_training=pd.DataFrame
pesmi_training=pesem[["len","dating","violence","world/life","night/time",
                       "shake the audience","family/gospel","romantic","communication","obscene",
                       "music","movement/places","light/visual perceptions","family/spiritual",
                       "like/girls","sadness","feelings","danceability","loudness","acousticness",
                       "instrumentalness","valence","energy","age","ocena"]]
i=0
while(i<5):
    i+=1
    pesem=pesmi.sample().iloc[0]
    print(pesem['artist_name'], "-", pesem['track_name'])    
    ocena=input("Oceni pesem:")
    pesem["ocena"]=ocena
    pesmi_training=pesmi_training.append(pesem[["len","dating","violence","world/life","night/time",
                                                 "shake the audience","family/gospel","romantic","communication","obscene",
                                                 "music","movement/places","light/visual perceptions","family/spiritual",
                                                 "like/girls","sadness","feelings","danceability","loudness","acousticness",
                                                 "instrumentalness","valence","energy","age","ocena"]])
i = 0
while i < 500:
    i += 1
    pesem = predlagaj_pesem(pesmi_training)
    print(pesem['artist_name'], "-", pesem['track_name'])
    ocena = input("Oceni pesem:")
    pesem["ocena"] = ocena  
    pesmi_training=pesmi_training.append(pesem[["len","dating","violence","world/life","night/time",
                                                 "shake the audience","family/gospel","romantic","communication","obscene",
                                                 "music","movement/places","light/visual perceptions","family/spiritual",
                                                 "like/girls","sadness","feelings","danceability","loudness","acousticness",
                                                 "instrumentalness","valence","energy","age","ocena"]])