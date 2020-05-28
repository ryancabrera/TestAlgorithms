import collections

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        print(dislikes)
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}


        def dfs(node, c=0):
            if node in color:
                print(type(color))
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node)
                   for node in range(1, N + 1)
                   if node not in color)


def main():
    N = 4
    #dislikes = list()
    #dislikes.append([1,2])
    #dislikes.append([1,3])
    #dislikes.append(([2,4]))
    #print(dislikes)
    dislikes = [[1,2],[1,3], [1,4]]
    ret = Solution().possibleBipartition(N, dislikes)

    out = (ret)
    print out

if __name__ == '__main__':
    main()
#output = Solution()
#print(Solution.possibleBipartition(output, [[1,2],[1,3],[2,4]],4))