import urllib.request
import requests
from tqdm import tqdm
from pathlib import Path
from urllib.request import urlretrieve
import pickle as pkl
import os
from enum import Enum
import torch
import torch.nn as nn
#import rsp.ml.model.TUC.ActionPrediction.model

#ONDEDRIVE_MODEL = 'https://1drv.ms/f/s!Aus2Qv-6ArmHiNNSLeOghncOzEJXVA?e=9nRSIf'

class MODEL_ID(Enum):
    TUC_ActionPrediction_Model004 = 'https://4qjlxa.am.files.1drv.com/y4mfQfn43y0SaOn9h0AYy123zQkYob5DwXL1mBzezMSufgtzGVYsYHRBMbr7ex_YYrzJZY9AC7MdmV_CRZJBb2ea6eLwkE3idjgceMHf2k1eIneOciwYEvkZpa1JY0Bc1YPsHBcHVajywZRb_6V6H39OIrKN5Hjkp0DZKIB-ZS3cw8LGjraX6oaJ4eD1WjyonL_Z91AGWpgPZ9Ip5rT9oksMU1oNtJv3ThRSIMV2TfIXJw?AVOverride=1'

def load_state_dict(model_id:MODEL_ID, force_reload:bool = False):
    out_file = Path('model').joinpath(f'{model_id.name}.pt')
    out_file.parent.mkdir(parents = True, exist_ok = True)

    model_library = __import__(f'rsp.ml.model.TUC.ActionPrediction.model', 'Model4')
    model = model_library.__dict__['TUC']['ActionPrediction']

    if not out_file.exists() or force_reload:
        url = model_id.value
        r = requests.get(url, allow_redirects=True)
        with open(out_file, 'wb') as f:
            f.write(r.content)
            #pkl.dump(r.content, f)

    out_file = '/Users/schulzr/Documents/GIT/tuc-actionprediction/runs/model004/model.pkl'
    
    with open(out_file, 'rb') as f:
        model = pkl.load(f)

    return model

if __name__ == '__main__':
    model = load_state_dict(MODEL_ID.TUC_ActionPrediction_Model004, force_reload = True)
    pass