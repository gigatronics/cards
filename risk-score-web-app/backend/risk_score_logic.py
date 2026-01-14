import os 
import json
import pandas as pd 

def find_top_matches(new_json, old_jsons,n) -> list:

    def jaccard(json1, json2) -> float:
        # get key & values
        set1 = {key for key, value in json1.items() if value is True}
        set2 = {key for key, value in json2.items() if value is True}
        
        # calc intersection and union
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        
        # calc jccard similarity 
        return len(intersection) / len(union) if union else 0

    # return the top n similar JSONs, along with their scores
    scored_jsons = [{"title": old_json['filename'], "score": jaccard(new_json, old_json)} for old_json in old_jsons]

    # sort in a descending order 
    sorted_jsons = sorted(scored_jsons, key=lambda x: x['score'], reverse=True)

    return sorted_jsons[:n]     #scored_jsons[:n]    


# give three campaign names and output their respective pmdef count
def get_pmdef_count(list, df) -> dict:
    return df.loc[df['campaign'].isin(list)].to_dict(orient='records') 



def main():
    # setup path
    print(os.getcwd())
    path = os.path.join(os.getcwd(), 'cards/config')
    fs = [f for f in os.listdir(path) if 'json' in f]

    # load input files
    test_json = json.load(open(path+'/'+'aero rec n ent.json', 'r')) 
    known_jsons = [json.load(open(path+'/'+f, 'r')) for f in fs] 

    # find top 3 similar offers 
    top3 = find_top_matches(test_json, known_jsons, 3)
    print(f'the top 3 matches are: {top3}')

    # extract title, and get pmdef counts
    top3_list = [match['title'] for match in top3]
    df = pd.read_csv(os.path.join(os.getcwd(), 'cards', 'tmp_pmdef_cnt.csv'))

    print(f'the respective pmdef counts are: {get_pmdef_count(top3_list, df)}') 

if __name__ == '__main__':
    main()  

