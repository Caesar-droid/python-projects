def make_album(artist,album_name,songs=None):
    album_0={'musician':artist,'album':album_name}
    album_1={'musician':artist,'album':album_name}
    album_2={'musician':artist,'album':album_name}
    if songs:
        album_0['num.songs']=songs
    return album_0
    if songs:
        album_1['num.songs']=songs
    return album_1
    if songs:
        album_2['num.songs']=songs
    return album_2
industry_0=make_album('nav','good intentions',8)
print(industry_0)
industry_1=make_album('wiz khalifa','contact')
print(industry_1)
industry_2=make_album('davido','apollo',43)
print(industry_2)