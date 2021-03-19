import sys

def main():
    def recursion(stack_ith, plate_needed):
        # base case 
        if stack_ith >= num_stacks or plate_needed <= 0: 
            return 0 
        
        if lookup_table[stack_ith][plate_needed]:
            return lookup_table[stack_ith][plate_needed]

        # recusrive case 
        current_max = 0
        for l in range(0, min(plate_needed, num_plates_per_stack) + 1):
            temp = recursion(stack_ith + 1, plate_needed - l)
            if l > 0:
                temp += plate_piles[stack_ith][l-1]
            current_max = max(current_max, temp)
        lookup_table[stack_ith][plate_needed] = current_max
        return current_max

    T = int(input()) # number of testcases
    for i in range(1, T + 1):
        N, K, P = [int(s) for s in input().split(" ")] #

        num_stacks = N 
        num_plates_per_stack = K 
        num_req_plates = P

        plate_piles = []
        
        for j in range(num_stacks):
            pile = []
            current = 0 
            for s in input().split(" "):
                current += int(s)
                pile.append(current)
            plate_piles.append(pile)

        lookup_table = [[0]*(num_req_plates + 1) for _ in range(num_stacks)]

        result = recursion(0, num_req_plates)
        print("Case #{}: {}".format(i, result))


if __name__ == "__main__":
    main()