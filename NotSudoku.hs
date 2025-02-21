-- I'm going to hate my life

parse :: String -> Int
parse "x" = 0
parse c = read c

gridify :: Int -> [Int] -> [[Int]]
gridify _ [] = []
gridify cols grid = take cols grid : gridify cols (drop cols grid)

makeUp :: Int -> [Int] -> [Int]
makeUp a = map (\x -> if x == 0 then a else x)

flipGrid :: [[a]] -> [[a]]
flipGrid grid = reverse $ fliphelper grid []
  where
    fliphelper ([] : _) acc = acc
    fliphelper grid acc = fliphelper (map tail grid) (map head grid : acc)

triangle r = (r * (r + 1)) `div` 2

display = unlines . map (unwords . map show)

solve :: [Int] -> [[Int]]
solve (r : c : grid) = flipGrid $ map (\row -> makeUp (triangle r - sum (row)) row) $ flipGrid $ gridify c grid

main =
  interact $
    display . solve . map parse . words

-- THIS CANNOT BE THE NICEST HASKELL SOLUTION