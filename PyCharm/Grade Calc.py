#GPA Calculation
print("========================")
print("    GPA Calculation    ")
print("========================")

def get_grade_and_gpa(marks):
    if marks>=80:
        return "A+",5.00
    elif marks>=70:
        return "A",4.00
    elif marks>=60:
        return "A-",3.50
    elif marks>=50:
        return "B",3.00
    elif marks>=40:
        return "C",2.00
    elif marks>=33:
        return "D",1.00
    else:
        return "F",0.00

def main():

    try:
        main_sub_count=int(input("\nPlease insert your main subject: "))
        main_subjects=[]
        total_main_gpa=0.0
        has_failed=False

        for i in range(1, main_sub_count + 1):
            sub_name=input("\nPlease insert your subject: ").strip()
            while True:
               try:
                   marks=float(input("Please insert your marks: "))
                   if 0<=marks<=100:
                       break
                   else:
                    print("Marks must be between 0 and 100")
               except ValueError:
                   print("Please insert correct marks")

            grade, gpa = get_grade_and_gpa(marks)
            if grade=="F":
                has_failed=True
            total_main_gpa += gpa
            main_subjects.append({"subjects": sub_name, "marks": marks, "grade": grade, "gpa": gpa, })


            print("\n"+"-"*60)
            opt_sub_name=input("4th Subject : ").strip()

            while True:
               try:
                  opt_marks=float(input("Please 4th Subject marks: "))
                  if 0<=opt_marks<=100:
                      break
                  else:
                      print("Marks must be between 0 and 100")
               except ValueError:
                   print("Please insert correct marks")
            opt_grade, opt_gpa = get_grade_and_gpa(opt_marks)

            if opt_gpa>2.0:
                extra_gpa=opt_gpa-2.0
            else:
                extra_gpa=0.0

            print("\n"+"="*60)
            print("Summary")
            print("="*60)
            print(f"{'sub':<18} |{'number':<8} |{'Grade':<6} |{'gpa':<6}")
            print("-"*60)

            for res in main_subjects:
                print(
                    res["subjects"],
                    "| Marks:",
                    res["marks"],
                    "| Grade:",
                    res["grade"],
                    "| GPA:",
                    res["gpa"],
                )
            print(f"{opt_sub_name + '(4th)':<18} | {opt_marks:<8.1f} | {opt_grade:<6} | {opt_gpa:<6.2f}")
            print("-"*60)

            if has_failed or opt_grade=="F":
                final_gpa=0.0
                final_grade="F"
            else:
                 calculated_gpa=(total_main_gpa+extra_gpa)
                 final_gpa=min(5.00, calculated_gpa)
                 if final_gpa==5.00:
                     final_grade= "A+"
                 elif final_gpa>=4.00:
                     final_grade = "A"
                 elif final_gpa>=3.50:
                     final_grade = "A-"
                 elif final_gpa>=3.00:
                     final_grade = "B"
                 elif final_gpa>=2.00:
                     final_grade = "C"
                 elif final_gpa>=1.00:
                     final_grade = "D"
                 else:
                     final_grade = "F"
            print(f"4th Subject bonus : +{extra_gpa:.2f}")
            print(f"Final GPA: {final_gpa:.2f}")
            print(f"Final grade: {final_grade}")
            print("-"*60)
    except ValueError:
        print("\nerror: Give correct info")
if __name__=="__main__":
    main()
