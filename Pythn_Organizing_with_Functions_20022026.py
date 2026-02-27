
def calculate_grade(*scores, **adjustments):
    # Calculate average of scores
    total = 0 
    for score in scores:
        total+=score
    average = total / len(scores)
    
    # average = sum(scores) / len(scores)
    
    # Add total bonus adjustments
    bonus = 0 
    for value in adjustments.values():
        bonus += value
        
    # bonus = sum(adjustments.values())
        
    # Final grade
    final_grade = average + bonus
    
    return final_grade


# Student 1 (No bonus)
grade1 = calculate_grade(85, 90, 78)
print(f"Final Grade: {grade1:.2f}%")

# Student 2 (With bonus)
grade2 = calculate_grade(70, 65, 80, attendance=5, project=10)
print(f"Final Grade: {grade2:.2f}%")
