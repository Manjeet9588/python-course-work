'''Calculate simple interest'''
principle = int(input("Enter your principle amount for interest : "))
rate = float(input("Enter rate of interest : "))
time = float(input("Enter time interval for interest : "))
simple_interest = (principle * rate * time)/100
print(f"The simple interest on {principle} amount at {rate} rate for {time} time is {simple_interest}")