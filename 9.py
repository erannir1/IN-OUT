import numpy as np
import matplotlib.pyplot as plt


def read_file(path):
    try:
        with open (path, "r") as c:
            grades = list()
            exercises = list()
            students_ids = list()
            l_1 = c.readline() # reads line 1
            l_1 = l_1.strip("\n").split(",")
            l_1 = l_1[1:-1] # removes str "student_id" and " "
            for i in l_1:
                i = int(i)
                students_ids.append(i)
            for line in c:
                next_l = line.strip("\n").split(",")
                exercises.append(int(next_l[0]))
                grades.append([int(grade)for grade in next_l[1:-1]])
            return np.array(exercises), np.array(students_ids), np.array(grades)
    except IOError:
        print "Cannot read file, exiting!!!"


def compute_total_average(grades):
    return np.mean(grades)


def compute_average_per_exercise(grades, exercises):
    return np.vstack((exercises, np.mean(grades, axis=1)))


def compute_max_grade_per_student(grades, students_ids):
    return np.vstack((students_ids, np.max(grades, axis=0)))


def find_student_with_max_avg(grades, ids):
    return ids[np.argmax(np.mean(grades, axis=0))]


def number_of_students_with_average_above(grades, ids, thr):
    return sum(np.mean(grades, axis=0) > thr)
    #masks if lower than thr
    #sums the True in the mask

def replace_lower_than(grades, thr):
    mask_r_l_t = grades < thr
    grades[mask_r_l_t] = thr



def check_if_passed(grades, pos):
    h_t_55_mask = grades[:,pos] > 55
    return np.all(h_t_55_mask)


def compute_statistics(grades):
    mean = np.mean(grades, axis=1)
    median = np.median(grades, axis=1)
    std = np.std(grades, axis=1)
    return np.array([mean,median,std])


def plot_exercises_scores(exercises, vals, semester_id):
    x = exercises
    y = vals
    plt.title(("Exercise scores for semester " + semester_id), fontsize = 20)
    plt.xlabel("exercise number", fontsize=16)
    plt.ylabel("score", fontsize=16)
    plt.bar(x, y, color='orange')
    plt.tick_params(labelsize=12)
    plt.ylim(0, 100)
    plt.xticks(exercises)
    plt.legend()
    plt.show()





def add_bonus(grades):
    pass


PATH = "example.csv" ## replace this to grades.csv to further test your code

## part A
exercises, students_ids, grades = read_file(PATH)
print 'total exercise, ids, grades', exercises.shape[0], students_ids.shape[0], grades.size

## part B
print 'total avg.', compute_total_average(grades)

## part C
avg_per_exercise = compute_average_per_exercise(grades, exercises)
print 'avg. per exercise', avg_per_exercise

## part D
max_grade_per_student = compute_max_grade_per_student(grades, students_ids)
print 'max get for student in column 1', max_grade_per_student[:, 1]

## part E
student = find_student_with_max_avg(grades, students_ids)
print 'student with max avg.', student

## part F
thr = 95
print number_of_students_with_average_above(grades, students_ids, thr), 'students scored more than', thr

## part G
changed_grades = grades.copy()
replace_lower_than(changed_grades, 72)
print 'grades for first student after replacment', changed_grades[:, 1]

## part H
pos_ = 2
id_ = students_ids[pos_]
res = check_if_passed(grades, pos_)
if res:
    print 'student', id_, 'passed!'
else:
    print 'student', id_, 'failed!'

## part I
statistics = compute_statistics(grades)
print 'basic statistics:\n', statistics

## part J
plot_exercises_scores(exercises, statistics[0], '2018/9a')

## Extra:
grades = add_bonus(grades)
print grades
