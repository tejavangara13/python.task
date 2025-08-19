total_seconds=int(input("Enter total seconds:"))
hours=total_seconds//3600
remaining=total_seconds%3600
minutes=remaining//60
seconds=remaining%60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

p1=50
q1=2
p2=70
q2=2
total_cost=(p1*q1)+(p2*q2)
tax=total_cost*0.18
bill=total_cost+tax
print(bill)

