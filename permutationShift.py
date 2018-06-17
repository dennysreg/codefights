def permutationShift(permutation):
  shift=[]
  for i in range(len(permutation)):
    shift.append(permutation[i]-i)
  return max(shift)-min(shift)