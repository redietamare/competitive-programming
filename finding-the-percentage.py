if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    results= student_marks[query_name]
    sum= 0
    for i in results:
       sum+=i
       i+=1
average= float(sum/len(results))
floatav= format(average,'.2f')

print(floatav)
