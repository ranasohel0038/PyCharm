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
    print("=" * 54)
    print("             GPA CALCULATOR PROGRAM             ")
    print("=" * 54)

    try:
        main_sub_count = int(input("\nTotal Main Subject Count: "))

        main_subjects = []
        total_main_gpa = 0.0
        has_failed = False

        # 1. Main subjects input
        for i in range(1, main_sub_count + 1):
            sub_name = input(
                f"\n{i} No. Subject: "
            ).strip()

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
                has_failed = True

            total_main_gpa += gpa
            main_subjects.append(
                {
                    "subject": sub_name,
                    "marks": marks,
                    "grade": grade,
                    "gpa": gpa,
                }
            )

        # 2. Main subjects calculation
        if has_failed:
            main_final_gpa = 0.00
            main_final_grade = "F (Failed)"
        else:
            main_final_gpa = total_main_gpa / main_sub_count
            main_final_grade = get_letter_grade(main_final_gpa)

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
            input("\nDo you have 4th (Optional) Subject? (y/n): ")
            .strip()
            .lower()
        )

        if choice in ["yes", "y"]:
            opt_sub_name = input("\n4th Subject Name: ").strip()

            while True:
                try:
                    opt_marks = float(
                        input(
                            f"'{opt_sub_name}' Obtained Marks (0-100): "
                        )
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
            print("                 FINAL RESULT WITH 4TH SUBJECT                 ")
            print("=" * 60)
            print(
                f"{opt_sub_name} (4th Subject) | Marks: {opt_marks} | Grade: {opt_grade} | GPA: {opt_gpa}"
            )
            print("-" * 60)

            if has_failed or opt_grade == "F":
                opt_final_gpa = 0.00
                opt_final_grade = "F (Failed)"
            else:
                calculated_gpa = (
                    total_main_gpa + extra_gpa
                ) / main_sub_count
                opt_final_gpa = min(5.00, calculated_gpa)
                opt_final_grade = get_letter_grade(opt_final_gpa)

            print(f"4th Subject Bonus Point: +{extra_gpa:.2f}")
            print(f"Final GPA: {opt_final_gpa:.2f}")
            print(f"Final Grade: {opt_final_grade}")
            print("=" * 60)

        else:
            # For no or 'n'
            print("\n" + "=" * 60)
            print("             FINAL RESULT WITHOUT 4TH SUBJECT             ")
            print("=" * 60)
            print(f"Final GPA: {main_final_gpa:.2f}")
            print(f"Final Grade: {main_final_grade}")
            print("=" * 60)

    except ValueError:
        print("\nError: Please enter valid numbers.")


if __name__ == "__main__":
    main()