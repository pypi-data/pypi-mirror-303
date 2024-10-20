import pandas as pd
import os
import numpy as np

def get_prompts(ids, model_name):
    II2V_id = [450, 451, 452, 453, 454, 455, 615, 616, 617]
    prompts_df = pd.read_excel('https://video-gen.oss-cn-beijing.aliyuncs.com/input/prompts.xlsx')
    input_df = pd.read_excel('https://video-gen.oss-cn-beijing.aliyuncs.com/input/input.xlsx')
    
    results = {"text prompt": [], "visual prompt": [], "save name": []}
    
    for id in ids:
        save_name = model_name + '_' + str(id).zfill(5) + '.mp4'
        prompt_row = prompts_df[prompts_df['ID'] == id].iloc[0]
        
        results["text prompt"].append(prompt_row['Text Prompt'])
        
        if prompt_row['Type'] != 't2v' and id not in II2V_id:
            matching_url = input_df[input_df['url'].apply(lambda x: int(x.split('/')[-1].split('.')[0]) == id)]['url'].iloc[0]
            results["visual prompt"].append(matching_url)
        elif id in II2V_id:
            matching_url_1st = input_df[input_df['url'].apply(lambda x: int(x.split('/')[-1].split('.')[0]) == id)]['url'].iloc[0]
            matching_url_last = matching_url_1st.replace(str(id).zfill(5), str(id).zfill(5)+'_last')
            matching_url = [matching_url_1st, matching_url_last]
            results["visual prompt"].append(matching_url)
        else:
            results["visual prompt"].append(None)
        results["save name"].append(save_name)
    return results