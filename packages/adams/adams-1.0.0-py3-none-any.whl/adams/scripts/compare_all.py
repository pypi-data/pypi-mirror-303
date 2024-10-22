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

import argparse
import pickle as pkl
import os
import cupy as cp
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--feature_file')
parser.add_argument('--ver')
parser.add_argument('--db_folder')
parser.add_argument('--ind1')
parser.add_argument('--ind2')
parser.add_argument('--device')
parser.add_argument('--out_folder')
args = parser.parse_args()

db_folder, part, ind1, ind2, device, out_folder,feature_path = args.db_folder, args.ver, int(args.ind1), int(args.ind2), int(
    args.device), args.out_folder, args.feature_file

def match(feature, path):
    try:
        with open(path, 'rb') as f:
            data = pkl.load(f)
        name = data[0]
        dt = data[1]
        len2 = dt.shape[0]
        dt = cp.array(dt)
        len1 = feature.shape[0]
        feature = cp.array(feature)
        res = cp.max(cp.dot(dt, feature.T) - 0.95, axis=0)
        ind = res > 0
        score = float(cp.sum(res * ind))
        match = int(cp.sum(ind))
        sumup = len1+len2
        return name, match, score, sumup
    except:
        return 0, 0, 0, 0


with open(db_folder,'rb') as f:
  path = pkl.load(f)
with open(feature_path, 'rb') as f:
    feature = pkl.load(f)
with cp.cuda.Device(device):
    feature = cp.array(feature)
    mempool = cp.get_default_memory_pool()
    res = []
    for j in path[ind1:ind2]:
        res.append(match(feature, j))
    mempool.free_all_blocks()
    with open(out_folder + '/{}.pkl'.format(j.split('/')[-1].split('.')[0]), 'wb') as f:
        pkl.dump(res, f)
