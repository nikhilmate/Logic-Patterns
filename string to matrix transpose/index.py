import math
n = 'roqfqeylxuyxjfyqterizzkhgvngapvudnztsxeprfp'
ar = [x for x in n if x != " "]
print(ar)
rows = math.floor(math.sqrt(len(ar)))
cols = math.ceil(math.sqrt(len(ar)))
if rows * cols < len(ar):
    while rows * cols < len(ar):
        if cols > rows:
            rows += 1
        else:
            cols += 1
print(rows, cols)

mat = []
count = []
for i in range(0, rows):
    row = []
    for j in range(0, cols):
        print((i*cols + j))
        if ((i * cols) + j)  < len(ar):
            row.append(ar[(i * cols) + j])
        else:
            row.append("")
    mat.append(row)
print(mat)
print(len(mat), len(mat[0]))
# temp = [[] for x in range(0, )]
# counter = 0
# for i in range(0, cols):
#     for j in range(0, rows):
#         if counter < len(ar):
#             temp[j].append(mat[i][j])
#             counter += 1
#     temp.append([])
# print(temp)
final = []
rows = len(mat)
cols = len(mat[0])
counter = 0
print(len(ar))
for i in range(0, len(mat[0])):
    if counter < len(ar):
        row = ''
        for j in range(0, len(mat)):
            if counter <= (rows*cols):
                row += mat[j][i]
#                 print(i, j, mat[j][i])
#     #             print(counter, mat[j][i])
                counter += 1
            else:
                break
        final.append(row)
    else:
        break
    
    print("\\\\\\")
print(final)