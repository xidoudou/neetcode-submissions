class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited = set()
        visiting = set()
        res = []

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True

            if preMap[crs] == []:
                res.append(crs)
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            res.append(crs)
            visited.add(crs)
            visiting.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        


        