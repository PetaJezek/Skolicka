type Random = [Int] -- typové synonymum

-- nekonecny seznam pseudonahodnych cisel z intervalu 0 .. 2^31-1
random :: Random
random = iterate f 123456789
  where f x = (1103515245 * x + 12345) `mod` (2 ^ 31)

-- pro zadaný rozsah (dolni, horni) a pseudonahodny generator 
-- vrati pseudonahodne cislo v intervalu dolni..horni 
-- a novou verzi generatoru  
randomR :: (Int, Int) -> Random -> (Int, Random)
randomR (dolni, horni) (r : rand) =
    (dolni + r * (horni - dolni + 1) `div` (2 ^ 31), rand)

-- pro zadaný rozsah (dolni, horni) a pseudonahodny generator 
-- vrati nekonecny seznam pseudonahodnych cisel 
-- v intervalu dolni..horni
randomRs :: (Int, Int) -> Random -> Random
randomRs (dolni, horni) rs =
    let (x, rs') = randomR (dolni, horni) rs
    in x : randomRs (dolni, horni) rs'

-- pro zadaný seznam a pseudonahodny generator 
-- vrati nahodny prvek seznamu a novou verzi generatoru
randomElem :: [a] -> Random -> (a, Random)
randomElem xs gen =
    let (i, gen') = randomR (0, length xs - 1) gen
    in (xs !! i, gen')


type Sachovnice = [Int]

ohrozujiSe :: (Int, Int) -> (Int, Int) -> Bool
ohrozujiSe (c1, r1) (c2, r2) =
    r1 == r2 || abs (c1 - c2) == abs (r1 - r2)

pocetKonfliktu :: Int -> Int -> Sachovnice -> Int
pocetKonfliktu testovanySloupec testovanyRadek deska =
    let 
        damySeSloupci = zip [1 .. length deska] deska
        -- Vybereme všechny kromě té v testovaném sloupci
        ostatniDamy = [ (c, r) | (c, r) <- damySeSloupci, c /= testovanySloupec ]
        -- Spočítáme s kolika z nich konfilktuje
        konflikty = [ () | dama <- ostatniDamy, ohrozujiSe (testovanySloupec, testovanyRadek) dama ]
    in length konflikty


sloupceSKonfliktem :: Sachovnice -> [Int]
sloupceSKonfliktem deska =
    let n = length deska
    in [ c | c <- [1 .. n], pocetKonfliktu c (deska !! (c - 1)) deska > 0 ]

nahradPrvek :: Int -> Int -> [Int] -> [Int]
nahradPrvek 1 novaHodnota (_ : zbytek) = novaHodnota : zbytek
nahradPrvek i novaHodnota (x : zbytek) = x : nahradPrvek (i - 1) novaHodnota zbytek
nahradPrvek _ _ []                     = []



damy :: Sachovnice -> Random -> Int -> (Sachovnice, Int)
damy deska gen krok =
    let spatneSloupce = sloupceSKonfliktem deska
    in if null spatneSloupce
       then (deska, krok) -- konec
       else
         let n = length deska

             -- vybereme jeden sloupec, který má konflikt
             (idxSloupce, gen1) = randomR (0, length spatneSloupce - 1) gen
             vybranySloupec     = spatneSloupce !! idxSloupce

             -- počet konfliktů pro každý řádek (1..n) v tomto sloupci
             radkySKonflikty = [ (r, pocetKonfliktu vybranySloupec r deska) | r <- [1 .. n] ]
             nejmeneKonfliktu = minimum [ k | (_, k) <- radkySKonflikty ]
             nejlepsiRadky    = [ r | (r, k) <- radkySKonflikty, k == nejmeneKonfliktu ]
            -- pokud jich je vic vybere nahodne jeden z nich
             (idxRadku, gen2) = randomR (0, length nejlepsiRadky - 1) gen1
             novyRadek        = nejlepsiRadky !! idxRadku
            -- 
             novaDeska = nahradPrvek vybranySloupec novyRadek deska
         in damy novaDeska gen2 (krok + 1)

tisk :: Sachovnice -> String
tisk deska = unlines [ unwords [ znak c r | c <- [1 .. n] ] ++ " " | r <- [1 .. n] ]
  where
    n = length deska
    znak c r = if deska !! (c - 1) == r then "Q" else "."


main :: IO ()
main = do
    n <- readLn
    gen <- return random
    let startovniDeska = take n (randomRs (1, n) gen)
        (vysledek, iterace) = damy startovniDeska gen 0
    putStr (tisk vysledek)
    putStrLn (show iterace ++ " iterations")

            