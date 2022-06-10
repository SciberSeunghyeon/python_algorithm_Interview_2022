class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        sizex, sizey = len(image) - 1, len(image[0]) - 1

        #BFS
        seen = []
        frontier = [(sr, sc)]

        def expand(pixel):
            return ((min(sizex, pixel[0] + 1), pixel[1]), (max(0, pixel[0] - 1), pixel[1]),
                    (pixel[0], min(sizey, pixel[1] + 1)), (pixel[0], max(0, pixel[1] - 1)))

        #BFS
        while frontier:
            next = []
            for u in frontier:
                for v in expand(u):
                    if v not in seen:
                        try:
                            if image[v[0]][v[1]] == oldColor:
                                seen.append(v)
                                next.append(v)
                        except:
                            pass
                image[u[0]][u[1]] = newColor
            frontier = list(next)

        return image
