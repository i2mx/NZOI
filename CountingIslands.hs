import System.IO
import qualified Data.Graph as Graph
import qualified Data.Set as Set

-- the input should be at most 1 megabyte

toCells :: [[Char]] -> [(Int, Int)]
toCells chars = [(x, y) | (y, row) <- zip [1 ..] chars, (x, cell) <- zip [1 ..] row, cell == '#']

toID :: Int -> Int -> (Int, Int) -> Graph.Vertex
toID width height (x, y) = x + (y - 1) * width

constructGraph :: Int -> Int -> [(Int, Int)] -> Graph.Graph
constructGraph width height cells = Graph.buildG bounds edges
  where
    getID = toID width height
    vertices = Set.fromList cells
    edges :: [Graph.Edge]
    edges =
      [(getID (x, y), getID (nx, ny)) | (x, y) <- cells, (nx, ny) <- [(x + 1, y), (x, y + 1)], Set.member (nx, ny) vertices]
    bounds :: (Graph.Vertex, Graph.Vertex)
    -- bounds = (0, width * height - 1)
    bounds = (1, width * height)

parse :: [String] -> (Int, Int, Int, [[Char]])
parse (x : xs) = (read a, read b, read c, xs)
  where
    [a, b, c] = words x

solve (width, height, 1, grid) = pseudo_islands - length (concatMap (filter (== '.')) grid)
  where
    pseudo_islands = length $ map length $ Graph.components graph
    graph = constructGraph width height $ toCells grid
solve (width, height, threshold, grid) = length $ filter (>= threshold) $ map length $ Graph.components graph
  where
    graph = constructGraph width height $ toCells grid

main = do 
  hSetBuffering stdin LineBuffering
  contents <- getContents
  print $ solve . parse . lines $ contents