import Data.List (nub)
factors :: Integer -> [Integer]
factors n = helper 2 n
    where 
    helper k n
        | n < 2 = []
        | k * k > n = [n]
        | n `mod` k == 0 = k : helper k (n `div` k)
        | otherwise = helper (k + 1) n


squareFree :: [Integer]
squareFree = filter isSquareFree [1..]
    where 
    isSquareFree n 
        | nub (factors n) == factors n = True
        | otherwise = False



squareRoot :: Integer -> Integer
squareRoot n = helper 0 n
    where 
    helper low high
        | low > high = high
        | mid * mid <= n = helper (mid + 1) high
        | otherwise = helper low (mid - 1)
        where mid = (low + high) `div` 2