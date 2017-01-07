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

import primes

def next_delta (delta_x, delta_y, turn):
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

def next_turn (p, num, is_previous_prime):
    turn = False
    if p.is_prime(num) and not is_previous_prime:
        turn = True
        is_previous_prime = True
    if not p.is_prime(num) and is_previous_prime:
        turn = True
        is_previous_prime = False
    return (turn, is_previous_prime)

def next_sign (sign):
    if sign == 1:
        return -1
    else:
        return 1

def next_iteration (p, num, is_previous_prime, delta_x, delta_y, sign):
    turn = False
    (turn, is_previous_prime) = next_turn (p, num, is_previous_prime)
    sign = next_sign (sign)
    (delta_x, delta_y) = next_delta (delta_x, delta_y, turn)
    return (delta_x, delta_y, sign, is_previous_prime, turn)
