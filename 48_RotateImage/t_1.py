class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for pixels in matrix[::-1]:
            for pos, pixel in enumerate(pixels[:n]):
                matrix[pos].append(pixel)
            pixels[:] = pixels[n:]
