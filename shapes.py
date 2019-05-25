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

import sys
sys.path.insert(0, '..\\primes\\')
import primes

class Shape:

    def next_delta_xy (self, delta_x, delta_y, turn):
        if turn:
            if delta_x == 1 and delta_y == 0:
                delta_x = 0
                delta_y = 1
                return (delta_x, delta_y)
            if delta_x == 0 and delta_y == 1:
                delta_x = -1
                delta_y = 0
                return (delta_x, delta_y)
            if delta_x == -1 and delta_y == 0:
                delta_x = 0
                delta_y = -1
                return (delta_x, delta_y)
            if delta_x == 0 and delta_y == -1:
                delta_x = 1
                delta_y = 0
                return (delta_x, delta_y)
        return (delta_x, delta_y)

    def next_delta_z (self, delta_z, is_previous_prime, is_current_prime):
        if not is_previous_prime and is_current_prime:
            if delta_z == 0:
                delta_z = 1
            elif delta_z == 1:
                delta_z = -1
            else:
                delta_z = 0
        return delta_z

    def next_turn (self, p, num, is_previous_prime, stats_primes, stats_nonprimes):
        turn = False
        is_current_prime = False
        if p.is_prime(num):
            is_current_prime = True
            stats_primes += 1
            if not is_previous_prime:
                turn = True
                is_previous_prime = True
        if not p.is_prime(num):
            stats_nonprimes += 1
            if is_previous_prime:
                turn = True
                is_previous_prime = False
        return (turn, is_previous_prime, is_current_prime, stats_primes, stats_nonprimes)

    def next_sign (self, sign):
        if sign == 1:
            return -1
        else:
            return 1

    def next_iteration (self, p, num, is_previous_prime, delta_x, delta_y, delta_z, sign, stats_primes, stats_nonprimes, stats_iterations):
        turn = False
        (turn, is_previous_prime, is_current_prime, stats_primes, stats_nonprimes) = self.next_turn (p, num, is_previous_prime, stats_primes, stats_nonprimes)
        sign = self.next_sign (sign)
        (delta_x, delta_y) = self.next_delta_xy (delta_x, delta_y, turn)
        delta_z = self.next_delta_z (delta_z, is_previous_prime, is_current_prime)
        stats_iterations += 1
        return (delta_x, delta_y, delta_z, sign, is_previous_prime, turn, stats_primes, stats_nonprimes, stats_iterations)

    def get_sum_of_decimal_digits (self, num):
        base = 10
        sum_of_digits = 0
        while num:
            sum_of_digits += num % base
            num //= base
        return sum_of_digits

    def get_next_num_from_set (self, num):
        if num == 2:
            return 1
        else:
            return 2
