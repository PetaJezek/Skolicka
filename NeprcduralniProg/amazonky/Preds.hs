module Main where

import Amazonky (Board, Move, getBestMove, getAllLegalMoves, alphabeta, updateBoard)
import Data.Array.Unboxed (array, (//))

puzzleBoard :: Board
puzzleBoard =
    array ((0, 0), (9, 9)) [((x, y), 3) | x <- [0 .. 9], y <- [0 .. 9]]
        // [ ((2, 3), 1), ((2, 5), 2)
           , ((2, 2), 0), ((2, 4), 0)
           , ((3, 2), 0), ((3, 5), 0)
           , ((4, 2), 0), ((4, 5), 0)
           , ((5, 2), 0), ((5, 3), 0), ((5, 4), 0), ((5, 5), 0)
           ]

expectedMove :: Move
expectedMove = ((2, 5), (3, 5), (2, 4)) -- C6 D6 C5

nejlepsiSkore :: Int
nejlepsiSkore = maximum (map spocitejSkore (getAllLegalMoves puzzleBoard 1))

spocitejSkore :: Move -> Int
spocitejSkore tah = alphabeta (updateBoard puzzleBoard tah 1) 9 1 0 (-99999) 99999

pocetNejlepsichTahu :: Int
pocetNejlepsichTahu = length (filter jeNejlepsi (getAllLegalMoves puzzleBoard 1))
  where
    jeNejlepsi tah = spocitejSkore tah == nejlepsiSkore

-- AI vybere ocekavany move
test1 :: Bool
test1 = getBestMove puzzleBoard 1 10 == Just expectedMove

-- Ocekavany tah je jediny nejlepsi
test2 :: Bool
test2 = pocetNejlepsichTahu == 1

vsechnyTestyProsly :: Bool
vsechnyTestyProsly = test1 && test2

main :: IO ()
main = do
    putStrLn ("test1: " ++ show test1)
    putStrLn ("test2: " ++ show test2)
    putStrLn ("vsechny testy prosly: " ++ show vsechnyTestyProsly)