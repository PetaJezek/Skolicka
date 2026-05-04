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
balanced (Node left x right) = balanced left && balanced right && abs (height left - height right) <= 1

height :: Tree -> Int
height Nil = 0
height (Node left x right) = 1 + max (height left) (height right)