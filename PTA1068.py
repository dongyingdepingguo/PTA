# !/usr/bin/env python

# _*_ coding: utf-8 _*_

M, N, TOL = [int(i) for i in input().split()]
image = []
unique = ''
count = 0
for _ in range(N):
    image.append(input().split())
for i in range(1, N-1):
    for j in range(1, M-1):
        tol1 = int(image[i][j]) - int(image[i+1][j])
        tol2 = int(image[i][j]) - int(image[i+1][j+1])
        tol3 = int(image[i][j]) - int(image[i+1][j-1])
        tol4 = int(image[i][j]) - int(image[i][j+1])
        tol5 = int(image[i][j]) - int(image[i][j-1])
        tol6 = int(image[i][j]) - int(image[i-1][j+1])
        tol7 = int(image[i][j]) - int(image[i-1][j-1])
        tol8 = int(image[i][j]) - int(image[i-1][j])
        if tol1 > TOL and tol2 > TOL and tol3 > TOL and tol4 > TOL and tol5 > TOL and tol6 > TOL and tol7 > TOL and tol8 > TOL:
            count += 1
            if count == 1:
                unique = '(%d, %d): %d' % ((j + 1), (i + 1), int(image[i][j]))
            else:
                print('Not Unique')
                break
    else:
        continue
    break
if count == 1:
    print(unique)
if unique == '':
    print('Not Exist')