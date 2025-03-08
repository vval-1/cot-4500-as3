from main.assignment_3 import euler_method, runge_kutta_method

class Testing:
    def __init__(self):
        pass

    def run_tests(self):
        self.test_euler_method()
        self.test_runge_kutta_method()  
    

    def test_euler_method(self):
        def f(t0, y0):
            return t0 - y0**2
    
        t_start, y_start = 0, 1  
        t_end, num_steps = 2, 10 
        step_size = (t_end - t_start) / num_steps 

        result = euler_method(f, t_start, y_start, step_size, num_steps)
        print()
        print("Euler's Method Result -", result)
        print()

    def test_runge_kutta_method(self):
        def f(t0, y0):
            return t0 - y0**2
        
        t_start, y_start = 0, 1  
        t_end, num_steps = 2, 10 

        step_size = (t_end - t_start) / num_steps 
        result = runge_kutta_method(f, t_start, y_start, step_size, num_steps)
        print("Runge Kutta Method Result -",result) 
        print()

if __name__ == "__main__":
    Testing().run_tests()