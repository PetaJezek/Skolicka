data Tree = Nil | Node Tree Int Tree
  deriving (Eq, Ord, Show)

allBalanced :: Int -> [Tree]
allBalanced 0 = [Nil]
allBalanced n = [x | x <- allPossibleTrees (1,n), balanced x]

allPossibleTrees :: (Int, Int) -> [Tree]
allPossibleTrees (0,0) = [Nil]
allPossibleTrees (low, high)
  | low > high = [Nil]
  | otherwise = [Node left x right | x <- [low..high],
                left <- allPossibleTrees (low, x - 1),
                right <- allPossibleTrees (x + 1, high)]


balanced :: Tree -> Bool
balanced Nil = True
balanced (Node left x right) = balanced left && balanced right && abs (count left - count right) <= 1

count :: Tree -> Int
count Nil = 0
count (Node left x right) = 1 + count left + count right