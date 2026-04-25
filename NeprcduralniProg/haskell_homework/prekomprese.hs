import Data.List (isPrefixOf)

prekomprese :: String -> [(Int, Int, Char)]
prekomprese vstup = helper "" vstup

-- Náš helper bere Levou část, Pravou část a vrací seznam trojic
helper :: String -> String -> [(Int, Int, Char)]
helper _ "" = []  -- Konec rekurze: pokud už není co číst, vracíme prázdný seznam
helper leva prava = 
    let 
        -- Tady se odehraje ta tvoje "matika"
        (v, d, z) = najdiNejdelsiPredponu leva prava 
        
        -- Připravíme si nové řetězce pro další krok rekurze
        zpracovanyKus = take (d + 1) prava
        novaLeva = leva ++ zpracovanyKus
        novaPrava = drop (d + 1) prava
    in 
        -- Vrátíme spočítanou trojici a připojíme k ní zbytek (rekurzivní volání)
        (v, d, z) : helper novaLeva novaPrava


najdiNejdelsiPredponu :: String -> String -> (Int, Int, Char)
najdiNejdelsiPredponu leva prava =
    let
        maxDelka = length prava - 1 
        delky = [maxDelka, maxDelka - 1 .. 0]        
        (d, v) = najdiPrvniShodu delky        
        z = prava !! d
    in
        (v, d, z)
    where
        najdiPrvniShodu :: [Int] -> (Int, Int)
        najdiPrvniShodu [] = (0, 0) -- Fallback, length 0 always matches
        najdiPrvniShodu (d:ds)
            | Just vzdalenost <- pozicePodretezce (take d prava) leva = (d, vzdalenost)
            | otherwise = najdiPrvniShodu ds
                
        pozicePodretezce :: String -> String -> Maybe Int
        pozicePodretezce "" _ = Just 0
        pozicePodretezce _ "" = Nothing
        pozicePodretezce hledany text
            -- Uses your custom isPrefixOf function!
            | isPrefixOf hledany text = Just (length text)
            | otherwise = pozicePodretezce hledany (tail text)
