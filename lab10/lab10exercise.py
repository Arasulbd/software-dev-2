"""
Students full name: Aminur Rasul
April 25, loop
"""
print("\n------LAb 10 Exercise ------")

colors = ['red','orange','olive','magenta','green']
color_check=input("Enter a color:").strip().lower()

for colors in colors:
    if color_check in colors:
        print(f"{color_check} colors is in the list")
        break
    else:
         print(f"{color_check} colors IS NOT in the list")
        