#
# Copyright (c) 2017, Marcin Barylski
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

import matplotlib.pyplot as plt
import primes
import shapes
import os
import numpy as np
import pickle

#############################################################
# Settings - configuration
#############################################################

# Minimal and maximum number - range of iterations
min_num = 1
max_num = 200000

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
cases_to_check = {'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9'}
#cases_to_check = {'c6', 'c7', 'c8', 'c9'}

min_case = 1
max_case = 10

# Helper files
#   o file_input_primes - contains prime numbers
#   o file_input_nonprimes - contains composite numbers
file_input_primes = 't_prime_numbers.txt'
file_input_nonprimes = 't_nonprime_numbers.txt'

# Save figures with partial results
figures_save_partial_results = True

# Colors for points
color_no_turn = 0
color_turn = 0

#############################################################
# Settings - output directory and files
#############################################################

directory = str(max_num)
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
file_output_extension = ".png"
file_output_pickle = directory + "/objs_shape.pickle"
file_output_stats = directory + "/objs_stats.csv"

#############################################################
# Results of calculations
#############################################################

new_x =       [0, 0, 0, 0, 0, 0, 0, 0, 0]
new_y =       [0, 0, 0, 0, 0, 0, 0, 0, 0]
delta_x =     [1, 1, 1, 1, 1, 1, 1, 1, 1]
delta_y =     [0, 0, 0, 0, 0, 0, 0, 0, 0]
num_current = [0, 0, 0, 0, 0, 0, 0, 0, 0]

datax =       [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
datay =       [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
colors =      [[0], [0], [0], [0], [0], [0], [0], [0], [0]]

is_previous_prime = [False, False, False, False, False, False, False, False, False]
sign =        [1, 1, 1, 1, 1, 1, 1, 1, 1]
k_current = 0

stats_primes =     [0, 0, 0, 0, 0, 0, 0, 0, 0]
stats_nonprimes =  [0, 0, 0, 0, 0, 0, 0, 0, 0]
stats_iterations = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#############################################################
# Presentation
#############################################################

def write_results_to_figures(save_partial_results, perc_completed):

    file_shape_1 = set_file_output_filename (file_output_shape_1, save_partial_results, "_" + str(perc_completed))
    file_shape_2 = set_file_output_filename (file_output_shape_2, save_partial_results, "_" + str(perc_completed))
    file_shape_3 = set_file_output_filename (file_output_shape_3, save_partial_results, "_" + str(perc_completed))
    file_shape_4 = set_file_output_filename (file_output_shape_4, save_partial_results, "_" + str(perc_completed))
    file_shape_5 = set_file_output_filename (file_output_shape_5, save_partial_results, "_" + str(perc_completed))
    file_shape_6 = set_file_output_filename (file_output_shape_6, save_partial_results, "_" + str(perc_completed))
    file_shape_7 = set_file_output_filename (file_output_shape_7, save_partial_results, "_" + str(perc_completed))
    file_shape_8 = set_file_output_filename (file_output_shape_8, save_partial_results, "_" + str(perc_completed))
    file_shape_9 = set_file_output_filename (file_output_shape_9, save_partial_results, "_" + str(perc_completed))

    if 'c1' in cases_to_check:
        write_results_to_figure (1, 0, "n=2k+1 (k=1,2,3...); n from 3 to ", file_shape_1)
    if 'c2' in cases_to_check:
        write_results_to_figure (2, 1, "n=6k+1 (k=1,2,3...); n from 7 to ", file_shape_2)
    if 'c3' in cases_to_check:
        write_results_to_figure (3, 2, "n=6k-1 (k=1,2,3...); n from 5 to ", file_shape_3)
    if 'c4' in cases_to_check:
        write_results_to_figure (4, 3, "n=6k-+1 (k=1,2,3...); n from 5 to ", file_shape_4)
    if 'c5' in cases_to_check:
        write_results_to_figure (5, 4, "n=1,2,3... ; n from 1 to ", file_shape_5)
    if 'c6' in cases_to_check:
        write_results_to_figure (6, 5, "n=30k+1 (k=1,2,3...); n from 4 to ", file_shape_6)
    if 'c7' in cases_to_check:
        write_results_to_figure (7, 6, "n=30k-1 (k=1,2,3...); n from 2 to ", file_shape_7)
    if 'c8' in cases_to_check:
        write_results_to_figure (8, 7, "n=30k-+1 (k=1,2,3...); n from 2 to ", file_shape_8)
    if 'c9' in cases_to_check:
        write_results_to_figure (9, 8, "n=sum of dec digits(k) (k=1,2,3...); n from 2 to ", file_shape_9)

def set_file_output_filename (file_start, add_something, file_end):
    if add_something:
        return (file_start + file_end)
    else:
        return (file_start)

def write_results_to_figure (fig_id, data_id, title_start, file_output):
    area = np.pi
    fig = plt.figure(fig_id)
    plt.scatter(datax[data_id], datay[data_id], s=area, c=colors[data_id], alpha=0.2)
    title = title_start + str(num_current[data_id])
    fig.suptitle(title, fontsize=10)
    file_output += file_output_extension
    plt.savefig(file_output)

def save_current_results (file_output_pickle):
    global k_current, new_x, new_y, delta_x, delta_y, num_current, datax, datay, colors, is_previous_prime, sign, stats_primes, stats_nonprimes, stats_iterations
    with open(file_output_pickle, 'wb') as f:
        pickle.dump([k_current, new_x, new_y, delta_x, delta_y, num_current, datax, datay, colors, is_previous_prime, sign, stats_primes, stats_nonprimes, stats_iterations], f)

def restore_previous_results (file_output_pickle):
    global k_current, new_x, new_y, delta_x, delta_y, num_current, datax, datay, colors, is_previous_prime, sign, stats_primes, stats_nonprimes, stats_iterations
    if os.path.exists(file_output_pickle):
        with open(file_output_pickle, 'rb') as f:
           k_current, new_x, new_y, delta_x, delta_y, num_current, datax, datay, colors, is_previous_prime, sign, stats_primes, stats_nonprimes, stats_iterations = pickle.load(f)

def run_test_case (tcid):
    num_current[tcid] = num

    (delta_x[tcid], delta_y[tcid], sign[tcid], is_previous_prime[tcid], turn, stats_primes[tcid], stats_nonprimes[tcid], stats_iterations[tcid]) = shapes.next_iteration (p, num, is_previous_prime[tcid], delta_x[tcid], delta_y[tcid], sign[tcid], stats_primes[tcid], stats_nonprimes[tcid], stats_iterations[tcid])
        
    new_x[tcid]+= delta_x[tcid]
    new_y[tcid]+= delta_y[tcid]

    update_points_optimized (tcid, new_x[tcid], new_y[tcid], turn)

def update_points (tcid, x, y, turn):
    datax[tcid].append(x)
    datay[tcid].append(y)
    if turn:
        colors[tcid].append(color_turn)
    else:
        colors[tcid].append(color_no_turn)

def update_points_optimized (tcid, x, y, turn): 
    old_datax = datax[tcid]
    old_datay = datay[tcid]
    i = 0
    found = False
    for old_x in old_datax:
        if old_x == x and old_datay[i] == y:
            found = True
            break
        i += 1

    if not found:
        datax[tcid].append(x)
        datay[tcid].append(y)
        if turn:
            colors[tcid].append(color_turn)
        else:
            colors[tcid].append(color_no_turn)

def write_stats_to_file ():
    f = open(file_output_stats, "a+")

    for i in range (min_case, max_case):
        case = "c" + str(i)
        if case in cases_to_check:
            perc_primes = int(stats_primes[i-1]*100/stats_iterations[i-1] + 0.5)
            perc_nonprimes = int(stats_nonprimes[i-1]*100/stats_iterations[i-1] + 0.5)
            print ("  Figure", i, "statistics:")
            print ("    * Primes     :", stats_primes[i-1], "(", perc_primes, "%)")
            print ("    * Non-primes :", stats_nonprimes[i-1], "(", perc_nonprimes, "%)")
            f.write (case + "," + str(stats_iterations[i-1]) + "," + str(stats_primes[i-1]) + "," + str(perc_primes) + "," + str(stats_nonprimes[i-1]) + "," + str(perc_nonprimes) + "\n")
    f.close ()

#############################################################
# Main
#############################################################

print ("Initialize objects...")
p = primes.Primes(caching_primality_results)
print ("DONE")
print ("Loading helper sets...")
p.init_set(file_input_primes, True)
p.init_set(file_input_nonprimes, False)
print ("DONE")
print ("Sorting primes...")
p.sort_prime_set()
print ("DONE")
print ("Restoring previous results...")
restore_previous_results (file_output_pickle)
if k_current > 0:
    min_num = k_current
    print ("Resuming calculations at", min_num)
print ("DONE")

# new calculations
for k in range (min_num, max_num):

    # case 1: subsequent odd numbers
    if 'c1' in cases_to_check:
        num = k*2 + 1
        run_test_case (0)

    # case 2:
    if 'c2' in cases_to_check:
        num = k*2*3 + 1
        run_test_case (1)

    # case 3:
    if 'c3' in cases_to_check:
        num = k*2*3 - 1
        run_test_case (2)

    # case 4:
    if 'c4' in cases_to_check:
        num = k*2*3 - 1*sign[3]
        run_test_case (3)

    # case 5:
    if 'c5' in cases_to_check:
        num = k
        run_test_case (4)

    # case 6:
    if 'c6' in cases_to_check:
        num = k*2*3*5 + 1
        run_test_case (5)

    # case 7:
    if 'c7' in cases_to_check:
        num = k*2*3*5 - 1
        run_test_case (6)

    # case 8:
    if 'c8' in cases_to_check:
        num = k*2*3*5 - 1*sign[7]
        run_test_case (7)

    # case 9: sum of decimal digits is prime or not
    if 'c9' in cases_to_check:
        num = shapes.get_sum_of_decimal_digits (k)
        run_test_case (8)

    # checkpoint - partial results
    if (k - min_num) % checkpoint_value == 0:

        perc_completed = str(int(k * 100 / max_num))
        print ("Checkpoint", k, "of total", max_num, "(" + perc_completed + "% completed)")

        write_stats_to_file ()
        
        # save results collected so far
        write_results_to_figures (figures_save_partial_results, perc_completed)
        k_current = k
        save_current_results(file_output_pickle)


# final results
write_results_to_figures (figures_save_partial_results, perc_completed)
write_stats_to_file ()
k_current = max_num
save_current_results(file_output_pickle)

