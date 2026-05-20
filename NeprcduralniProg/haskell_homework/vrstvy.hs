import Data.List (sort, groupBy, nub)
import  Data.Set  (fromList, notMember)
 
vrstvy :: Ord a => [(a, a)] -> [[a]]
vrstvy hrany = zpracujVrstvy (vytvorGraf hrany)
  where
    -- Převedení seznamu hran na seznam sousednosti pro kady vrchol ve tvaru (vrchol, [sousedi])
    vytvorGraf :: Ord a => [(a, a)] -> [(a, [a])]
    vytvorGraf h = seznamSousednosti(sort(oboustraneHrany h)) 
    
    oboustraneHrany :: Ord a => [(a,a)] -> [(a,a)]
    oboustraneHrany  = concatMap (\(x,y) -> [(x,y), (y,x)]) 

    seznamSousednosti :: Ord a => [(a,a)] -> [(a, [a])]
    seznamSousednosti hrany = 
        let grouped = groupBy (\(x1, _) (x2, _) -> x1 == x2) hrany
        in map seskup grouped
        where
            seskup :: [(a,a)] -> (a, [a])
            seskup hranyVrcholu = 
                let v = fst (head hranyVrcholu)
                    sousedi = [y | (_, y) <- hranyVrcholu]
                in (v, sousedi)
         
    zpracujVrstvy :: Ord a => [(a, [a])] -> [[a]]
    zpracujVrstvy [] = []
    zpracujVrstvy graf = 
        let 
            
            -- Najdeme listy
            listy =  filter (\ (_, sousedi) -> length sousedi <= 1)graf
                
            zbytekGrafu = odstraneniListu graf listy
                where 
                    odstraneniListu :: Ord a => [(a, [a])] -> [(a, [a])] -> [(a, [a])]
                    odstraneniListu graf listy = 
                        let
                        listySet = fromList [v | (v,_) <- listy]
                        --- Bereme vsechny (v, sousdy) z grafu. Smazeme nechame ty ktere nemaji vrchol v  listySet a pak vysledne filtrujeme sousedy zbyvajicih vrcholu abychom odtranili listy
                        in [ (v, filter (`notMember` listySet) sousedi) | (v, sousedi) <- graf, notMember v listySet ]
            
            hodnotyListu = sort [v | (v, _) <- listy] 
        in 
         
            hodnotyListu : zpracujVrstvy zbytekGrafu