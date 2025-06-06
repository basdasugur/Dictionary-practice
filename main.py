
# Practice for dictionary,


grades = {
    "Ali" : 85,
    "Zeynep" : 92,
    "Mehmet" : 76,
    "Uğur" : 95,
    "Akın" : 88,
    "Mahmut" : 45,
    "Azra" : 30
}


# Add a new student

grades["Berke"] = 65

print(grades)

# Update a student's grade
grades["Mehmet"] = 85
print(grades)


grades.update({
    "Mahmut": 60,
    "Azra": 55,
    "Ayşe": 78
      })

