# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.
#
# When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)
#
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.
#
#
#
# Example 1:
#
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.

class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.seats = {i: None for i in range(N)}


    def seat_dist(self, seat):
        non_empties = [k for k, v in self.seats.items() if v]
        if not non_empties:
            return None
        return min([abs(seat - seat2) for seat2 in non_empties])


    def seat(self):
        """
        :rtype: int
        """
        empties = [k for k, v in self.seats.items() if not v]
        if len(empties) == self.N:
            self.seats[0] = 1
            return 0
        dists = {seat: self.seat_dist(seat) for seat in empties}
        max_dist = max(dists.values())
        seat = min([k for k, v in dists.items() if v == max_dist])
        self.seats[seat] = 1
        return seat


    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.seats[p] = None
        return



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
