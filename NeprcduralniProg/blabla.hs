type Graf = [(String, [String])]







sousedniVrcholy :: Graf -> String -> [String]
sousedniVrcholy graf v = [i | [u, i] <- graf,  v == u]

cesta :: Graf -> String -> Int -> Maybe [String]
cesta graf vrchol n = 
    let 
        mnozinavrcholu = sousedniVrcholy vrchol
    in
        cesta2 graf mnozinavrcholu [vrchol] n


