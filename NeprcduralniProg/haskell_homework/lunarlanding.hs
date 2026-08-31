module Main where

import Data.Char (isDigit, digitToInt, intToDigit)
import Data.Set (Set, empty, insert, member)

type Pos    = (Int, Int)
type State  = [Pos]
type Action = (Int, Pos, Pos)

stred :: Pos
stred = (3, 3)

-- Projde každý znak vstupu, najde jejich pozici. Serazene od kosmonauta po posledniho robota
nactiVstup :: String -> State
nactiVstup vstup = [najdiPozici n | n <- [0 .. maxCislo]]
  where
    radky    = lines vstup
    maxCislo = digitToInt (maximum [znak | radek <- radky, znak <- radek, isDigit znak])
    najdiPozici n = head [ (sloupec+1, radek+1)
                         | (radek, radekZnaky) <- zip [0..] radky
                         , (sloupec, znak)     <- zip [0..] radekZnaky
                         , znak == intToDigit n ]

-- Posouvá postavu z pozice (x,y) směrem (dx,dy).
posunAz :: Pos -> Pos -> [Pos] -> Maybe Pos
posunAz (x, y) (dx, dy) obsazene =
    let (nx, ny) = (x + dx, y + dy)
    in if nx < 1 || nx > 5 || ny < 1 || ny > 5
       then Nothing
       else if (nx, ny) `elem` obsazene
            then Just (x, y)
            else posunAz (nx, ny) (dx, dy) obsazene

-- Pro vsechny postavy zkusi vsechny moves
mozneKroky :: State -> [(State, Action)]
mozneKroky stav =
    [ (novyStav, (i, staraPoloha, novaPoloha))
    | (i, staraPoloha) <- zip [0..] stav
    , (dx, dy)         <- [(0, -1), (0, 1), (-1, 0), (1, 0)]
    , let obsazene   = [poloha | (j, poloha) <- zip [0..] stav, j /= i]
    , Just novaPoloha <- [posunAz staraPoloha (dx, dy) obsazene]
    , novaPoloha /= staraPoloha
    , let novyStav   = [if j == i then novaPoloha else poloha | (j, poloha) <- zip [0..] stav]
    ]

-- Ze starých a nových souřadnic odvodí pismeno směru
nazevSmeru :: Pos -> Pos -> String
nazevSmeru (x1, y1) (x2, y2)
    | y2 < y1   = "U"
    | y2 > y1   = "D"
    | x2 < x1   = "L"
    | otherwise  = "R"

-- Převede akci na 5u napr.
akceNaText :: Action -> String
akceNaText (i, odkud, kam) = show i ++ nazevSmeru odkud kam

-- Helper funkce pro hledej
vyres :: State -> Maybe [Action]
vyres pocatecniStav = hledej [(pocatecniStav, [])] (insert pocatecniStav empty)

hledej :: [(State, [Action])] -> Set State -> Maybe [Action]
hledej [] _ = Nothing
hledej ((stav, akce) : zbytek) navstivene
    | head stav == stred = Just (reverse akce)
    | otherwise =
        let dalsiStavy     = [ (novyStav, novaAkce : akce)
                             | (novyStav, novaAkce) <- mozneKroky stav
                             , not (member novyStav navstivene) ]
            novaNavstivene = foldr insert navstivene (map fst dalsiStavy)
            novaFronta     = zbytek ++ dalsiStavy
        in hledej novaFronta novaNavstivene

main :: IO ()
main = do
    vstup <- getContents
    let stav = nactiVstup vstup
    case vyres stav of
        Nothing   -> putStrLn "no solution"
        Just akce -> putStrLn (unwords (map akceNaText akce))
