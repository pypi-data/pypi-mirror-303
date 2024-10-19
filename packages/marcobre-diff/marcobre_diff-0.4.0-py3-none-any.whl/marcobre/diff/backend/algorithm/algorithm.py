import pandas as pd
import os
import time
import numpy as np
import multiprocessing
import subprocess
import math
from .constants import GRADES
import datetime
from marcobre.diff.backend.backend import create_historical,get_all_historical


def sweep_level(lv_ref_y,ref_df, cmp_df, lv, ref_lv_index, cmp_lv_index):
    print(f"lv: {lv}")
    j = ref_lv_index[0]
    ref_max_index = ref_lv_index[1]
    diff_index = []
    cmp_max_index = cmp_lv_index[1]
    for i in range(cmp_lv_index[0], cmp_lv_index[1]):
        # print(f"[{lv}] {i}/{cmp_max_index}, {j}/{ref_max_index}", end='\r')
        if j >= ref_max_index:
            diff_index.append(i)
            continue

        cmp_block = cmp_df.loc[i]

        match_cmp_block = False



        while not match_cmp_block and j < ref_max_index:
            ref_block = ref_df.loc[j]

            if ref_block.Y < cmp_block.Y:  # jump on Y
                target_y = cmp_block.Y
                ref_y_index = int(lv_ref_y[lv_ref_y.index < target_y].sum())

                jump_index = ref_lv_index[0] + ref_y_index
                if j < jump_index:
                    j = jump_index
                else:
                    j += 1
                continue

            if ref_block.Y <= cmp_block.Y and ref_block.X < cmp_block.X:  # jump on X
                jump = 1
                j += jump
                continue

            cmp_block_xyz = np.array([cmp_block.X, cmp_block.Y, cmp_block.Z])
            ref_block_xyz = np.array([ref_block.X, ref_block.Y, ref_block.Z])
            # reference block is ahead of cmp_block (NEW BLOCK)
            if sum(ref_block_xyz > cmp_block_xyz) >= 1:
                diff_index.append(i)
                break

            else:
                match_cmp_block = True

                new_diff_index = False
                for var in GRADES:
                    if not math.isclose(cmp_block[var], ref_block[var]):
                        new_diff_index = True
                        break

                if new_diff_index:
                    diff_index.append(i)
                j += 1

    return diff_index


def sweep_level_vector(args):
    lv_ref_y,ref_df, cmp_df, lv, ref_lv_index, cmp_lv_index = args
    return sweep_level(lv_ref_y,ref_df, cmp_df, lv, ref_lv_index, cmp_lv_index)


def algorithm_function(ref_file,cmp_file):
    ref_df = pd.read_csv(ref_file)
    cmp_df = pd.read_csv(cmp_file)
    ref_df[["X", "Y", "Z"]] = ref_df[["X", "Y", "Z"]].round(1)
    cmp_df[["X", "Y", "Z"]] = cmp_df[["X", "Y", "Z"]].round(1)

    # Filter empty blocks
    ref_df[GRADES] = ref_df[GRADES].round(4)
    cmp_df[GRADES] = cmp_df[GRADES].round(4)
    ref_df = ref_df[ref_df[GRADES].agg('sum', axis=1) > 0]
    cmp_df = cmp_df[cmp_df[GRADES].agg('sum', axis=1) > 0]

    # Sort and re-index for comparison
    ref_df = ref_df.sort_values(by=["Z", "Y", "X"]).reset_index(drop=True)
    cmp_df = cmp_df.sort_values(by=["Z", "Y", "X"]).reset_index(drop=True)

    # Jump on Z
    ref_lv = ref_df.groupby("Z").Z.count()
    cumsum_ref_lv = ref_lv.cumsum().to_dict()
    cmp_lv = cmp_df.groupby("Z").Z.count()
    cumsum_cmp_lv = cmp_lv.cumsum().to_dict()
    ref_lvs = set(cumsum_ref_lv.keys())
    cmp_lvs = set(cumsum_cmp_lv.keys())
    lvs = list(set.intersection(ref_lvs, cmp_lvs))
    lvs.sort()
    ref_lv_min_index = 0
    cmp_lv_min_index = 0



    lv_index = {}
    for lv in lvs:
        ref_lv_max_index = cumsum_ref_lv[lv]
        cmp_lv_max_index = cumsum_cmp_lv[lv]

        # {lv: [ref_lv_index_range, cmp_lv_index_range]}
        lv_index[lv] = [(ref_lv_min_index, ref_lv_max_index), (cmp_lv_min_index, cmp_lv_max_index)]

        ref_lv_min_index = ref_lv_max_index
        cmp_lv_min_index = cmp_lv_max_index

    # Jump on Y
    ref_y = ref_df.groupby(by=["Z", "Y"]).Y.count()
    current_lv = 710.0
    lv_ref_y = ref_y.loc[current_lv]

    levels = []

    for lv, lv_indexes in lv_index.items():
        ref_lv_index, cmp_lv_index = lv_indexes
        lv_ref_df = ref_df[ref_df.Z == lv].copy()
        lv_cmp_df = cmp_df[cmp_df.Z == lv].copy()
        levels.append([lv_ref_y,lv_ref_df, lv_cmp_df, lv, ref_lv_index, cmp_lv_index])

    cpus = -1
    max_cpus = multiprocessing.cpu_count()
    cpus = max_cpus if cpus > max_cpus or cpus <= 0 else cpus
    diff_start_time = time.time()
    print(diff_start_time)
    pool = multiprocessing.Pool(processes=cpus)
    diff_index_pool = pool.map(sweep_level_vector, levels)
    elapsed_time = time.time() - diff_start_time
    diff_index = []
    for diff_index_process in diff_index_pool:
        diff_index += diff_index_process
    diff_df = cmp_df.loc[diff_index]

    # Create file
    # Define the directory to save the output
    user_home = os.path.expanduser("~")
    output_dir = os.path.join(user_home, 'marcobre')

    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create file
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    ref_filename = os.path.basename(os.path.splitext(ref_file)[0])
    cmp_filename = os.path.basename(os.path.splitext(cmp_file)[0])
    output_filename = f"{ref_filename}__{cmp_filename}_{current_datetime}.csv"
    output_path = os.path.join(output_dir, output_filename)
    print(output_path)
    diff_df.to_csv(output_path)

    #save in DB
    create_historical(f"{ref_filename}.csv",f"{cmp_filename}.csv",f"{ref_filename}__{cmp_filename}_{current_datetime}.csv")
    historical_records = get_all_historical()
    print(historical_records)
    # Open the output directory
    if os.name == 'nt':  # For Windows
        os.startfile(output_dir)
    elif os.name == 'posix':  # For macOS/Linux
        subprocess.run(['open', output_dir])  # macOS
