v=float(input("Enter voltage (V): "))
r=float(input("Enter resistance (R) : "))
i=v/r
if i<0.5:
    print("Low current")
elif 0.5<=i<=2:
    print("Normal current")
elif i>2:
    print("High current")   