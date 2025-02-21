-- okay this solution is not so bad

time n a b
  | remainder == 0 = bottom
  | remainder <= a = bottom + 1
  | otherwise = bottom + 2
  where
    remainder = n `mod` (a + b)
    bottom = 2 * (n `div` (a + b))

solve [n, a, b, c, d] = time n c d - time n a b

main = interact $ show . solve . map read . words