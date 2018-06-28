def whoseMove(lastPlayer, win):
  if win:
    return lastPlayer
  if lastPlayer == 'white':
    return 'black'
  return 'white'