from q3_process_payroll import process_payroll 

def test_process_payroll():
    hours1 = [ [ "Tom", 20.00, 10, 12, 7, 9, 11 ],
               [ "Leslie", 18.50, 10, 10, 10, 10, 9 ],
               [ "Tobias", 16.75, 6, 12, 6.5, 11, 6 ] ]
    assert(process_payroll(hours1) == [ [ "Tom", 980.0], [ "Leslie", 906.5 ], [ "Tobias", 695.125] ])
    hours2 = [ [ "Kushal", 24.0, 8, 7.5, 9.5 ],
               [ "Yumin", 23.5, 9.5, 9.5, 9.5 ],
               [ "Tianxin", 25.0, 6, 5.5, 6.5 ] ]
    assert(process_payroll(hours2) == [ [ "Kushal", 600.0 ], [ "Yumin", 669.75 ], [ "Tianxin", 450.0 ] ])
    hours3 = [ [ "Steven", 12.5, 7] ]
    assert(process_payroll(hours3) == [ [ "Steven", 87.5 ] ])
    
