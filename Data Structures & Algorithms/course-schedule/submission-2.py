class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        visited = set()
        courses = {}

        for i in range(numCourses):
            courses[i] = []

        for course, prereq in prerequisites:
            courses[course].append(prereq)
                    
        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for prereq in courses[course]:
                if dfs(prereq) == False:
                    return False

            path.remove(course)
            visited.add(course)
            return True

        for course in courses.keys():
            if dfs(course) == False:
                return False

        return True            