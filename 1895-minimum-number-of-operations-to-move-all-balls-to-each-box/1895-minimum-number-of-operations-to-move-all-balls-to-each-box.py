class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Initialize the answer array 
        answer = []
        # Two pointers for the current box and the ith box we want to move all the balls in
        i_box = 0
        curr_box = 0
        # Variable to keep track of the nb of moves needed to put all the balls in the ith box 
        nb_operations = 0
        while i_box < len(boxes):
            # If we searched in all the boxes, we start again with a new ith box
            if curr_box == len(boxes):
                answer.append(nb_operations)
                curr_box, nb_operations = 0, 0
                i_box += 1
            # Ignore the ith box 
            elif i_box == curr_box:
                curr_box += 1
            # If there is a ball in the current box, we compute the needed moves to place it in the ith box    
            elif boxes[curr_box] == "1":
                nb_operations += abs(i_box - curr_box)
                curr_box += 1
            else:
                curr_box += 1
        return answer