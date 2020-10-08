def func(x):
	return x + 8

def test_positivo():
	assert func(3) == 11
    
def test_negativo():
	assert func(-15) == -7
    
 def test_zero():
	assert func(0) == 8