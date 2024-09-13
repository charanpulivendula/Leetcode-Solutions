
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # points.sort(key=lambda x : (-x[1],x[0]))
        points.sort(key=lambda x : (x[0],-x[1]))
        print(points)
        count = 0
        for i in range(len(points)-1):
            max_x = points[i][0]
            max_y = points[i][1]
            min_x = points[i][0]
            min_y = points[i][1]
            first_found = True
            for j in range(i+1, len(points)):
                if (points[j][0] >= points[i][0] and points[j][1] <= points[i][1]):
                    if j == i + 1:
                        count += 1
                        if first_found:
                            first_found = False
                            max_x = points[j][0]
                            min_x = points[j][0]
                            min_y = points[j][1]
                            max_y = points[j][1]
                    else:
                        if first_found:
                            count += 1
                            first_found = False
                            max_x = points[j][0]
                            min_x = points[j][0]
                            min_y = points[j][1]
                            max_y = points[j][1]
                            continue
                        if (points[j][0] > max_x and points[j][1] > max_y):
                            count += 1
                            max_x = points[j][0]
                            max_y = points[j][1]
                        elif (points[j][0] < min_x and points[j][1] < min_y):
                            count += 1
                            min_y = points[j][1]
                            min_x = points[j][0]
                        
        return count