#!/usr/bin/env python

from cyaron import * # 引入CYaRon的库

for i in range(1,11):
    io = IO(file_prefix="problem", data_id=i) # test3.in, test3.out

    a = randint(1,1000)
    b = "abcdefghijklmnopqrstuvwxyz"
    _max = ati([1E3])
    _in = [ choice(b) for i in range(0,a)]
    io.input_write(''.join(_in))
    io.output_gen("../std")
