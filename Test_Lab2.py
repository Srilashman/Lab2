import Lab2

def test_min_max():
    input_arr = [-9, 0, 1, 10, 7]

    assert(Lab2.calc_min_max_temperature(input_arr) == [-9, 10])

def test_average():
    input_arr = [-9, 0, 1, 10, 8]

    assert(Lab2.calc_average_temperature(input_arr) == 2)

def test_median():
    input_arr = [-9, 0, 1, 10, 7]
    input_arr = Lab2.sort_temperature(input_arr)
    assert(Lab2.calc_median_temperature(input_arr) == 1) # for odd length arr

    input_arr = [-9, 0, 1, 10, 7, -7]
    input_arr = Lab2.sort_temperature(input_arr)
    assert(Lab2.calc_median_temperature(input_arr) == 0.5) # for even length arr
