from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # solution one: 暴力
        res = 0
        for x in arr1:
            cnt = 0
            for y in arr2:
                if abs(x-y) <= d:
                    break
                else:
                    cnt += 1
                if cnt == len(arr2):
                    res += 1
        return res

        # solution two: 一行代码
        return sum(all(abs(a1 - a2) > d for a2 in arr2) for a1 in arr1)

if __name__ == "__main__":
    arr1 = [-803,715,-224,909,121,-296,872,807,715,407,94,-8,572,90,-520,-867,485,-918,-827,-728,-653,-659,865,102,-564,-452,554,-320,229,36,722,-478,-247,-307,-304,-767,-404,-519,776,933,236,596,954,464]
    arr2 = [817,1,-723,187,128,577,-787,-344,-920,-168,-851,-222,773,614,-699,696,-744,-302,-766,259,203,601,896,-226,-844,168,126,-542,159,-833,950,-454,-253,824,-395,155,94,894,-766,-63,836,-433,-780,611,-907,695,-395,-975,256,373,-971,-813,-154,-765,691,812,617,-919,-616,-510,608,201,-138,-669,-764,-77,-658,394,-506,-675,523,730,-790,-109,865,975,-226,651,987,111,862,675,-398,126,-482,457,-24,-356,-795,-575,335,-350,-919,-945,-979,611]
    d = 37
    print(Solution().findTheDistanceValue(arr1, arr2, d))