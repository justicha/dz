def f(hospital, student, matching):
    hospital_in = {}
    for name_hospital, name_student in matching.items():
        hospital_in[name_student] = name_hospital

    for name_hospital, name_student in matching.items():
        for good_student in hospital[name_hospital]:
            if good_student == name_student:
                break
                
            elif good_student in hospital_in:
                hospital_now = hospital_in[good_student]
                if student[good_student].index(name_hospital) < student[good_student].index(hospital_now):
                    return f"Неустойчивая пара: {name_hospital} и {good_student}"
    
    return "Паросочетание устойчиво"

hospital = {
    'Atlanta': ['Xavier', 'Yolanda', 'Zeus'],
    'Boston': ['Yolanda', 'Xavier', 'Zeus'],
    'Chicago': ['Xavier', 'Yolanda', 'Zeus']
}

student = {
    'Xavier': ['Boston', 'Atlanta', 'Chicago'],
    'Yolanda': ['Atlanta', 'Boston', 'Chicago'],
    'Zeus': ['Atlanta', 'Boston', 'Chicago']
}

matching = {'Atlanta': 'Zeus', 'Boston': 'Yolanda', 'Chicago': 'Xavier'}

f(hospital, student, matching)
