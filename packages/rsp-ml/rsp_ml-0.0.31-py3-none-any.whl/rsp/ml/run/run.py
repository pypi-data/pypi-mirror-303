import os
from datetime import datetime
import numpy as np
import json
import matplotlib.pyplot as plt
import torch
import rsp.common.console as console
import pickle as pkl

class Run():
    def __init__(self, id = None, moving_average_epochs = 1000):
        if id is None:
            self.id = datetime.now().strftime('%Y%m%d%H%M%S%f')
            self.data = {}
        else:
            self.id = id
            self.__load__()
            
        self.moving_average_epochs = moving_average_epochs
        self.__init_run_dir__()
    
    def append(self, key:str, phase:str, value):
        if not key in self.data:
            self.data[key] = {}
        if not phase in self.data[key]:
            self.data[key][phase] = {
                'val': [],
                'avg': []
            }
        if np.isnan(value):
            if len(self.data[key][phase]['val']) > 0:
                value = self.data[key][phase]['val'][-1]
            else:
                value = 0.

        self.data[key][phase]['val'].append(value)
        self.data[key][phase]['avg'].append(np.average(self.data[key][phase]['val'][-self.moving_average_epochs:]))

    def plot(self):
        if not os.path.isdir(f'runs/{self.id}/plot'):
            os.mkdir(f'runs/{self.id}/plot')

        for key in self.data:
            key_str = key.replace('_', ' ')
            fname = f'runs/{self.id}/plot/{key}.jpg'

            cmap = plt.get_cmap('tab20b')
            colors = cmap(np.linspace(0, 1, len(self.data[key])))

            for i, phase in enumerate(self.data[key]):
                if len(self.data[key][phase]['val']) == 0:
                    continue
                plt.plot(self.data[key][phase]['val'], color=colors[i], alpha=0.3)
                plt.plot(self.data[key][phase]['avg'], label=phase, color=colors[i])

            plt.title(key_str)
            plt.xlabel('episode')
            plt.ylabel(key_str)
            plt.minorticks_on()
            plt.grid(which='minor', color='lightgray', linewidth=0.2)
            plt.grid(which='major', linewidth=.6)
            plt.legend()
            plt.savefig(fname)
            plt.close()

    def save(self):
        self.__init_run_dir__()
        with open(f'runs/{self.id}/data.json', 'w') as f:
            json.dump(self.data, f)

    def get_val(self, key:str, phase:str):
        return self.data[key][phase]['val'][-1]
    
    def get_avg(self, key:str, phase:str):
        return self.data[key][phase]['avg'][-1]
    
    def len(self):
        l = 0
        for key in self.data:
            for phase in self.data[key]:
                l_temp = len(self.data[key][phase]['val'])
                if l_temp > l:
                    l = l_temp
        return l

    def __init_run_dir__(self):
        if not os.path.isdir('runs'):
            os.mkdir('runs')
        self.directory = f'runs/{self.id}'
        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)
        self.plot_directory = f'{self.directory}/plot'
        if not os.path.isdir(self.plot_directory):
            os.mkdir(self.plot_directory)

    def __load__(self):
        if not os.path.isfile(f'runs/{self.id}/data.json'):
            self.data = {}
        else:
            with open(f'runs/{self.id}/data.json', 'r') as f:
                self.data = json.load(f)

    def save_state_dict(self, state_dict, fname = 'state_dict.pt'):
        self.__init_run_dir__()
        with open(f'runs/{self.id}/{fname}', 'wb') as f:
            torch.save(state_dict, f)

    def load_state_dict(self, model:torch.nn.Module, fname = 'state_dict.pt'):
        if not os.path.isfile(f'runs/{self.id}/{fname}'):
            console.warn(f'File runs/{self.id}/{fname} not found.')
            return
        with open(f'runs/{self.id}/{fname}', 'rb') as f:
            model.load_state_dict(torch.load(f))

    def save_model(self, model:torch.nn.Module, fname = 'model.pkl'):
        self.__init_run_dir__()
        with open(f'runs/{self.id}/{fname}', 'wb') as f:
            pkl.dump(model, f)

    def load_model(self, fname = 'model.pkl'):
        if not os.path.isfile(f'runs/{self.id}/{fname}'):
            console.warn(f'File runs/{self.id}/{fname} not found.')
            return
        with open(f'runs/{self.id}/{fname}', 'rb') as f:
            model = pkl.load(f)
        return model