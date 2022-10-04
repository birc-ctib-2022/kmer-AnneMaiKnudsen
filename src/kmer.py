"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """

    liste=[]
    for i in range(0,len(x)-k+1):
        liste.append(x[i:i+k])
    return liste

    ...


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    >>> unique_kmers('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """
    list=[]
    for i in range(len(x)-k+1):
        if x[i:i+k] not in list:
            list.append(x[i:i+k])
    return list
    ...


def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    >>> count_kmers('agtagtcg', 3)
    {'agt': 1, 'gta': 1, 'tag': 1, 'gtc': 1, 'tcg': 1}
    
    FIXME: do you want more tests here?
    """
    lis=[]
    for i in range(len(x)-k+1):
        if x[i:i+k] not in lis:
            lis.append(x[i:i+k])
    counts=dict.fromkeys(lis,0)

    for k in lis:
        counts[k]+=1
    return counts
    

    ...

