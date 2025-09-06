def gather_credits(number_of_credits_needed, *course_info):
    taken_courses = set()
    total_credits = 0

    for course_name, course_credits in course_info:
        if course_name in taken_courses:
            continue
        else:
            taken_courses.add(course_name)
            total_credits += course_credits
            if total_credits >= number_of_credits_needed:
                break

    if total_credits >= number_of_credits_needed:
        return f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(sorted(taken_courses))}"
    else:
        return f"You need to enroll in more courses! You have to gather {number_of_credits_needed - total_credits} credits more."

print(gather_credits(60,("Basics", 27),("Fundamentals", 27),("Advanced", 30),("Web", 30)))