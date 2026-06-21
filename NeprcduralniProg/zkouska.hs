data Tree a = Node a [Tree a] 
    deriving Show


dfs :: Tree a-> Tree (a, Int, Int)
dfs t = fst(go 1 t) 



go :: Int -> Tree a -> (Tree(a, Int, Int) , Int)
go t (Node x []) = (Node (x, t, t+1) [], t+2)
go t (Node x children) = 
    let (doneChildren, closeTime) = goList (t+1) children
    in 
        (Node (x, t, closeTime) doneChildren, closeTime +1)



goList :: Int -> [Tree a] -> ([Tree (a, Int, Int)], Int)
goList t [] = ([], t)
goList t (c:cs) =
    let (doneC, closeTime1) = go t c
        (doneCs, closeTime2) = goList closeTime1 cs
    in (doneC : doneCs, closeTime2)





type Pozice = (Int, Int)
strelci :: Int -> Int -> Int
strelci k n = 
    let
        vsechnyMoznosti = generuj n k
        dobreReseni = [i | i <- vsechnyMoznosti, neohrozujiSe i]
    in
        length dobreReseni
        




generuj :: Int -> Int -> [[Pozice]]
generuj 0 _ = []
generuj n k =   kombinace vsechnyPozice k
    where 
        vsechnyPozice = [(i,j) | i <- [1..n], j <- [1..n]] 
        kombinace :: [Pozice] -> Int -> [[Pozice]]
        kombinace  _ 0 = [[]]
        kombinace  [] _ = []
        kombinace (x:xs) k = map (x:) (kombinace xs (k-1)) ++ kombinace xs k



neohrozujiSe2 :: Pozice -> Pozice -> Bool
neohrozujiSe2 (x,y) (u, v) = 
    abs(x-u) == abs(y-v)


neohrozujiSe :: [Pozice] -> Bool
neohrozujiSe positions =
    let badPositions =  [(i,j) | i <- positions, j <- positions, i <j, neohrozujiSe2 i j]
    in
        null badPositions
        

