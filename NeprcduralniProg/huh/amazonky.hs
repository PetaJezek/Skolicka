import Text.Read (readMaybe)
import Data.Char (toUpper)
import Data.List (intersperse, maximumBy)
import Data.Ord (comparing)
import Data.Array.Unboxed
import System.IO (hFlush, stdout)
import System.IO.Error (tryIOError)

type Board = UArray (Int, Int) Int
type Move = (Pos, Pos, Pos)
type Pos = (Int, Int)

-- vraci pocatecni stav hraci desky
initialBoard :: Board
initialBoard = array ((0,0), (9,9)) [ ((x,y), initVal x y) | x <- [0..9], y <- [0..9] ]
  where
    -- Bílé amazonky 
    initVal 0 3 = 1
    initVal 3 0 = 1
    initVal 6 0 = 1
    initVal 9 3 = 1
    -- Černé amazonky 
    initVal 0 6 = 2
    initVal 3 9 = 2
    initVal 6 9 = 2
    initVal 9 6 = 2
    -- Zbytek je prázdný
    initVal _ _ = 0


parseCord :: String -> Maybe Pos
parseCord (letter:number) = do
    let x = fromEnum (toUpper letter) - fromEnum 'A'
    yy <- readMaybe number :: Maybe Int
    let y = yy - 1 
    if x >= 0 && x <= 9 && y >= 0 && y <= 9
        then Just (x,y)
        else Nothing
parseCord _ = Nothing

-- Bere vstup cloveka a vraci move
parseMove :: String -> Maybe Move
parseMove input = case words input of
    [start, end, arrow] -> do
        s <- parseCord start
        e <- parseCord end
        a <- parseCord arrow
        return (s,e,a)
    _ -> Nothing

serializeSave :: Board -> Int -> Int -> String
serializeSave board currentPlayer moveNumber = unlines $
    ["AMAZONKY 1", show currentPlayer ++ " " ++ show moveNumber]
    ++ lines (renderBoard board)

parseSave :: String -> Maybe (Board, Int, Int)
parseSave content = case lines content of
    "AMAZONKY 1":metadata:boardHeader:rows -> case words metadata of
        [playerText, moveText] -> do
            player <- readMaybe playerText
            moveNumber <- readMaybe moveText
            boardRows <- mapM parseSaveRow rows
            if boardHeader == "   A B C D E F G H I J"
                && player `elem` [0, 1] && moveNumber >= 0
                && map fst boardRows == [9, 8 .. 0]
                && all ((== 10) . length . snd) boardRows
                then Just
                    ( array ((0,0), (9,9))
                        [((x,y), value) | (y,row) <- boardRows,
                                          (x,value) <- zip [0..9] row]
                    , player
                    , moveNumber
                    )
                else Nothing
        _ -> Nothing
    _ -> Nothing
  where
    parseSaveRow row = case words row of
        rowNumber:tiles -> do
            number <- readMaybe rowNumber
            values <- mapM parseTileValue tiles
            if number >= 1 && number <= 10 && length values == 10
                then Just (number - 1, values)
                else Nothing
        _ -> Nothing
    parseTileValue "." = Just 0
    parseTileValue "W" = Just 1
    parseTileValue "B" = Just 2
    parseTileValue "X" = Just 3

loadSave :: FilePath -> IO (Either String (Board, Int, Int))
loadSave path = do
    result <- tryIOError (readFile path >>= \content -> length content `seq` pure content)
    pure $ case result of
        Left err -> Left (show err)
        Right content -> maybe (Left "Neplatny format ulozene pozice.") Right (parseSave content)

-- jednoduchy konvertor z move na string pro vypis
moveToString :: Move -> String
moveToString ((x1, y1), (x2, y2), (x3, y3)) =
    unwords [format x1 y1, format x2 y2, format x3 y3]
  where
    format x y = toEnum (fromEnum 'A' + x) : show (y + 1)

-- 'playing' je číslo hráče na tahu (0 pro bileho tedy cloveka a 1 pro ai)
updateBoard :: Board -> Move -> Int -> Board
updateBoard board (pos1, pos2, pos3) playing = 
    board // [(pos1, 0), (pos2, playing + 1), (pos3, 3)]

-- vraci stav desky na souradnicich 
getState :: Board -> Int -> Int -> Int
getState board x y = board ! (x, y)

-- vraci znak podle stavu
getTileAt :: Board -> Int -> Int -> Char
getTileAt board x y
    | state == 0 = '.'
    | state == 1 = 'W'
    | state == 2 = 'B'
    | state == 3 = 'X'
    | otherwise  = '?'
  where
    state = getState board x y

-- vraci desku v ascii
renderBoard :: Board -> String
renderBoard board = unlines (header : rows)
  where
    header = "   A B C D E F G H I J"
    rows = [ renderRow y | y <- [9, 8 .. 0] ]
    renderRow y = 
        let 
            rowNumber = y + 1 
            gridContent = intersperse ' ' [ getTileAt board x y | x <- [0..9] ]
        in 
            pad rowNumber ++ " " ++ gridContent
    pad n 
        | n < 10    = show n ++ " "
        | otherwise = show n

-- vraci tru pokud je tah legalni
checkMoveLegality :: Board -> Move -> Int -> Bool
checkMoveLegality board (pos1, pos2, pos3) playing = 
    getState board startX startY == playing + 1
   && checkLegality board pos1 pos2
   && checkLegality tempBoard pos2 pos3
    where
        (startX, startY) = pos1 
        tempBoard = board // [(pos1, 0)]

-- vraci true pokud je cesta mezi pos1 a pos2 legalni
checkLegality :: Board -> Pos -> Pos -> Bool
checkLegality board pos1 pos2 = case getPath pos1 pos2 of
    Nothing -> False
    Just path -> all (isPosEmpty board) path

-- vraci vsechny souradnice mezi pos1 a pos2
getPath :: Pos -> Pos -> Maybe [Pos]
getPath (x1,y1) (x2,y2)
    | isQueenMove && distance > 0 =
        Just [ (x1 + i * dirX, y1 + i * dirY) | i <- [1..distance] ]
    | otherwise = Nothing
  where
        dx = x2 - x1
        dy = y2 - y1
        dirX = signum dx
        dirY = signum dy
        distance = max (abs dx) (abs dy)
        isQueenMove = (dx == 0) || (dy == 0) || (abs dx == abs dy)

-- vraci true pokud je souradnice empty neboli stav je 0
isPosEmpty :: Board -> Pos -> Bool
isPosEmpty board (x,y) = getState board x y == 0


-- Hlavni loop hry
gameLoop :: Board -> Int -> Int -> IO ()
gameLoop board currentPlayer moveNumber = do
    putStrLn $ "Tah cislo: " ++ show (moveNumber)
    putStrLn "Aktualni stav desky:"
    putStrLn (renderBoard board)
    -- aby se to printlo hned
    hFlush stdout

    -- ai je na tahu
    if currentPlayer == 1
        then do
            putStrLn "AI je na tahu..."
            hFlush stdout
            -- dynamicke nastaveni hloubky
            let currentDepth
                    | numMoves > 600 = 2
                    | numMoves > 100 = 3
                    | numMoves > 20  = 4
                    | otherwise      = 5
                numMoves = length (getAllLegalMoves board currentPlayer)
            case getBestMove board currentPlayer currentDepth of
                Just move -> do
                    let newBoard = updateBoard board move currentPlayer
                    let nextPlayer = (currentPlayer + 1) `mod` 2
                    putStrLn $ "AI ma hloubku: " ++ show currentDepth
                    putStrLn $ "AI provedla tah: " ++ moveToString move
                    hFlush stdout
                    gameLoop newBoard nextPlayer (moveNumber + 1)
                Nothing -> do
                    putStrLn "AI nema zadny legalni tah. Hrac vyhral!"
                    hFlush stdout
        -- hrac je na tahu 
        else do
        
            putStrLn "Hrac je na tahu:"
            hFlush stdout

            input <- getLine
            case words input of
                "save":pathParts | not (null pathParts) -> do
                    let path = unwords pathParts
                    result <- tryIOError (writeFile path (serializeSave board currentPlayer moveNumber))
                    case result of
                        Left err -> putStrLn $ "Ulozeni se nezdarilo: " ++ show err
                        Right () -> putStrLn $ "Pozice ulozena do: " ++ path
                    gameLoop board currentPlayer moveNumber
                "load":pathParts | not (null pathParts) -> do
                    let path = unwords pathParts
                    result <- loadSave path
                    case result of
                        Left err -> do
                            putStrLn $ "Nacteni se nezdarilo: " ++ err
                            gameLoop board currentPlayer moveNumber
                        Right (loadedBoard, loadedPlayer, loadedMoveNumber) -> do
                            putStrLn $ "Pozice nactena ze: " ++ path
                            gameLoop loadedBoard loadedPlayer loadedMoveNumber
                _ -> case parseMove input of
                    Just move ->
                        if checkMoveLegality board move currentPlayer
                            then do
                                let newBoard = updateBoard board move currentPlayer
                                let nextPlayer = (currentPlayer + 1) `mod` 2
                                gameLoop newBoard nextPlayer (moveNumber + 1)
                            else do
                                putStrLn "Neplatny tah, zkuste to znovu."
                                gameLoop board currentPlayer moveNumber
                    Nothing -> do
                        putStrLn "Spatny format. Zadejte tah (napr. D1 D4 D5), save <soubor> nebo load <soubor>."
                        gameLoop board currentPlayer moveNumber

main :: IO ()
main = do
    putStrLn "==============================="
    putStrLn "   Vitejte ve hre Amazonky!    "
    putStrLn "==============================="
    putStrLn "Zadejte soubor pozice k nacteni (Enter = nova hra):"
    path <- getLine
    if null path
        then gameLoop initialBoard 0 0
        else do
            result <- loadSave path
            case result of
                Left err -> do
                    putStrLn $ "Nacteni se nezdarilo: " ++ err
                    gameLoop initialBoard 0 0
                Right (board, currentPlayer, moveNumber) ->
                    gameLoop board currentPlayer moveNumber


-- POMOCNE FUNKCE

-- vsechny pozice amazonek daneho hrace
getPlayerAmazons :: Board -> Int -> [Pos]
getPlayerAmazons board player = [ pos | (pos, state) <- assocs board, state == player + 1 ]


allPositions :: [Pos]
allPositions = [(x,y) | x <- [0..9], y <- [0..9]]

directions :: [(Int, Int)]
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

onBoard :: (Int, Int) -> Bool
onBoard (x, y) = x >= 0 && x <= 9 && y >= 0 && y <= 9
-- Vraci vsechny pozice mezi dvema pozicemi 
walk :: Board -> (Int, Int) -> (Int, Int) -> [(Int, Int)]
walk board (x, y) (dx, dy) =
    let nextPos = (x + dx, y + dy)
    in if onBoard nextPos && isPosEmpty board nextPos
       then nextPos : walk board nextPos (dx, dy) 
       else []

-- Vsechny pozice kam muzeme dojit pomoci queen move
getReachable :: Board -> Pos -> [Pos]
getReachable board pos = concatMap (walk board pos) directions

-- vsechny legalni tahy pro daneho hrace
getAllLegalMoves :: Board -> Int -> [Move]
getAllLegalMoves board player = do
    amazon <- getPlayerAmazons board player
    destination <- getReachable board amazon
    let tempBoard = board // [(amazon, 0)]
    arrow <- getReachable tempBoard destination
    return (amazon, destination, arrow)

-- NOVA RYCHLA HEURISTIKA
evaluateBoard :: Board -> Int -> Int
evaluateBoard board player = 
    let 
        playerMobility = sum [length (getReachable board amazon) | amazon <- getPlayerAmazons board player]
        opponentMobility = sum [length (getReachable board amazon) | amazon <- getPlayerAmazons board ((player + 1) `mod` 2)]
    in
        playerMobility - opponentMobility

getBestMove :: Board -> Int -> Int -> Maybe Move
getBestMove board ai depth =
    let legalMoves = getAllLegalMoves board ai
    in  
        if null legalMoves
        then Nothing 
        else 
            let 
                nextPlayer = (ai + 1) `mod` 2
                scoreMove move =
                    let newBoard = updateBoard board move ai
                    -- Vypočítá skóre pomocí alpha-beta algoritmu
                    in alphabeta newBoard (depth - 1) ai nextPlayer (-99999) 99999

                -- Vytvoří seznam dvojic
                scoresMoves = [(move, scoreMove move) | move <- legalMoves]
                bestMove = maximumBy (comparing snd) scoresMoves
            in Just (fst bestMove)

alphabeta :: Board -> Int -> Int -> Int -> Int -> Int -> Int
alphabeta board 0 ai _ _ _ = evaluateBoard board ai
alphabeta board depth ai currentPlayer alpha beta =
    let legalMoves = getAllLegalMoves board currentPlayer
    in if null legalMoves
        then
             if currentPlayer == ai 
                then -99999
                else 100000
        else
            let nextPlayer = (currentPlayer + 1) `mod` 2 
            in if currentPlayer == ai
                then evaluateMax board legalMoves depth nextPlayer alpha beta (-99999)
                else evaluateMin board legalMoves depth nextPlayer alpha beta 99999
    where
            evaluateMax  _ [] _ _ _ _ bestValue = bestValue
            evaluateMax board (move:moves) depth nextPlayer alpha beta bestValue =
                let newBoard = updateBoard board move currentPlayer
                    score = alphabeta newBoard (depth -1) ai nextPlayer alpha beta
                    newBestValue = max bestValue score
                    newAlpha = max alpha newBestValue
                in if newAlpha >= beta
                    then newBestValue
                    else evaluateMax board moves depth nextPlayer newAlpha beta newBestValue
            
            evaluateMin  _ [] _ _ _ _ bestValue = bestValue
            evaluateMin board (move:moves) depth nextPlayer alpha beta bestValue = 
                let newBoard = updateBoard board move currentPlayer
                    score = alphabeta newBoard (depth -1) ai nextPlayer alpha beta
                    newBestValue = min bestValue score
                    newBeta = min beta newBestValue
                in if alpha >= newBeta
                    then newBestValue 
                    else evaluateMin board moves depth nextPlayer alpha newBeta newBestValue