# Store the input into a dictionary with structure
# {
#     <name>: '<array of scores>'
# }
# get the average score of the query name


# Sample input:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    scores_list = student_marks[query_name]
    # print(scores_list)

    res = [sum(scores_list) / len(scores_list) for score in scores_list]

    print(format(res[0], '.2f'))
