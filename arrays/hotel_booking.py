class Solution:
    @staticmethod
    def hotel_booking(ARR, DEP, RM):
        guest_count = i = j = 0
        count = 1

        comb = list(zip(ARR, DEP))
        comb.sort(key=lambda x: x[0])
        ARR.sort()
        DEP.sort()

        while i < len(ARR):
            RM -= 1

            if ARR[i] >= DEP[i-1]:
                RM += 1

            if RM < 0:
                return 0
            i += 1

        return 1

    @staticmethod
    def hotel_bookingB(arrive, depart, K):
        arrive.sort()
        depart.sort()
        i = 0
        j = 0

        while i < len(arrive) and j < len(depart):

            K -= 1
            if arrive[i] >= depart[j]:
                j += 1
                K += 1
            if K < 0:
                return 0
            i += 1

        return 1


if __name__ == '__main__':
    s = Solution
    arrivals = [1, 3, 5]
    depart = [2, 6, 8]

    arrivals1 = [1, 3, 9]
    depart1 = [4, 8, 6]
    number_of_room = 2
    print(s.hotel_bookingB(arrivals1, depart1, number_of_room))
