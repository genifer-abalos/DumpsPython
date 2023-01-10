# PROBLEM
# print the names of students (in alphabetical order) who had the second to the lowest score
#

if __name__ == '__main__':
    name_arr = []
    score_arr = []
    row = []
    records = []

    # input number of students, then,
    # alternately,
    #   input name
    #   input score
    for _ in range(int(input())):
        name = input()
        score = float(input())
        row = [name, score]
        records.append(row)

    # print(records)
    # get all the scores from records[] array
    score_arr = [rec[1] for rec in records]
    # print(score_arr)

    score_set = set(score_arr)  # convert list to set to remove duplicate scores
    # print(score_set)
    sorted_score = sorted(score_set)    # sorted() will transform the set {} back to list []
    second_lowest = sorted_score[1]     # the second to the lowest score (arrange in increasing order)
    # print(second_lowest)

    res = [rec[0] for rec in records if rec[1] == second_lowest]
    # print(res)
    # print the result in alphabetical order
    [print(student) for student in sorted(res)]