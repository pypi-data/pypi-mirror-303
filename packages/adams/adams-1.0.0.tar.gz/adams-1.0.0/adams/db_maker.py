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
from adams.tool_kit import *
import os
from scipy.spatial import distance_matrix
import cupy as cp
import pickle as pkl
from tqdm.contrib.concurrent import process_map
from functools import partial
import gzip


def get_feature_list(pdb_folder, out_folder, file):
    error = []
    try:
        ca = get_coordinate(os.path.join(pdb_folder, file), 'X')
        name = file[:-4]
        dist = distance_matrix(ca, ca)
        dist = extract_features(dist)
        dist = norm(dist)
        length = len(ca)
        # return name, dist, length
        with open(os.path.join(out_folder, file[:-3]+'pkl'), 'wb') as f:
            pkl.dump([name, dist, length], f)
        label = set(categorize_matrix(np.vstack(dist),mode='embed'))
        return (name,label)
    except:
        error.append('1')



class DatabaseMaker():
    def __init__(self, device=0, process=40):
        self.device = device
        self.process = process

    def make(self, pdb_folder, out_folder):
        mempool = cp.get_default_memory_pool()
        files = os.listdir(pdb_folder)
        feature_p = partial(get_feature_list, pdb_folder, out_folder)
        result = process_map(feature_p,files,max_workers=self.process,chunksize = int(len(files)/self.process))
        with open(os.path.join(out_folder,'prefilter.pkl'),'wb') as f:
          pkl.dump(result,f)
        mempool.free_all_blocks()

