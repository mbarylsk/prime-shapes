#
# Copyright (c) 2017-2019, Marcin Barylski
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, 
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice, 
#    this list of conditions and the following disclaimer in the documentation 
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, 
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY 
# OF SUCH DAMAGE.
#

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pickle
import math
from random import randint
import shapes
import dataprocessing
import os
import sys
sys.path.insert(0, '..\\primes\\')
import primes

#############################################################
# Settings - configuration
#############################################################

# Minimal and maximum number - range of iterations
min_num = 1
max_num = 1000000

# Checkpoint value when partial results are drawn/displayed
# should be greater than zero
checkpoint_value = 5000

# Caching previous primality results
#   o True  - auxilary sets of primes and composite numbers will grow
#             it will speed up further primality tests but more RAM will
#             be occupied
#   o False - do not cache new primality test results
caching_primality_results = False

# Cases to be checked
cases_to_check = {'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12'}

min_case = 1
max_case = 13

# Helper files
#   o file_input_primes - contains prime numbers
#   o file_input_nonprimes - contains composite numbers
file_input_primes = '..\\primes\\t_prime_numbers.txt'
file_input_nonprimes = '..\\primes\\t_nonprime_numbers.txt'

# Save figures with partial results
figures_save_partial_results = False

enable_points_lifetime = False
enable_optimized_points_save = True
continue_previous_calculations = True
use_3d_plotting = True

# Colors for points
color_no_turn = 0
color_turn = 0

lifetime_start = 10000

#############################################################
# Settings - output directory and files
#############################################################

directory = "results/" + str(max_num)
if not os.path.exists(directory):
    os.makedirs(directory)
file_output_shape_1 = directory + "/f_shape_1"
file_output_shape_2 = directory + "/f_shape_2"
file_output_shape_3 = directory + "/f_shape_3"
file_output_shape_4 = directory + "/f_shape_4"
file_output_shape_5 = directory + "/f_shape_5"
file_output_shape_6 = directory + "/f_shape_6"
file_output_shape_7 = directory + "/f_shape_7"
file_output_shape_8 = directory + "/f_shape_8"
file_output_shape_9 = directory + "/f_shape_9"
file_output_shape_10 = directory + "/f_shape_10"
file_output_shape_11 = directory + "/f_shape_11"
file_output_shape_12 = directory + "/f_shape_12"
file_output_extension = ".png"
file_output_pickle = directory + "/objs_shape.pickle"
file_output_stats = directory + "/objs_stats.csv"

#############################################################
# Results of calculations
#############################################################

new_x = []
new_y = []
new_z = []
delta_x = []
delta_y = []
delta_z = []
num_current = []
datax = []
datay = []
dataz = []
lifetime = []
colors = []
is_previous_prime = []
sign = []
stats_primes = []
stats_nonprimes = []
stats_iterations = []
k = 0
k_current = 0
num = 1

for i in range (min_case, max_case):
    new_x.append(0)
    new_y.append(0)
    new_z.append(0)
    delta_x.append(1)
    delta_y.append(0)
    delta_z.append(1)
    num_current.append(0)
    datax.append([])
    datay.append([])
    dataz.append([])
    lifetime.append([])
    colors.append([])
    is_previous_prime.append(False)
    sign.append(1)
    stats_primes.append(0)
    stats_nonprimes.append(0)
    stats_iterations.append(0)

#############################################################
# Presentation
#############################################################

def get_max_diff (tcid):
    diff_x = max(datax[tcid]) - min(datax[tcid])
    diff_y = max(datay[tcid]) - min(datay[tcid])
    diff_z = max(dataz[tcid]) - min(dataz[tcid])
    return (diff_x + 1, diff_y + 1, diff_z + 1)

def get_points (tcid):
    return (len(datax[tcid]))

def write_results_to_figures(save_partial_results, perc_completed, k):
    file_shape_1 = set_file_output_filename (file_output_shape_1, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_2 = set_file_output_filename (file_output_shape_2, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_3 = set_file_output_filename (file_output_shape_3, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_4 = set_file_output_filename (file_output_shape_4, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_5 = set_file_output_filename (file_output_shape_5, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_6 = set_file_output_filename (file_output_shape_6, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_7 = set_file_output_filename (file_output_shape_7, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_8 = set_file_output_filename (file_output_shape_8, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_9 = set_file_output_filename (file_output_shape_9, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_10 = set_file_output_filename (file_output_shape_10, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_11 = set_file_output_filename (file_output_shape_11, save_partial_results, "_" + str(perc_completed) + str(k))
    file_shape_12 = set_file_output_filename (file_output_shape_12, save_partial_results, "_" + str(perc_completed) + str(k))

    if 'c1' in cases_to_check:
        write_results_to_figure (1, 0, "n=2k+1 (k=1,2,3...); n from 3 to ", file_shape_1, False)
        write_results_to_figure (1, 0, "n=2k+1 (k=1,2,3...); n from 3 to ", file_shape_1 + "3d", True)
    if 'c2' in cases_to_check:
        write_results_to_figure (2, 1, "n=6k+1 (k=1,2,3...); n from 7 to ", file_shape_2, False)
        write_results_to_figure (2, 1, "n=6k+1 (k=1,2,3...); n from 7 to ", file_shape_2 + "3d", True)
    if 'c3' in cases_to_check:
        write_results_to_figure (3, 2, "n=6k-1 (k=1,2,3...); n from 5 to ", file_shape_3, False)
        write_results_to_figure (3, 2, "n=6k-1 (k=1,2,3...); n from 5 to ", file_shape_3 + "3d", True)
    if 'c4' in cases_to_check:
        write_results_to_figure (4, 3, "n=6k-+1 (k=1,2,3...); n from 5 to ", file_shape_4, False)
        write_results_to_figure (4, 3, "n=6k-+1 (k=1,2,3...); n from 5 to ", file_shape_4 + "3d", True)
    if 'c5' in cases_to_check:
        write_results_to_figure (5, 4, "n=1,2,3... ; n from 1 to ", file_shape_5, False)
        write_results_to_figure (5, 4, "n=1,2,3... ; n from 1 to ", file_shape_5 + "3d", True)
    if 'c6' in cases_to_check:
        write_results_to_figure (6, 5, "n=30k+1 (k=1,2,3...); n from 4 to ", file_shape_6, False)
        write_results_to_figure (6, 5, "n=30k+1 (k=1,2,3...); n from 4 to ", file_shape_6 + "3d", True)
    if 'c7' in cases_to_check:
        write_results_to_figure (7, 6, "n=30k-1 (k=1,2,3...); n from 2 to ", file_shape_7, False)
        write_results_to_figure (7, 6, "n=30k-1 (k=1,2,3...); n from 2 to ", file_shape_7 + "3d", True)
    if 'c8' in cases_to_check:
        write_results_to_figure (8, 7, "n=30k-+1 (k=1,2,3...); n from 2 to ", file_shape_8, False)
        write_results_to_figure (8, 7, "n=30k-+1 (k=1,2,3...); n from 2 to ", file_shape_8 + "3d", True)
    if 'c9' in cases_to_check:
        write_results_to_figure (9, 8, "n=sum of dec digits(k) (k=1,2,3...); n from 2 to ", file_shape_9, False)
        write_results_to_figure (9, 8, "n=sum of dec digits(k) (k=1,2,3...); n from 2 to ", file_shape_9 + "3d", True)
    if 'c10' in cases_to_check:
        write_results_to_figure (10, 9, "n=1 or 2", file_shape_10, False)
        write_results_to_figure (10, 9, "n=1 or 2", file_shape_10 + "3d", True)
    if 'c11' in cases_to_check:
        write_results_to_figure (11, 10, "n = sin(10k) ; k from 1 to ", file_shape_11, False)
        write_results_to_figure (11, 10, "n = sin(10k) ; k from 1 to ", file_shape_11 + "3d", True)
    if 'c12' in cases_to_check:
        write_results_to_figure (12, 11, "n = random integer between 2 and 9", file_shape_12, False)
        write_results_to_figure (12, 11, "n = random integer between 2 and 9", file_shape_12 + "3d", True)

def set_file_output_filename (file_start, add_something, file_end):
    if add_something:
        return (file_start + file_end)
    else:
        return (file_start)

def write_results_to_figure (fig_id, data_id, title_start, file_output, if_3d):
    global datax, datay, dataz, colors

    title = title_start + str(num_current[data_id]) + " iter=" + str(k) 

    if if_3d:
        fig = plt.figure(fig_id)
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(datax[data_id], datay[data_id], dataz[data_id], c=colors[data_id], marker='o')

    else:
        area = np.pi
        fig = plt.figure(fig_id)
        plt.clf()
        plt.scatter(datax[data_id], datay[data_id], s=area, c=colors[data_id], alpha=0.2)
        fig.suptitle(title, fontsize=10)

    file_output += file_output_extension
    plt.savefig(file_output)
    plt.close(fig)

def save_current_results (file_output_pickle):
    global k_current, new_x, new_y, new_y, delta_x, delta_y, delta_z, num_current, datax, datay, dataz, colors, lifetime, is_previous_prime, sign, stats_primes, stats_nonprimes, stats_iterations
    with open(file_output_pickle, 'wb') as f:
        pickle.dump([k_current, new_x, new_y, new_z, delta_x, delta_y, delta_z, num_current, datax, datay, dataz, colors, lifetime, is_previous_prime, sign, stats_primes, stats_nonprimes, stats_iterations], f)

def restore_previous_results (file_output_pickle):
    global k_current, new_x, new_y, new_y, delta_x, delta_y, delta_z, num_current, datax, datay, dataz, colors, lifetime, is_previous_prime, sign, stats_primes, stats_nonprimes, stats_iterations
    if os.path.exists(file_output_pickle):
        with open(file_output_pickle, 'rb') as f:
           k_current, new_x, new_y, new_z, delta_x, delta_y, delta_z, num_current, datax, datay, dataz, colors, lifetime, is_previous_prime, sign, stats_primes, stats_nonprimes, stats_iterations = pickle.load(f)

def run_test_case (tcid, s):
    num_current[tcid] = num

    (delta_x[tcid], delta_y[tcid], delta_z[tcid], sign[tcid], is_previous_prime[tcid], turn, stats_primes[tcid], stats_nonprimes[tcid], stats_iterations[tcid]) = s.next_iteration (p, num, is_previous_prime[tcid], delta_x[tcid], delta_y[tcid], delta_z[tcid], sign[tcid], stats_primes[tcid], stats_nonprimes[tcid], stats_iterations[tcid])
        
    new_x[tcid]+= delta_x[tcid]
    new_y[tcid]+= delta_y[tcid]
    new_z[tcid]+= delta_z[tcid]

    update_points (tcid, new_x[tcid], new_y[tcid], new_z[tcid], turn, enable_optimized_points_save, enable_points_lifetime)

def update_points (tcid, x, y, z, turn, is_optimized, is_lifetime):
    global datax, datay, lifetime, colors
    global lifetime_start
    found = False

    # if points have lifetime - update it and remove all expiring points
    if is_lifetime:
        i = 0
        indices_to_be_removed = []
        for l in lifetime[tcid]:
            if int(l) > 1:
                lifetime[tcid][i] -= 1
            # lifetime expired - mark point for removal
            else:
                indices_to_be_removed.append(i)
            i += 1

        # remove marked points
        for j in indices_to_be_removed:
            del datax[tcid][j]
            del datay[tcid][j]
            del dataz[tcid][j]
            del lifetime[tcid][j]
            del colors[tcid][j]

    # check if point is already on the list
    if is_optimized:
        k = 0
        old_datax = datax[tcid]
        old_datay = datay[tcid]
        old_dataz = dataz[tcid]

        for old_x in old_datax:
            if old_x == x and old_datay[k] == y and old_dataz[k] == z:
                found = True
                # renew existing point lifetime
                if is_lifetime:
                    lifetime[tcid][k] = lifetime_start
                break
            k += 1

    # remember point if not found yet
    if not found:
        datax[tcid].append(x)
        datay[tcid].append(y)
        dataz[tcid].append(z)
        if is_lifetime:
            lifetime[tcid].append(lifetime_start)
        if turn:
            colors[tcid].append(color_turn)
        else:
            colors[tcid].append(color_no_turn)

    # internal checks
    if is_lifetime: 
        if len(lifetime[tcid]) != len(datax[tcid]):
            raise ("WrongLengthsOfStructures")
        for l in lifetime[tcid]:
            if int(l) < 1:
                raise ("ExpiredPointOnTheList")
    if len(datax[tcid]) != len(datay[tcid]):
        raise ("WrongLengthsOfStructures")

def write_stats_to_file ():
    f = open(file_output_stats, "a+")

    for i in range (min_case, max_case):
        case = "c" + str(i)
        if case in cases_to_check:
            perc_primes = int(stats_primes[i-1]*100/stats_iterations[i-1] + 0.5)
            perc_nonprimes = int(stats_nonprimes[i-1]*100/stats_iterations[i-1] + 0.5)
            (diff_x, diff_y, diff_z) = get_max_diff (i-1)
            fill_2d = int(get_points (i-1) * 100 / (diff_x * diff_y))
            fill_3d = int(get_points (i-1) * 100 / (diff_x * diff_y * diff_z))
            print ("  Figure", i, "statistics:")
            print ("    * Primes         :", stats_primes[i-1], "(", perc_primes, "% )")
            print ("    * Non-primes     :", stats_nonprimes[i-1], "(", perc_nonprimes, "% )")
            print ("    * Diff (x,y,z)   :", "(", diff_x, ",", diff_y, ",", diff_z, ")")
            print ("    * 2D Figure fill :", fill_2d, "%")
            print ("    * 3D Figure fill :", fill_3d, "%")
            f.write (case + "," + str(stats_iterations[i-1]) + "," + str(stats_primes[i-1]) + "," + str(perc_primes) + "," + str(stats_nonprimes[i-1]) + "," + str(perc_nonprimes) + "\n")
    f.close ()

#############################################################
# Main
#############################################################

print ("Initialize objects...")
p = primes.Primes(caching_primality_results)
s = shapes.Shape()
dp = dataprocessing.DataProcessing()
print ("DONE")
print ("Loading helper sets...")
p.init_set(file_input_primes, True)
p.init_set(file_input_nonprimes, False)
print ("DONE")
print ("Sorting primes...")
p.sort_primes_set()
print ("DONE")
if continue_previous_calculations:
    print ("Restoring previous results...")
    restore_previous_results (file_output_pickle)
    if k_current > 0:
        min_num = k_current
        k = k_current
        print ("Resuming calculations at", min_num)
    print ("DONE")

# new calculations
for k in range (min_num, max_num):

    # case 1: subsequent odd numbers
    if 'c1' in cases_to_check:
        num = k*2 + 1
        run_test_case (0, s)

    # case 2: 6k+1
    if 'c2' in cases_to_check:
        num = k*2*3 + 1
        run_test_case (1, s)

    # case 3: 6k-1
    if 'c3' in cases_to_check:
        num = k*2*3 - 1
        run_test_case (2, s)

    # case 4: 6k+-1
    if 'c4' in cases_to_check:
        num = k*2*3 - 1*sign[3]
        run_test_case (3, s)

    # case 5: k
    if 'c5' in cases_to_check:
        num = k
        run_test_case (4, s)

    # case 6: 30k+1
    if 'c6' in cases_to_check:
        num = k*2*3*5 + 1
        run_test_case (5, s)

    # case 7: 30k-1
    if 'c7' in cases_to_check:
        num = k*2*3*5 - 1
        run_test_case (6, s)

    # case 8: 30k+-1
    if 'c8' in cases_to_check:
        num = k*2*3*5 - 1*sign[7]
        run_test_case (7, s)

    # case 9: sum of decimal digits is prime or not
    if 'c9' in cases_to_check:
        num = dp.get_sum_of_decimal_digits (k)
        run_test_case (8, s)

    # case 10: 1 and 2 only
    if 'c10' in cases_to_check:
        num = dp.get_next_num_from_set (num)
        run_test_case (9, s)

    # case 11: integer(10sin(k))
    if 'c11' in cases_to_check:
        num = int(10*math.sin(k))
        run_test_case (10, s)

    # case 12: random integer from 2,3,4,5,6,7,8,9 (4 primes, 4 non-primes)
    if 'c12' in cases_to_check:
        num = randint(2,9)
        run_test_case (11, s)

    # checkpoint - partial results
    if (k - min_num) % checkpoint_value == 0:

        perc_completed = str(int(k * 100 / max_num))
        print ("Checkpoint", k, "of total", max_num, "(" + perc_completed + "% completed)")

        write_stats_to_file ()
        
        # save results collected so far
        write_results_to_figures (figures_save_partial_results, perc_completed, k)
        k_current = k
        save_current_results(file_output_pickle)


# final results
perc_completed = str(int(k * 100 / max_num))
write_results_to_figures (figures_save_partial_results, perc_completed, k)
write_stats_to_file ()
k_current = max_num
save_current_results(file_output_pickle)

