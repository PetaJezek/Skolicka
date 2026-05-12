import Data.Array 
import Data.Char (digitToInt, intToDigit)
type Board = [[Int]]
type Coordinate = (Int, Int)

-- Replaces the value in the list xs at index i with value v
replaceAt :: [Int] -> Int -> Int -> [Int]
replaceAt xs i v = take i xs ++ [v] ++ drop (i + 1) xs 


placeNumber :: Board -> Coordinate -> Int -> Board
placeNumber board (x,y) n =  take y board ++ [replaceAt(board !! y) x n] ++ drop (y + 1) board

getRow :: Board -> Int -> [Int]
getRow board i = board !! i


getColumn :: Board -> Int -> [Int]
getColumn board i = [row !! i | row <- board]

getBlock :: Board -> Coordinate -> [Int]
getBlock board (x,y) = [board !! r !! c | r <- [blockRowStart..blockRowStart+1], c <- [blockColStart..blockColStart+1]]
  where
    blockRowStart = (y `div` 2) * 2
    blockColStart = (x `div` 2) * 2
    

isSafe :: Board -> Coordinate -> Int -> Bool
isSafe board (x,y) n = notElem n (getRow board y) &&
                       notElem n (getColumn board x) &&
                       notElem n (getBlock board (x,y))


findIndex :: [Int] -> Maybe Int
findIndex xs = findIndexHelper xs 0
  where findIndexHelper [] _ = Nothing
        findIndexHelper (x:xs) i = if x == 0 then Just i else findIndexHelper xs (i + 1)

findEmptyRow :: Board -> Maybe Coordinate
findEmptyRow board = findEmptyHelper board 0 
  where findEmptyHelper [] _ = Nothing
        findEmptyHelper (row:rows) y = case findIndex row of
                                        Just x -> Just (x, y)
                                        Nothing -> if y < 5 then findEmptyHelper rows (y + 1) else Nothing


make12Arrays :: [Int] -> [[Int]]
make12Arrays [a, b, c, d, 
              e, f, g, h, 
              i, j, k, l, 
              m, n, o, p] = 
    [ 
     
      [a, b, c, d],
      [e, f, g, h],
      [i, j, k, l],
      [m, n, o, p],
      
      -- 2. The 4 Columns (Straight down)
      [a, e, i, m],
      [b, f, j, n],
      [c, g, k, o],
      [d, h, l, p],
      
      -- 3. The 4 Blocks (The 2x2 squares)
      [a, b, e, f], -- Top Left
      [c, d, g, h], -- Top Right
      [i, j, m, n], -- Bottom Left
      [k, l, o, p]  -- Bottom Right
    ]


solve :: Board -> [Board]
solve board = case findEmptyRow board of
                Nothing -> [board]  
                Just (x,y) -> 
                  let 

                    safeNumbers = [n | n <- [1..4], isSafe board (x,y) n]
                    newBoards = [placeNumber board (x,y) n | n  <- safeNumbers]
                  in 
                    concatMap solve newBoards


parseInput :: String -> Board
parseInput text = map (map digitToInt) (lines text)

formatBoard :: Board -> String
formatBoard board = unlines (map (map intToDigit) board)


main :: IO ()
main = interact solveSudoku

solveSudoku :: String -> String
solveSudoku input =
    let board = parseInput input
        solution = solve board
    in case solution of
        [] -> "No solution found."
        (s:_) -> formatBoard s