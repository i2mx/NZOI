solve :: String -> String
solve s = if isBalanced s [] then "YES" else "NO"
  where
    isBalanced :: String -> String -> Bool
    isBalanced [] [] = True
    isBalanced [] _ = False
    isBalanced ('(' : xs) stack = isBalanced xs ('(' : stack)
    isBalanced ('[' : xs) stack = isBalanced xs ('[' : stack)
    isBalanced ('{' : xs) stack = isBalanced xs ('{' : stack)
    isBalanced (')' : xs) ('(' : stack) = isBalanced xs stack
    isBalanced (')' : xs) _ = False
    isBalanced (']' : xs) ('[' : stack) = isBalanced xs stack
    isBalanced (']' : xs) _ = False
    isBalanced ('}' : xs) ('{' : stack) = isBalanced xs stack
    isBalanced ('}' : xs) _ = False
    isBalanced (x : xs) stack = isBalanced xs stack

class Read' a where
  read' :: String -> a

instance Read' Int where
  read' = read

data Tree a = Leaf a | Node (Tree a) (Tree a)

data Tree' a where 
  Leaf' :: a -> Tree' a
  Node' :: Tree' a -> Tree' a -> Tree' a
  
main = interact $ solve . (!! 1) . lines
