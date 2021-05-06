# class Solution(object):
#     def areacover(self, radius, x_center, y_center, x1, y1, x2, y2):
#         if x1 <=x_center <= x2 and y1 <= y_center <= y2:
#             return True
#         elif x_center > x2 and y1 <= y_center <= y2:
#             return radius >=x_center - x2
#         elif y_center < y1 and x1 <= x_center <= x2:
#             return radius >= y1 - y_center
#         elif x_center < x1 and y1 <= y_center <=y2:
#             return radius >= x1 - x_center
#         elif y_center > y2 and x1 <= x_center <= x2:
#             return radius >=y_center - y2
#         else:
#             return min((x1 - x_center)**2 + (y2 - y_center)**2, (x2 - x_center)**2 + (y2 - y_center)**2,
#                        (x2 - x_center)**2 + (y1 - y_center)**2, (x1 - x_center)**2 + (y1 - y_center)**2)
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     print(solution.areacover(1,1,1,-3,-3,3,3))

