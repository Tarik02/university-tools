ii = lambda: [int(i) for i in input().split()]

mat = [ii()]

for _ in range(1, len(mat[0])):
	mat.append(ii())


def det(m):
	if len(m) == 2:
		return m[0][0] * m[1][1] - m[0][1] * m[1][0]

	acc = 0
	for i in range(len(m)):
		sign = pow(-1, 1 + 1 + i)
		acc += m[i][0] * sign * det(
			[i[1:] for i in (m[:i] + m[i + 1:])]
		)

	return acc


print(det(mat))
