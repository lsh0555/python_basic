N = int(input())

image = []

for _ in range(N):
    image.append(input())


def compress(row, col, size):
    # 현재 영역의 첫 번째 값을 기준값으로 설정
    first = image[row][col]

    # 현재 영역의 모든 픽셀 확인
    for r in range(row, row + size):
        for c in range(col, col + size):

            # 하나라도 다른 값이 있다면 4등분
            if image[r][c] != first:
                half = size // 2

                result = "("

                # 1. 왼쪽 위
                result += compress(row, col, half)

                # 2. 오른쪽 위
                result += compress(row, col + half, half)

                # 3. 왼쪽 아래
                result += compress(row + half, col, half)

                # 4. 오른쪽 아래
                result += compress(row + half, col + half, half)

                result += ")"

                return result

    # 영역 전체가 같은 값이면 0 또는 1 반환
    return first


print(compress(0, 0, N))