import jlab as jl

def test_resistor_functions():
    assert np.isclose(jl.parallel_resistors([100, 200, 300]), 54.54545454545454)
    assert np.isclose(jl.series_resistors([100, 200, 300]), 600)

def test_capacitor_functions():
    assert np.isclose(jl.parallel_capacitors([1e-6, 2e-6, 3e-6]), 6e-6)
    assert np.isclose(jl.series_capacitors([1e-6, 2e-6, 3e-6]), 5.454545454545454e-07)

def test_voltage_divider():
    assert np.isclose(jl.voltage_divider(10, [1000, 1000]), 5.0)
    assert np.isclose(jl.voltage_divider(12, [2000, 1000]), 4.0)

if __name__ == "__main__":
    test_resistor_functions()
    test_capacitor_functions()
    test_voltage_divider()
    print("All tests passed.")