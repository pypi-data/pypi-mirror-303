"""
    Copyright (C) 2024  Guo Zhengyang

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import pandas as pd
from adams.tool_kit import *
import cupy as cp
from scipy.spatial import distance_matrix as dm
import numpy as np
import os
import pickle as pkl
import GPUtil
import subprocess
from tqdm import tqdm

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    return gpus

class ADAMS_match():
    def __init__(self, ref, gpu_usage, threshold=0.95):
        self.ref = ref
        self.features = cp.array([])
        self.distance_matrix = np.array([])
        self.label = []
        self.threshold = threshold
        self.extract_features()
        self.gpu_usage = gpu_usage
        self.total_task = 0
        self.chunk_size = 0
        self.process = []
        self.raw_result = []

    def extract_features(self):
        ca = get_coordinate(self.ref, 'X')
        dist = dm(ca, ca)
        features = extract_features(dist)
        features = norm(features)
        self.distance_matrix = dist
        self.features = cp.array(features)
        self.label = set(categorize_matrix(np.array(features),mode='embed')) ##
    def match(self, db_folder, temp, prefilter_threshold=0.01):
        if not os.path.exists(temp):
            os.mkdir(temp)
        with open('./feature.pkl','wb') as f:
            pkl.dump(self.features,f)
        script_path = subprocess.run('which compare_all.py',text=True,shell=True,capture_output=True).stdout[:-1]
        with open(os.path.join(db_folder,'prefilter.pkl'),'rb') as f:
          prefilter_label = pkl.load(f)
        passed_protein = []
        for i in tqdm(prefilter_label,desc='prefilter'):
          try:
            if len(self.label & i[1])> (prefilter_threshold*len(self.label)):
              passed_protein.append(os.path.join(db_folder,i[0]+'.pkl'))
          except:
              continue
        print(f'{len(passed_protein)} structures passed')
        plst_path = os.path.join(temp,'prefilter')
        with open(plst_path,'wb') as f:
          pkl.dump(passed_protein,f)
        gpus = get_gpu_info()
        gpu_tasks = [int(n.memoryFree / 2000)  for n in gpus]
        for i in self.gpu_usage:
            self.total_task += gpu_tasks[i]
        files = os.listdir(db_folder)
        self.chunk_size = int(len(passed_protein) / self.total_task) + 1
        total = 0
        for i in self.gpu_usage:
            gpu = i
            max_task = gpu_tasks[i]
            current_task = 0
            for j in range(gpu_tasks[i]):
                start = total * self.chunk_size
                if current_task < max_task:
                    process = subprocess.Popen(
                        f'python {script_path} --ver {total} --feature_file ./feature.pkl --db_folder {plst_path} --ind1 {start} --ind2 {start + self.chunk_size} --device {gpu} --out_folder {temp}',shell=True,text=True)
                    self.process.append(process)
                total += 1
        for i in self.process:
            i.wait()
        name = []
        match = []
        score = []
        identity = []
        files = os.listdir(temp)
        for i in files:
            if i[-4:] == '.pkl':
                with open(os.path.join(temp, i), 'rb') as f:
                    data = pkl.load(f)
                name.extend([n[0] for n in data])
                match.extend([n[1] for n in data])
                score.extend([n[2] for n in data])
                id_lst = []
                for n in data:
                    if n[3] != n[1]:
                      id_lst.append(n[1]/(n[3]-n[1]))
                    else:
                      id_lst.append(1)
                identity.extend(id_lst)
        score_z = z_score(score)
        match_z = z_score(match)
        total_z = score_z + match_z

        result = pd.DataFrame(
                {'name': name, 'match': match, 'score': score, 'z_match': match_z, 'z_score': score_z, 'z': total_z,'identity':identity})
        os.system(f'rm -r {temp}'+'/*')
        result = result[result['match']!=0]
        result_sort = result.sort_values(by='identity',ascending=False)
        return result_sort
