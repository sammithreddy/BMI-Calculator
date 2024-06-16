import tkinter as tk
frame=tk.Tk()
frame.geometry("300x400")
frame.title("BMI Finder")
l=tk.Label(text="Enter height(In CM) and weight(In KG) respectively")
handw=tk.Text(frame,height=1,width=15,bg="light yellow")
bmi=tk.Text(frame,height=3,width=24,bg="light cyan")
b=tk.Button(frame,height=2,text="Submit",command=lambda: findBMI())
l.pack()
handw.pack()
bmi.pack()
b.pack()
def findBMI():
    bmi.delete("1.0","end")
    both=handw.get('1.0','end')
    h,w=map(int,both.split(" "))
    h=float(h/100)
    total=w/(h*h)
    if total>=25:
        bmi.insert(tk.END ,"BMI is {} and the person is Overweight".format(round(total,2)))
    elif total<18.5:
        bmi.insert(tk.END ,"BMI is {} and the person is Underweight".format(round(total,2)))
    else:
        bmi.insert(tk.END ,"BMI is {} and the person is Healthy".format(round(total,2)))
frame.mainloop()