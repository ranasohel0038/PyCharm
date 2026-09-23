# ======================
# GPA CALCULATOR PROGRAM
# ======================


def get_grade_and_gpa(marks):
    if marks >= 80:
        return "A+", 5.00
    elif marks >= 70:
        return "A", 4.00
    elif marks >= 60:
        return "A-", 3.50
    elif marks >= 50:
        return "B", 3.00
    elif marks >= 40:
        return "C", 2.00
    elif marks >= 33:
        return "D", 1.00
    else:
        return "F", 0.00


def get_letter_grade(gpa):
    if gpa == 5.00:
        return "A+"
    elif gpa >= 4.00:
        return "A"
    elif gpa >= 3.50:
        return "A-"
    elif gpa >= 3.00:
        return "B"
    elif gpa >= 2.00:
        return "C"
    elif gpa >= 1.00:
        return "D"
    else:
        return "F"


def main():
    while True:
        print("\n" + "=" * 54)
        print("            MY GPA CALCULATOR             ")
        print("=" * 54)

        try:
            main_sub_count = int(
                input("\nPlease Enter your Total Main Subject: ")
            )

            main_subjects = []
            total_main_gpa = 0.0
            failed_subjects = []  # For Failed Sub List

            # 1. Main subjects input
            for i in range(1, main_sub_count + 1):
                sub_name = input(f"\n{i} no. Subject Name: ").strip()

                while True:
                    try:
                        marks = float(
                            input(f"'{sub_name}' Obtained Marks (0-100): ")
                        )
                        if 0 <= marks <= 100:
                            break
                        else:
                            print("Marks must be between 0 and 100!")
                    except ValueError:
                        print("Please insert correct marks.")

                grade, gpa = get_grade_and_gpa(marks)

                if grade == "F":
                    failed_subjects.append(sub_name)

                total_main_gpa += gpa
                main_subjects.append(
                    {
                        "subject": sub_name,
                        "marks": marks,
                        "grade": grade,
                        "gpa": gpa,
                    }
                )

            # Golden A+ Knowing Flag (All Sub must be A+)
            is_golden_aplus = (
                len(failed_subjects) == 0
                and all(res["grade"] == "A+" for res in main_subjects)
            )

            # 2. Main subjects calculation
            if failed_subjects:
                main_final_gpa = 0.00
                fail_list_str = ", ".join(failed_subjects)
                main_final_grade = f"F (Failed in {len(failed_subjects)} subject/s: {fail_list_str})"
            else:
                main_final_gpa = total_main_gpa / main_sub_count
                base_grade = get_letter_grade(main_final_gpa)
                if is_golden_aplus:
                    main_final_grade = "Golden A+"
                else:
                    main_final_grade = base_grade

            # 3. Output main subjects result
            print("\n" + "=" * 60)
            print("                 MAIN SUBJECT RESULT                 ")
            print("=" * 60)
            for res in main_subjects:
                print(
                    f"{res['subject']} | Marks: {res['marks']} | Grade: {res['grade']} | GPA: {res['gpa']}"
                )
            print("-" * 60)
            print(f"Main Subjects Total GPA: {main_final_gpa:.2f}")
            print(f"Main Subjects Grade: {main_final_grade}")
            print("=" * 60)

            # 4. 4th subject option
            choice = (
                input("\nDo you have 4th Subject? (y/n): ").strip().lower()
            )

            if choice in ["yes", "y"]:
                opt_sub_name = input("\nEnter 4th Subject Name: ").strip()

                while True:
                    try:
                        opt_marks = float(
                            input(f"'{opt_sub_name}' Obtained Marks (0-100): ")
                        )
                        if 0 <= opt_marks <= 100:
                            break
                        else:
                            print("Marks must be between 0 and 100!")
                    except ValueError:
                        print("Please insert correct marks.")

                opt_grade, opt_gpa = get_grade_and_gpa(opt_marks)

                if opt_gpa > 2.0:
                    extra_gpa = opt_gpa - 2.0
                else:
                    extra_gpa = 0.0

                print("\n" + "=" * 60)
                print(
                    "                 FINAL RESULT WITH 4TH SUBJECT                 "
                )
                print("=" * 60)
                print(
                    f"{opt_sub_name} (4th Subject) | Marks: {opt_marks} | Grade: {opt_grade} | GPA: {opt_gpa}"
                )
                print("-" * 60)

                if failed_subjects or opt_grade == "F":
                    opt_final_gpa = 0.00
                    # Failed count with 4th subject
                    total_failed = list(failed_subjects)
                    if opt_grade == "F":
                        total_failed.append(f"{opt_sub_name} (4th Subject)")

                    fail_list_str = ", ".join(total_failed)
                    opt_final_grade = f"F (Failed in {len(total_failed)} subject/s: {fail_list_str})"
                else:
                    calculated_gpa = (
                        total_main_gpa + extra_gpa
                    ) / main_sub_count
                    opt_final_gpa = min(5.00, calculated_gpa)

                    base_grade = get_letter_grade(opt_final_gpa)
                    if is_golden_aplus:
                        opt_final_grade = "Golden A+"
                    else:
                        opt_final_grade = base_grade

                print(f"4th Subject Bonus Point: +{extra_gpa:.2f}")
                print(f"Final GPA: {opt_final_gpa:.2f}")
                print(f"Final Grade: {opt_final_grade}")
                print("=" * 60)

            else:
                print("\n" + "=" * 60)
                print(
                    "             FINAL RESULT WITHOUT 4TH SUBJECT             "
                )
                print("=" * 60)
                print(f"Final GPA: {main_final_gpa:.2f}")
                print(f"Final Grade: {main_final_grade}")
                print("=" * 60)

        except ValueError:
            print("\nError: Please enter valid numbers.")

        # >>> For again counting <<<
        again = (
            input("\nDo You Want Calculate Again? (y/n): ").strip().lower()
        )
        if again not in ["yes", "y"]:
            print("\nThanks for using me!")
            input("\nPress Enter to exit...")
            break


if __name__ == "__main__":
    main()