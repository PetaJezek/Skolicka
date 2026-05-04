queens :: [Int] -> Bool
queens positions = not (any threatens pairs)
  where
    queen = zip [0..] positions
    pairs = [(i, j ) | i <- queen, j <- queen, i < j]
    threatens ((x1,y1), (x2, y2)) =
        x1 == x2 || 
        y1 == y2 || 
        abs (x1 - x2) == abs (y1 - y2)