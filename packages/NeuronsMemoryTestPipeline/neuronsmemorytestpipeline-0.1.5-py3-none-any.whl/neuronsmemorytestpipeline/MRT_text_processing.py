
import pandas as pd
pd.options.display.show_dimensions = False
from tqdm.auto import tqdm
import time
from fuzzywuzzy import fuzz

def catch_typo(to_correct, presented):
    # short entries are sent to further processing then 
    # Check Levenshtein distance against potential matches

    if len(to_correct) > 3:
        potential_matches = [b for b in presented if fuzz.partial_ratio(to_correct, b) >= 85]
        if len(potential_matches) > 0:
            return True
        # Check common typo patterns against potential matches (add your patterns)
        typo_patterns = {'l': 'i', 'i': 'l', 'p': 'b', 'b': 'p', 'o': 'a', 'a': 'o', 'e': 'i', 'i': 'e'}
        for char, typo in typo_patterns.items():
            if any(typo in to_correct and char in match for match in potential_matches):
                return True
    return False

def catch_abbreviation(to_correct, presented):
    """
    Checks if a phrase matches the abbreviated form of any entry in a given list.
    Args:
    to_correct (str): The phrase to check.
    presented (list of str): The list of full phrases.
    Returns:
    str or None: The original phrase corresponding to the abbreviation if a match is found, otherwise None.
    """
    
    def generate_abbreviation(phrase):
        return ''.join(word[0].upper() for word in phrase.split())
    
    corrected_abbreviation = to_correct.upper()

    for entry in presented:
        if generate_abbreviation(entry) == corrected_abbreviation:
            #print(f'         {to_correct} -> {entry}')
            return entry
    return None

def catch_lower_upper_case(to_correct, presented):
    """
    Checks if a phrase matches the lower or upper case form of any entry in a given list.
    Args:
    to_correct (str): The phrase to check.
    presented (list of str): The list of full phrases.
    Returns:
    str or None: The original phrase corresponding to the abbreviation if a match is found, otherwise None.
    """
    def lower_case(phrase):
        return phrase.lower()

    corrected_abbreviation = to_correct.lower()
    for entry in presented:
        if lower_case(entry) == corrected_abbreviation:
            #print(f'         {to_correct} -> {entry}')
            return entry
    return None

def clean_text_ai(brands_presented, brands_to_clean, model):
    res_all = []
    for brand_to_correct in tqdm(brands_to_clean):

        prompt = f"""
            You are a professional Brand Name Spell Checker. 
            Given 2 variables:
                potential_responses = {brands_presented}
                brand_to_check = {brand_to_correct}
            Identify if brand_to_check is in the potential_responses, it can be misspelled, using: 
                - spelling similarity of at least 98%
                - edit distance <= 2
                - semantic similairy of 90%.
            Return "Not Found" if brand_to_check is not in the potential_responses or no close match exists.
                Examples of acceptable variations: "Addidas" -> "Adidas", "Nke" -> "Nike", "ume" -> "Puma",  "Bang"->"Bang & Olufsen"
                Examples of brand_to_check that must return "Not Found": "Can\'t remember", "don\'t know", "None"
                Further examples of Unacceptable variations: "I don't know" -> "Panasonic", "Sony" -> "Panasonic" , "Life"->"Bang & Olufsen"
                
             **Only return ONE option FROM the potential_responses OR "Not Found" as a response**
             Example to return: "Guess" or "Nike" or "Burger King" if "Guess" or "Nike" or "Burger King" are in the potential_responses
            Do not return anything diffrent than the potential_responses or "Not Found"!
            """
        
        res = model.predict(prompt)
        try: 
            res_all.append({'given_response_label_presented':brand_to_correct, 'typed_brand':res.text})
        except:
            res_all.append({'given_response_label_presented':brand_to_correct, 'typed_brand':"Not Found"})

        time.sleep(0.3)
    
    df_cleaned = pd.DataFrame(res_all)
    df_cleaned.columns = ['original','corrected']
    return df_cleaned

def add_correct_entries(df, brand_cleaned):
    brand_cleaned.columns = ['given_response_label_presented', 'corrected', 'method']
    merged_df = pd.merge(df, brand_cleaned, on='given_response_label_presented', how='left')
    merged_df['recalled_brand'] = merged_df['corrected'].fillna('Not Found')
    merged_df = merged_df.drop(['corrected'], axis=1)
    return merged_df

    
def calculate_corrected_brands(df, brands_presented):
    """
    Calculates the total number of the updated/ corrected brand names obtained from the free text recall
    Args:
        df (pandas df): data frame that contains typed_brand column
    Returns:
        grouped_df: aggregated dataframe per group with counts of corrected brand names.
    """
    count_df = df.loc[df.recalled_brand.isin(brands_presented)].reset_index(drop=True)

    count_df = count_df.drop_duplicates(['participant_id', 'recalled_brand', 'method'])
    corrected_counts = count_df.groupby(['group_id','method']).recalled_brand.value_counts()
    pd.set_option('display.max_rows', None)
    print('*'*50)
    print('\nList of Corrected Entries by Method Used:')
    print(corrected_counts)
    pd.reset_option('display.max_rows')     
    corrected_counts = corrected_counts.reset_index()

    return corrected_counts

def clean_free_recall (df, brands_presented, brands_to_clean, model):
    print('*'*50)
    df['method'] =  ''
    df['corrected'] = ''
    for row in df.itertuples():
        index = row.Index
        brand = row.given_response_label_presented      
        match_abbr = catch_abbreviation(brand, brands_presented)
        match_lower = catch_lower_upper_case(brand, brands_presented)
        if match_abbr:
            #print('ABBREVIATION')
            df.at[index, 'corrected'] = match_abbr
            df.at[index, 'method'] = 'abbreviation'
            
        elif match_lower:
            #print('CASE')
            df.at[index, 'corrected'] = match_lower
            df.at[index, 'method'] = 'case'
        
        else:
            if catch_typo(brand, brands_presented):
                closest_match = sorted(brands_presented, key=lambda b: fuzz.partial_ratio(brand, b), reverse=True)[0]
                #print(f'         {brand} -> {closest_match}')
                #print('FUZZY')
                df.at[index, 'corrected'] = closest_match
                df.at[index, 'method'] = 'fuzzy'
            else:
                if fuzz.ratio(brand, brands_presented) <= 15:
                    df.at[index, 'corrected'] = ''
                    df.at[index, 'method'] = 'not_match'
                else:
                    df.at[index, 'corrected'] = ''
                    df.at[index, 'method'] = 'maybe'
    print(f"\nThere are {df[df.method =='abbreviation'].shape[0]} entries that were indentified as a match using Abbreviation.")
    print(f"\nThere are {df[df.method =='case'].shape[0]} entries that were indentified as a match using Lower Upper Case.")
    print(f"\nThere are {df[df.method =='fuzzy'].shape[0]} entries that were indentified as a match using Fuzzy.")
    df.loc[df['given_response_label_presented'].isin(['others', 'other', 'Others']), 'method'] = 'not_match'
    print(f"\nThere are {df[df.method =='not_match'].shape[0]} entries that do not match targeted Brands at all.")
    print(f"\nThere are {df[df.method =='maybe'].shape[0]} entries that will be further analyzed with AI.")

    further = df[df.method == 'maybe'].copy()
    further['corrected'] = ''
    df = df[df.method != 'maybe'].copy()
    if len(further)>0:
        clean_df_2 = clean_text_ai(brands_presented, further['given_response_label_presented'].unique(), model = model)
        clean_df_2 = clean_df_2[clean_df_2.corrected!='Not Found'].copy()
        for row in further.itertuples():
            index = row.Index
            brand = row.given_response_label_presented
            if brand in clean_df_2.original.unique():
                #print('AI')
                #print(f"         {brand} -> {clean_df_2.loc[clean_df_2.original == brand]['corrected'].values[0]}")
                further.at[index, 'corrected'] = clean_df_2.loc[clean_df_2.original == brand]['corrected'].values[0]
                further.at[index, 'method'] = 'ai'
            else:
                further.at[index, 'method'] = 'not_match'
                
    print(f"\nThere are {further[further.method =='ai'].shape[0]} entries that were indentified as a match using AI.")
    final_df = pd.concat([df, further], axis=0, ignore_index=True)
    value_counts = final_df['method'].value_counts()
    print('*'*50)
    for method, count in value_counts.items():
        print(f"{method}: {count}")
    return final_df
